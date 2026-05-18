# ML inference platform — GPU workloads and latency agent

Reference pattern for **GPU-backed inference** on Kranix: deploy a model-serving workload with **`resources.gpu`**, push **inference latency** metrics to **`kranix-api` analytics**, and run a small **monitoring agent** that watches **p99 latency** and recommends **rollback** when a threshold is exceeded.

Two paths:

| Path | Purpose |
|------|---------|
| **Local / CI (`run-local`)** | Uses [`kranix-mock-api`](https://github.com/kranix-io/kranix-packages/tree/main/cmd/kranix-mock-api) + Python agent — no Kubernetes |
| **Cluster (`run-k8s`)** | Prior placeholder flow: KServe / GPU cluster (requires ops setup) |

## Ecosystem alignment

| Repo | Role |
|------|------|
| [`kranix-api`](https://github.com/kranix-io/kranix-api) | `POST /api/v1/analytics/metrics`, `GET /api/v1/analytics/workloads/{id}?type=latency` |
| [`kranix-packages`](https://github.com/kranix-io/kranix-packages) | Shared **`WorkloadSpec`** / **`GPUSpec`**, Python & TS SDKs, **`kranix-mock-api`** analytics |
| [`kranix-mcp`](https://github.com/kranix-io/kranix-mcp) | Optional: natural-language “why is p99 high?” using the same metrics API |
| [`kranix-operator`](https://github.com/kranix-io/kranix-operator) | Production: reconcile GPU node selectors + policies |

## Prerequisites (local)

- Python 3.10+
- Go 1.22+ (to run `kranix-mock-api` from `kranix-packages`)

## Local demo

Terminal 1 — from your `kranix-packages` clone:

```bash
go run ./cmd/kranix-mock-api -addr :18080 -skip-auth=true
```

Terminal 2 — this example:

```bash
make setup
export KRANIX_API_URL=http://127.0.0.1:18080
make run-local
```

The agent will deploy a **mock** GPU workload, synthesize latency samples, print **p50/p95/p99**, and emit an alert when **p99** crosses the configured threshold (see `src/latency_agent.py`).

## Full Kubernetes path

For a real cluster with NVIDIA device plugins and KServe (operators team):

```bash
make setup-k8s
make run-k8s
make verify
make clean-k8s
```

Scripts under `scripts/` are stubs you can replace with your org’s installers.

## Files

- `manifests/gpu-workload.example.json` — REST example body (GPU + backend) aligned with [`types/workload.go`](https://github.com/kranix-io/kranix-packages/blob/main/types/workload.go)
- `src/latency_agent.py` — deploy + metrics + threshold logic
- `scripts/run_local_mock.sh` — optional one-liner wrapper

## Cleanup

Local: stop the mock API and agent processes. Cluster: `make clean-k8s`.
