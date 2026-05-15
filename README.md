# kranix-examples

> Example projects, starter templates, and reference architectures for the Kranix ecosystem.

This repo is the fastest way to go from zero to a working Kranix setup. Whether you're deploying your first container, connecting an AI agent to your cluster, or building a full GitOps pipeline — there's a runnable example here for it.

Every example is self-contained, documented, and tested against the latest Kranix release.

---

## Structure

```
kranix-examples/
├── quickstart/                   # Absolute first steps
│   ├── docker-hello-world/       # Deploy a container with kranix-cli
│   └── kubernetes-hello-world/   # Deploy to a local k8s cluster
│
├── ai-agents/                    # MCP + AI agent integration
│   ├── claude-deploy-app/        # Claude deploys and monitors a workload
│   ├── claude-debug-crash/       # Claude analyzes and fixes a failing pod
│   ├── gpt-cluster-ops/          # GPT-4 operating a namespace via MCP
│   └── custom-mcp-agent/         # Build your own MCP-compatible agent
│
├── gitops/                       # GitOps workflows with KranixApp CRDs
│   ├── single-app-gitops/        # One app, one namespace, full GitOps loop
│   ├── multi-env-promotion/      # dev → staging → production promotion
│   └── auto-rollback/            # Automatic rollback on health gate failure
│
├── platform-engineering/         # IDP and platform patterns
│   ├── namespace-per-team/       # Isolated namespaces with KranixPolicy
│   ├── self-service-deploy/      # Developer self-service via kranix-api
│   └── policy-enforcement/       # Resource limits and network policy
│
├── observability/                # Monitoring and debugging
│   ├── ai-failure-analysis/      # krane analyze in a real crash scenario
│   ├── log-streaming/            # Real-time log aggregation example
│   └── cluster-health-dashboard/ # Health dashboard using kranix-api
│
├── local-dev/                    # Local development environments
│   ├── local-k8s-cluster/        # Full local cluster with kind + Kranix
│   ├── ephemeral-environments/   # Spin up and tear down dev envs on demand
│   └── docker-compose-stack/     # Compose stack managed by Kranix runtime
│
└── reference-architectures/      # Full production-grade blueprints
    ├── microservices-platform/   # Multi-service app with GitOps + MCP ops
    ├── ml-inference-platform/    # GPU workloads + AI agent orchestration
    └── edge-cluster-ops/         # Remote node management at the edge
```

---

## Quickstart

If you're new to Kranix, start here:

```bash
git clone https://github.com/kranix-io/kranix-examples
cd kranix-examples/quickstart/docker-hello-world
```

Follow the `README.md` inside each example — every one has its own prerequisites, setup steps, and expected output.

---

## Examples

### Quickstart

#### `quickstart/docker-hello-world`
Deploy your first container using `kranix-cli`. No Kubernetes required. Shows the full deploy → status → logs → teardown loop in under 5 minutes.

**What you'll use:** `kranix-cli`, `kranix-runtime` (Docker backend)

---

#### `quickstart/kubernetes-hello-world`
Deploy a workload to a local Kubernetes cluster (`kind`). Covers namespace creation, deployment, and log streaming via the CLI.

**What you'll use:** `kranix-cli`, `kranix-api`, `kind`

---

### AI agents

#### `ai-agents/claude-deploy-app`
Connect Claude Desktop to `kranix-mcp` and use it to deploy an nginx workload, check its status, and stream logs — all through a natural language conversation.

**What you'll use:** `kranix-mcp`, Claude Desktop, `kranix-api`

```
You → Claude: "Deploy nginx to the staging namespace with 2 replicas"
Claude → kranix-mcp → kranix-api → cluster
Claude → You: "nginx is running. 2/2 replicas ready. Here are the logs..."
```

---

#### `ai-agents/claude-debug-crash`
A deliberately broken deployment (bad image tag, OOM config) is handed to Claude. Claude uses `analyze_workload` to identify the crash reason, suggest a fix, and apply a corrected manifest.

**What you'll use:** `kranix-mcp`, `kranix-api`, Claude API

---

