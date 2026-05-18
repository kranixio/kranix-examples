# AI on-call runbook — PagerDuty → Kranix agent

End-to-end pattern: **PagerDuty** sends a webhook to a small **bridge service** that maps the incident to a **Kranix incident runbook** and calls `kranix-api` to **execute** it. The runbook encodes the steps your agent (or automation) performs: acknowledge, gather workload context, stream logs, restart, escalate, etc.

This example includes:

1. **`src/pagerduty_bridge.py`** — HTTP receiver for PagerDuty v2 generic webhooks; translates payload → `POST /api/v1/incident/runbooks/{id}/execute`.
2. **`src/agent_demo.py`** — Same API sequence **without** PagerDuty (lists runbooks, executes the seeded playbook, polls execution). Ideal for CI and laptops.
3. Alignment with **[`kranix-api` incident routes](https://github.com/kranix-io/kranix-api)** (`/api/v1/incident/runbooks`, `/execute`, `/executions`) and **`kranix-mock-api`** in [`kranix-packages`](https://github.com/kranix-io/kranix-packages) (seeded runbook `rb-oncall-pagerduty`).

## Prerequisites

- Python 3.10+
- Either a running **`kranix-api`** or **`kranix-mock-api`** (recommended for a first pass)

## Quick start (mock API)

From **`kranix-packages`** (separate clone):

```bash
go run ./cmd/kranix-mock-api -addr :18080 -skip-auth=true
```

From **this example**:

```bash
make setup
export KRANIX_API_URL=http://127.0.0.1:18080
python src/agent_demo.py
```

You should see the default **PagerDuty-aligned** runbook and an execution record.

## Run the PagerDuty bridge

Terminal 1 — mock or real API:

```bash
# mock
cd ../kranix-packages && go run ./cmd/kranix-mock-api -addr :18080 -skip-auth=true
```

Terminal 2 — bridge (listens on `:8090` by default):

```bash
cd observability/ai-oncall-pagerduty
make setup
export KRANIX_API_URL=http://127.0.0.1:18080
export BRIDGE_ADDR=:8090
python src/pagerduty_bridge.py
```

Terminal 3 — synthetic PagerDuty POST (shape is illustrative; adjust for your event):

```bash
curl -sS -X POST http://127.0.0.1:8090/hooks/pagerduty \
  -H 'Content-Type: application/json' \
  -d '{"event":{"id":"evt-demo","service":"checkout-api","severity":"critical","title":"Service down"}}'
```

## Ecosystem alignment

| Component | Role |
|-----------|------|
| [`kranix-api`](https://github.com/kranix-io/kranix-api) | `GET/POST /api/v1/incident/runbooks`, `POST …/execute`, executions CRUD |
| [`kranix-packages`](https://github.com/kranix-io/kranix-packages) | `kranix-mock-api` implements the same paths for tests + SSE `runbook.executed` |
| [`kranix-mcp`](https://github.com/kranix-io/kranix-mcp) | Optional: LLM agent calls tools that wrap the same API instead of raw HTTP |
| [`types/webhook.go`](https://github.com/kranix-io/kranix-packages/blob/main/types/webhook.go) | Webhook / event types for `PagerDuty` integration in platform configs |

## Production

- Use **signed** PagerDuty webhooks and verify signatures before executing runbooks.
- Map `service` / `urgency` → runbook ID via config or `kranix-api` metadata.
- Attach **`kranix-mcp`** or an internal agent worker to **poll executions** and run real remediation (Kubernetes, rollbacks, etc.) as `kranix-core` gains implementation behind the API.

## Cleanup

Stop the bridge and API processes (`Ctrl+C`). No cluster resources are created in the mock path.

## Makefile targets

| Target | Purpose |
|--------|---------|
| `make setup` | `pip install -r requirements.txt` |
| `make run-bridge` | Start PagerDuty webhook bridge |
| `make run-demo` | Run `agent_demo.py` against `KRANIX_API_URL` |
| `make verify` | `curl` health if bridge is up |
