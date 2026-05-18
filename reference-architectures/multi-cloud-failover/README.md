# Multi-cloud failover — AWS ↔ GCP

Reference pattern for workloads that can **run on AWS (EKS)** with **hot or warm standby on GCP (GKE)** (or the reverse), using health-based traffic shift and GitOps-aligned manifests.

## What you practice

1. **Same workload spec**, two cluster contexts (`kubectl config use-context` / CI credentials).
2. **Labels** such as `kranix.io/cloud: aws|gcp` and `kranix.io/role: primary|standby` for routing and policy.
3. **Health gates** — when the primary fails (synthetic or real), promote standby (apply manifest, flip DNS / global LB, or call **`kranix-api`** to update the active target).
4. **Observability** — `GET /_api/sse` or workload events for failover auditing (see [`kranix-packages` SSE types](https://github.com/kranix-io/kranix-packages/blob/main/types/sse.go)).

## Ecosystem alignment

| Repo | Role |
|------|------|
| [`kranix-api`](https://github.com/kranix-io/kranix-api) | REST for deploy / patch / restart across logical backends |
| [`kranix-operator`](https://github.com/kranix-io/kranix-operator) | Reconcile `KranixApp` per cluster |
| [`kranix-packages`](https://github.com/kranix-io/kranix-packages) | Shared workload types; **`kranix-mock-api`** for local failover drills |
| [`kranix-mcp`](https://github.com/kranix-io/kranix-mcp) | Optional: agent summarizes dual-cluster status |

## Layout (conceptual)

```
                    Global DNS / LB
                          │
          ┌───────────────┴────────────────┐
          ▼                                 ▼
    EKS (primary)                      GKE (standby)
    Kranix runtime                      Kranix runtime
```

## Files

| Path | Purpose |
|------|---------|
| `manifests/workload-primary.aws.sample.yaml` | Sample doc + labels for AWS-active |
| `manifests/workload-standby.gcp.sample.yaml` | Same app identity, GCP standby |
| `scripts/failover-drill.sh` | **Local:** patch workload labels on **`kranix-mock-api`** to simulate standby promotion |

## Quick drill (mock API)

Terminal 1 — [`kranix-packages`](https://github.com/kranix-io/kranix-packages):

```bash
go run ./cmd/kranix-mock-api -addr :18080 -skip-auth=true
```

Terminal 2 — this example:

```bash
export KRANIX_API_URL=http://127.0.0.1:18080
chmod +x scripts/failover-drill.sh
./scripts/failover-drill.sh
```

The script deploys a workload tagged **AWS primary**, simulates failure, **PATCH**es metadata to **GCP active**, and optionally hits **`GET /api/sse/stats`** to show listeners.

## Production checklist

- **Terraform / Cluster API** for peer clusters; **external-dns** + health-checked LB.
- **Zero-durable state** or **async replication** for data plane before doing automatic failover.
- **Runbook** in [`observability/ai-oncall-pagerduty`](../../observability/ai-oncall-pagerduty/) for human approval on real cuts.

## Makefile

```bash
make setup    # chmod scripts (Unix)
make run      # same as failover-drill.sh when KRANIX_API_URL is set
make verify   # curl mock health
```

## Cleanup

No long-lived cloud resources in the mock path; stop **`kranix-mock-api`** when done.