#### `ai-agents/gpt-cluster-ops`
GPT-4 connects via the HTTP/SSE transport of `kranix-mcp` and performs a full ops workflow: list namespaces, check cluster health, restart a degraded workload, and confirm recovery.

**What you'll use:** `kranix-mcp` (HTTP transport), OpenAI API

---

#### `ai-agents/custom-mcp-agent`
A minimal Python script that implements an MCP client and connects to `kranix-mcp`. Shows the raw MCP protocol flow — tool discovery, tool call, result handling — without relying on Claude or GPT.

**What you'll use:** `kranix-mcp`, Python MCP client library

---

### GitOps

#### `gitops/single-app-gitops`
A single `KranixApp` manifest committed to a Git repo. The Kranix operator watches the CRD and reconciles on every commit. Demonstrates the full GitOps loop: commit → operator detects change → runtime applies → status updated.

**What you'll use:** `kranix-operator`, `kranix-charts`, `kind`

```yaml
# kranixapp.yaml
apiVersion: kranix.io/v1alpha1
kind: KranixApp
metadata:
  name: api-server
  namespace: production
spec:
  image: myorg/api-server:v1.4.2
  replicas: 3
```

---

#### `gitops/multi-env-promotion`
Three branches (`dev`, `staging`, `main`) each map to a namespace. A GitHub Actions workflow promotes a workload image tag from dev → staging → production using the Kranix API, with a manual approval gate before production.

**What you'll use:** `kranix-operator`, `kranix-api`, GitHub Actions

---

#### `gitops/auto-rollback`
A `KranixApp` with `autoHeal: true` and a `healthCheckPath`. A bad deployment is introduced. The operator detects the health gate failure and automatically rolls back to the last known-good spec. Shows the full rollback event in the CRD status.

**What you'll use:** `kranix-operator`, `kranix-core`

---

### Platform engineering

#### `platform-engineering/namespace-per-team`
Three teams, three namespaces, one cluster. Each namespace has a `KranixPolicy` enforcing CPU/memory limits, network isolation, and image pull restrictions. Shows how platform teams can define policy once and apply it consistently.

**What you'll use:** `kranix-operator`, `KranixPolicy`, `KranixNamespace`

---

#### `platform-engineering/self-service-deploy`
A minimal internal developer portal (HTML + JS) that calls `kranix-api` directly, allowing developers to deploy pre-approved workloads to their own namespace without needing `kubectl` or CLI access.

**What you'll use:** `kranix-api`, `kranix-packages` (TypeScript SDK)

---

#### `platform-engineering/policy-enforcement`
Demonstrates how `KranixPolicy` blocks a non-compliant workload (missing resource limits, privileged container) and emits a policy violation event — before it ever reaches the runtime.

**What you'll use:** `kranix-operator`, `kranix-core`, `KranixPolicy`

---

### Observability

#### `observability/ai-failure-analysis`
A simulated crash scenario (OOMKilled, CrashLoopBackOff, missing ConfigMap). Runs `kranix analyze` against each and shows the structured output: crash reason, probable fix, resource recommendation, and generated patch.

**What you'll use:** `kranix-cli`, `kranix-api`, `kranix-core`

---

#### `observability/log-streaming`
Streams logs from a multi-replica workload in real time using both `kranix logs --follow` (CLI) and the SSE endpoint directly (`/api/v1/pods/:id/logs`). Useful for understanding how to build log tooling on top of Kranix.

**What you'll use:** `kranix-cli`, `kranix-api`

---

#### `observability/cluster-health-dashboard`
A simple React dashboard that polls `kranix-api` for cluster health, workload statuses, and recent events — rendered in a browser. Shows how to build ops tooling directly on the Kranix API.

**What you'll use:** `kranix-api`, `kranix-packages` (TypeScript SDK), React

---

### Local dev

#### `local-dev/local-k8s-cluster`
Full local Kranix setup on a `kind` cluster — installs `kranix-charts`, verifies operator health, creates a test namespace, and deploys a sample app. The recommended starting point before any cloud deployment.

**What you'll use:** `kind`, `kranix-charts`, `kranix-cli`

---

#### `local-dev/ephemeral-environments`
Creates a fresh namespace + workload on demand (e.g. per Git branch or PR), runs a test suite against it, then tears the whole environment down. Shows how to use the Kranix API in CI for ephemeral test environments.

