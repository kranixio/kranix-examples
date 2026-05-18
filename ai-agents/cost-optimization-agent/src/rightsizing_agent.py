#!/usr/bin/env python3
"""Rightsizing agent: cost + utilization -> PATCH workload (optional)."""

from __future__ import annotations

import json
import os
import sys

import httpx

BASE = os.environ.get("KRANIX_API_URL", "http://127.0.0.1:8080").rstrip("/")
NS = os.environ.get("RIGHTSIZING_NAMESPACE", "default")
DRY = os.environ.get("RIGHTSIZING_DRY_RUN", "1") == "1"
API_KEY = os.environ.get("KRANIX_API_KEY", "")


def headers(*, json_ct: bool = False) -> dict[str, str]:
    h = {"Accept": "application/json"}
    if API_KEY:
        h["Authorization"] = f"Bearer {API_KEY}"
    if json_ct:
        h["Content-Type"] = "application/json"
    return h


def main() -> None:
    with httpx.Client(timeout=60.0) as client:
        r = client.get(
            f"{BASE}/api/v1/cost/summary",
            params={"namespace": NS} if NS else None,
            headers=headers(),
        )
        r.raise_for_status()
        print("cost summary:", json.dumps(r.json(), indent=2))

        lr = client.get(
            f"{BASE}/api/v1/workloads",
            params={"namespace": NS},
            headers=headers(),
        )
        lr.raise_for_status()
        body = lr.json()
        workloads = body if isinstance(body, list) else body.get("workloads") or []

        for wl in workloads:
            wid = wl.get("id")
            if not wid:
                continue
            cr = client.get(f"{BASE}/api/v1/workloads/{wid}/cost", headers=headers())
            if cr.status_code >= 400:
                print(f"skip {wid}: cost {cr.status_code}", file=sys.stderr)
                continue
            cost = cr.json()
            rs = cost.get("rightsizing") or {}
            reason = str(rs.get("reason") or "")
            if "candidate for rightsizing" not in reason.lower():
                print(f"{wid}: no action ({reason[:60] or 'ok'})")
                continue
            print(f"{wid}: RECOMMEND cpu_request={rs.get('recommended_cpu_request')} "
                  f"cpu_limit={rs.get('recommended_cpu_limit')}")
            if DRY:
                print("  (dry-run: no PATCH)")
                continue
            spec = wl.get("spec") or {}
            spec["resources"] = spec.get("resources") or {}
            spec["resources"]["cpuRequest"] = rs.get("recommended_cpu_request")
            spec["resources"]["cpuLimit"] = rs.get("recommended_cpu_limit")
            payload = {**spec, "labels": wl.get("labels") or {}}
            pr = client.patch(
                f"{BASE}/api/v1/workloads/{wid}",
                headers=headers(json_ct=True),
                json=payload,
            )
            if pr.status_code >= 400:
                print(f"  PATCH failed {pr.status_code} {pr.text}", file=sys.stderr)
            else:
                print("  PATCH ok:", pr.json().get("id", wid))


if __name__ == "__main__":
    main()
