#!/usr/bin/env sh
# Optional: start mock API from sibling kranix-packages repo, then run agent.
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PLATFORM_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PACKAGES="${KRANIX_PACKAGES_DIR:-$(cd "$PLATFORM_ROOT/../../.." && pwd)/../kranix-packages}"
PORT="${MOCK_PORT:-18080}"
if test -f "$PACKAGES/cmd/kranix-mock-api/main.go"; then
  (cd "$PACKAGES" && go run ./cmd/kranix-mock-api -addr ":$PORT" -skip-auth=true) &
  MOCK_PID=$!
  trap 'kill "$MOCK_PID" 2>/dev/null || true' EXIT
  sleep 1
fi
export KRANIX_API_URL="http://127.0.0.1:${PORT}"
exec python3 "$PLATFORM_ROOT/src/latency_agent.py"
