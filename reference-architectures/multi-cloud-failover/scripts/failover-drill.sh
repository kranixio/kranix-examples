#!/usr/bin/env bash
set -euo pipefail
BASE="${KRANIX_API_URL:-http://127.0.0.1:8080}"
BASE="${BASE%/}"

echo "==> Deploy primary (AWS-labeled) workload via kranix-api"
PAYLOAD=$(dirname "$0")/../manifests/workload-api-primary.aws.json
curl -sS -X POST "$BASE/api/v1/workloads" \
  -H 'Content-Type: application/json' \
  --data-binary "@$PAYLOAD" | tee /tmp/kranix-failover-wl.json
WL_ID=$(python3 -c "import json;print(json.load(open('/tmp/kranix-failover-wl.json'))['id'])" 2>/dev/null || echo "")
if [[ -z "$WL_ID" ]]; then
  echo "Deploy failed or unexpected response"
  exit 1
fi
echo "Workload: $WL_ID"

echo "==> Simulate primary failure / operator decision: PATCH to GCP-active posture"
curl -sS -X PATCH "$BASE/api/v1/workloads/$WL_ID" \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "payments-api-primary",
    "namespace": "default",
    "image": "your-registry/payments-api:v1.4.0",
    "replicas": 3,
    "backend": "kubernetes",
    "resources": {
      "cpuRequest": "500m",
      "cpuLimit": "2",
      "memoryRequest": "512Mi",
      "memoryLimit": "2Gi"
    },
    "labels": {
      "kranix.io/cloud": "gcp",
      "kranix.io/role": "active",
      "kranix.io/app": "payments-api",
      "kranix.io/failover": "from-aws-drill"
    }
  }' | tee /tmp/kranix-failover-patched.json

echo "==> SSE subscribers count (if supported)"
curl -sS "$BASE/api/sse/stats" || true
echo
echo "Drill complete. In production: shift DNS / GLB to GKE and scale standby."
