#!/usr/bin/env python3
"""
Receives PagerDuty-style JSON POSTs and executes a Kranix incident runbook.

SECURITY: For production, verify PagerDuty webhook signatures and authenticate callers.
"""

from __future__ import annotations

import json
import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

import httpx

BASE = os.environ.get("KRANIX_API_URL", "http://127.0.0.1:8080").rstrip("/")
LISTEN = os.environ.get("BRIDGE_ADDR", ":8090")
DEFAULT_RUNBOOK = os.environ.get("DEFAULT_RUNBOOK_ID", "rb-oncall-pagerduty")
SKIP_AUTH = os.environ.get("KRANIX_SKIP_AUTH", "1") == "1"
API_KEY = os.environ.get("KRANIX_API_KEY", "")


def api_headers() -> dict[str, str]:
    h = {"Accept": "application/json", "Content-Type": "application/json"}
    if not SKIP_AUTH and API_KEY:
        h["Authorization"] = f"Bearer {API_KEY}"
    return h


def map_payload_to_runbook(body: dict) -> tuple[str, dict]:
    """Resolve runbook id + execution payload from webhook JSON."""
    event = body.get("event") or body.get("messages", [{}])[0] if body.get("messages") else {}
    if isinstance(event, list):
        event = event[0] if event else {}
    service = (
        event.get("service")
        or event.get("service_name")
        or body.get("service")
        or "unknown-service"
    )
    runbook = body.get("runbook_id") or DEFAULT_RUNBOOK
    execution = {
        "source": "pagerduty",
        "raw": body,
        "service": service,
        "severity": event.get("severity") or body.get("severity"),
        "title": event.get("title") or body.get("title"),
    }
    return str(runbook), execution


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args) -> None:  # noqa: A003
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def do_GET(self) -> None:  # noqa: N802
        if urlparse(self.path).path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status":"ok"}')
            return
        self.send_error(404)

    def do_POST(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path != "/hooks/pagerduty":
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length) if length else b"{}"
        try:
            body = json.loads(raw.decode() or "{}")
        except json.JSONDecodeError:
            self.send_error(400, "invalid json")
            return
        rb_id, execution = map_payload_to_runbook(body)
        try:
            with httpx.Client(timeout=60.0) as client:
                r = client.post(
                    f"{BASE}/api/v1/incident/runbooks/{rb_id}/execute",
                    headers=api_headers(),
                    json=execution,
                )
                r.raise_for_status()
                out = r.json()
        except Exception as e:  # noqa: BLE001
            self.send_response(502)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())
            return
        self.send_response(202)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(out).encode())


def main() -> None:
    host, port = "0.0.0.0", 8090
    if LISTEN.startswith(":"):
        port = int(LISTEN[1:])
    elif ":" in LISTEN:
        host_part, p = LISTEN.rsplit(":", 1)
        if host_part:
            host = host_part
        port = int(p)
    server = HTTPServer((host, port), Handler)
    print(f"pagerduty_bridge listening on http://{host}:{port}", file=sys.stderr)
    print(f"forwarding to {BASE} runbook execute (default id: {DEFAULT_RUNBOOK})", file=sys.stderr)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()


if __name__ == "__main__":
    main()