**What you'll use:** `kranix-api`, GitHub Actions, `kranix-packages` (Go SDK)

---

#### `local-dev/docker-compose-stack`
A three-service Compose stack (API, worker, Postgres) managed by the Kranix Docker runtime. Demonstrates compose lifecycle management, inter-service networking, and log aggregation through Kranix.

**What you'll use:** `kranix-runtime` (Compose backend), `kranix-cli`

---

### Reference architectures

#### `reference-architectures/microservices-platform`
A production-grade reference: five microservices, GitOps-managed via `KranixApp` CRDs, with namespace-per-environment isolation, policy enforcement, and an AI agent (Claude) available for on-call debugging via MCP.

**Components:** `kranix-core`, `kranix-api`, `kranix-mcp`, `kranix-operator`, `kranix-charts`, GitHub Actions

---

#### `reference-architectures/ml-inference-platform`
A machine learning inference platform: model server deployment, GPU workload scheduling, health-gated rollouts for new model versions, and an AI agent that monitors inference latency and triggers rollback when thresholds are breached.

**Components:** `kranix-core`, `kranix-mcp`, `kranix-operator`, KServe integration

---

#### `reference-architectures/edge-cluster-ops`
Remote node management: three edge nodes connected to a central Kranix control plane. Workloads are deployed to specific nodes by label selector, and an MCP-connected agent monitors node health and redistributes workloads on node failure.

**Components:** `kranix-core`, `kranix-runtime` (remote backend), `kranix-mcp`, `kranix-api`

---

## Running an example

Every example follows the same structure:

```
example-name/
├── README.md          # What it does, prerequisites, and steps
├── Makefile           # make setup / make run / make clean
├── manifests/         # KranixApp, KranixPolicy, and K8s YAMLs
├── scripts/           # Setup and teardown shell scripts
└── src/               # Application code (if applicable)
```

Common commands available in most examples:

```bash
make setup    # install prerequisites, create cluster or namespace
make run      # deploy the example
make verify   # check expected state
make clean    # tear everything down
```

---

## Prerequisites (general)

Most examples require some combination of:

- [`kranix-cli`](https://github.com/kranix-io/kranix-cli) installed
- Docker Desktop or a Docker daemon running
- `kind` for Kubernetes examples (`brew install kind`)
- `helm` for chart-based examples (`brew install helm`)
- A running `kranix-api` (local or remote)

Each example's own `README.md` lists exactly what it needs.

---

## Contributing

New examples are welcome. Good candidates:

- A real use case you solved with Kranix
- An integration with another tool (ArgoCD, Backstage, Grafana, etc.)
- A simpler version of an existing example
- A reference architecture for a specific industry or stack

To contribute an example:

1. Copy the structure of the closest existing example
2. Add a `README.md` with: what it does, prerequisites, steps, and expected output
3. Include a `Makefile` with at minimum `setup`, `run`, and `clean` targets
4. Open a PR — we'll review and test it against the latest Kranix release

See [CONTRIBUTING.md](./CONTRIBUTING.md) for full guidelines.

---

## Related repos

| Repo | Description |
|---|---|
| [`kranix-core`](https://github.com/kranix-io/kranix-core) | Orchestration engine |
| [`kranix-api`](https://github.com/kranix-io/kranix-api) | REST / gRPC API |
| [`kranix-mcp`](https://github.com/kranix-io/kranix-mcp) | MCP server for AI agents |
| [`kranix-cli`](https://github.com/kranix-io/kranix-cli) | Terminal UX |
| [`kranix-operator`](https://github.com/kranix-io/kranix-operator) | Kubernetes operator |
| [`kranix-charts`](https://github.com/kranix-io/kranix-charts) | Helm charts |
| [`kranix-packages`](https://github.com/kranix-io/kranix-packages) | Shared SDK |
| [`kranix-web`](https://github.com/kranix-io/kranix-web) | Website and documentation |

---

## License

Apache 2.0 — see [LICENSE](./LICENSE).

Example application code (inside `src/` directories) is provided as-is for learning purposes and carries no warranty.
