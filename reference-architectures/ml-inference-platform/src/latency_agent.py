#!/usr/bin/env python3
"""
Deploy a GPU inference workload (via kranix-api) and monitor latency percentiles.

Uses POST /api/v1/analytics/metrics and GET .../analytics/workloads/{id}?type=latency
(mock implementation in kranix-packages kranix-mock-api).
"""

from __future__ import annotations

import json
import os
import random
import sys
import time
from datetime import datetime, timezone

import httpx

BASE = os.environ.get("KRANIX_API_URL", "http://127.0.0.1:8080").rstrip("/")
API_KEY = os.environ.get("KRANIX_API_KEY", "")
P99_THRESHOLD_MS = float(os.environ.get("INFERENCE_P99_THRESHOLD_MS", "40"))
ROUNDS = int(os.environ.get("AGENT_ROUNDS", "8"))


def headers(*, json_ct: bool = False) -> dict[str, str]:
    h = {"Accept": "application/json"}
    if API_KEY:
        h["Authorization"] = f"Bearer {API_KEY}"
    if json_ct:
        h["Content-Type"] = "application/json"
    return h


def deploy(body: dict) -> dict:
    with httpx.Client(timeout=60.0) as client:
        r = client.post(f"{BASE}/api/v1/workloads", headers=headers(json_ct=True), json=body)
        r.raise_for_status()
        return r.json()


def record_latency(workload_id: str, value_ms: float) -> None:
    metric = {
        "metricType": "latency",
        "resourceId": workload_id,
        "resourceType": "workload",
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "value": value_ms,
        "labels": {"type": "inference_latency"},
    }
    with httpx.Client(timeout=30.0) as client:
        r = client.post(f"{BASE}/api/v1/analytics/metrics", headers=headers(json_ct=True), json=metric)
        r.raise_for_status()


def fetch_latency(workload_id: str) -> dict:
    with httpx.Client(timeout=30.0) as client:
        r = client.get(
            f"{BASE}/api/v1/analytics/workloads/{workload_id}",
            params={"type": "latency"},
            headers=headers(),
        )
        r.raise_for_status()
        return r.json()


def main() -> None:
    spec_path = os.path.join(os.path.dirname(__file__), "..", "manifests", "gpu-workload.example.json")
    with open(spec_path, encoding="utf-8") as f:
        spec = json.load(f)
    spec.setdefault("namespace", "default")
    spec["name"] = spec.get("name", "ml-demo") + "-" + str(random.randint(1000, 9999))
    print("Deploying GPU workload:", spec["name"], file=sys.stderr)
    wl = deploy(spec)
    wid = wl.get("id")
    if not wid:
        print("Unexpected deploy response:", wl, file=sys.stderr)
        sys.exit(1)
    print("Workload id:", wid, file=sys.stderr)

    degraded = False
    for i in range(ROUNDS):
        base = 15.0 + random.random() * 10
        if i >= ROUNDS // 2:
            base += 35 + random.random() * 30
            degraded = True
        record_latency(wid, round(base, 2))
        time.sleep(0.15)
        snap = fetch_latency(wid)
        lat = snap.get("latency") or {}
        p99 = lat.get("p99Ms")
        print(f"round={i} p99_ms={p99} avg_ms={lat.get('avgMs')} samples={lat.get('samples')}")
        if p99 is not None and float(p99) > P99_THRESHOLD_MS:
            print(
                f"ALERT: p99 {p99}ms exceeds threshold {P99_THRESHOLD_MS}ms -> "
                "recommend canary rollback / model revision check (integrate with kranix-mcp or GitOps).",
                file=sys.stderr,
            )
    if degraded:
        print("Agent completed: observed elevated tail latency in second half of simulation.", file=sys.stderr)


if __name__ == "__main__":
    main()
