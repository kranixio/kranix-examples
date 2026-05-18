# Cost optimization — rightsizing agent

An **automation / agent** pattern that reads **Kranix cost signals** and **applies conservative rightsizing** to over-provisioned workloads via **`PATCH /api/v1/workloads/{id}`**.

Aligned with:

- [`GET /api/v1/cost/summary`](https://github.com/kranix-io/kranix-api) — [`kranix-api`](https://github.com/kranix-io/kranix-api)
- [`GET /api/v1/workloads/{id}/cost`](https://github.com/kranix-io/kranix-api) (same shape as mock)

The reference implementation is **`src/rightsizing_agent.py`** (Python + **httpx**). Use **`kranix-mock-api`** for a safe dry run: the mock returns **`rightsizing.recommended_*`** fields derived from synthetic CPU utilization.

## Quick start

Terminal 1 — **`kranix-mock-api`**:

```bash
cd /path/to/kranix-packages
go run ./cmd/kranix-mock-api -addr :18080 -skip-auth=true
```

Terminal 2 — seed an “over-provisioned” workload and run the agent:

```bash
cd ai-agents/cost-optimization-agent
make setup
export KRANIX_API_URL=http://127.0.0.1:18080
export RIGHTSIZING_DRY_RUN=0   # set to 1 to only print recommendations
python src/rightsizing_agent.py
```

## Behavior

1. **`GET /api/v1/cost/summary`** for optional namespace filter.
2. For each workload in that namespace (from **`GET /api/v1/workloads`**), **`GET .../workloads/{id}/cost`**.
3. If **`rightsizing.reason`** contains **`candidate for rightsizing`**, **`PATCH`** the workload with **`cpuRequest` / `cpuLimit`** from recommendations (unless **`RIGHTSIZING_DRY_RUN=1`**).

## Ecosystem alignment

| Repo | Role |
|------|------|
| [`kranix-api`](https://github.com/kranix-io/kranix-api) | Cost + workload endpoints (stubs until `kranix-core` backs them) |
| [`kranix-packages`](https://github.com/kranix-io/kranix-packages) | Mock cost model, shared **`WorkloadSpec`** |
| [`kranix-mcp`](https://github.com/kranix-io/kranix-mcp) | Optional: LLM explains trade-offs before PATCH |

## Safety

- Default to **`RIGHTSIZING_DRY_RUN=1`** in CI.
- Gate production apply with a PR or **`kranix` policy**; this sample is **tutorial code**.

## Makefile

| Target | Action |
|--------|--------|
| `make setup` | `pip install -r requirements.txt` |
| `make run` | Run agent (requires env) |
| `make seed-overprovisioned` | `curl` POST a fat CPU limit into mock |
