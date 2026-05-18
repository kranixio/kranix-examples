#!/usr/bin/env python3
"""Dry-run the on-call flow: list runbooks → execute PagerDuty playbook → show execution."""

from __future__ import annotations

import json
import os
import sys

import httpx

BASE = os.environ.get("KRANIX_API_URL", "http://127.0.0.1:8080").rstrip("/")
HEADERS = {"Accept": "application/json"}
if not os.environ.get("KRANIX_SKIP_AUTH"):
    key = os.environ.get("KRANIX_API_KEY", "")
    if key:
        HEADERS["Authorization"] = f"Bearer {key}"


def main() -> None:
    with httpx.Client(timeout=30.0) as client:
        r = client.get(f"{BASE}/api/v1/incident/runbooks", headers=HEADERS)
        r.raise_for_status()
        data = r.json()
        runbooks = data.get("runbooks") or []
        print("Runbooks:", len(runbooks))
        for rb in runbooks:
            print(f"  - {rb.get('id')}: {rb.get('name')}")

        rb_id = os.environ.get("RUNBOOK_ID", "rb-oncall-pagerduty")
        body = {
            "trigger": "agent_demo",
            "simulated_pagerduty": {
                "service": "checkout-api",
                "urgency": "high",
                "title": "Synthetic incident",
            },
        }
        r2 = client.post(
            f"{BASE}/api/v1/incident/runbooks/{rb_id}/execute",
            headers={**HEADERS, "Content-Type": "application/json"},
            json=body,
        )
        if r2.status_code >= 400:
            print(r2.status_code, r2.text, file=sys.stderr)
            sys.exit(1)
        ex = r2.json()
        print("Execute response:", json.dumps(ex, indent=2, default=str))


if __name__ == "__main__":
    main()
