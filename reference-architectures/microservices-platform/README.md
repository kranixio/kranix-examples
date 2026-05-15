# Microservices Platform

A production-grade reference: five microservices, GitOps-managed via `KranixApp` CRDs, with namespace-per-environment isolation, policy enforcement, and an AI agent (Claude) available for on-call debugging via MCP.

## What You'll Learn

- Production microservices architecture
- GitOps with KranixApp CRDs
- Multi-environment isolation
- Policy enforcement at scale
- AI-powered debugging via MCP
- Service-to-service communication

## Prerequisites

- [`kranix-core`](https://github.com/kranix-io/kranix-core)
- [`kranix-api`](https://github.com/kranix-io/kranix-api)
- [`kranix-mcp`](https://github.com/kranix-io/kranix-mcp)
- [`kranix-operator`](https://github.com/kranix-io/kranix-operator)
- [`kranix-charts`](https://github.com/kranix-io/kranix-charts)
- GitHub Actions
- A Kubernetes cluster
- Claude Desktop or Claude API

## Setup

```bash
make setup
```

## Running the Example

```bash
make run
```

## Expected Output

You should see:
- Five microservices deployed
- GitOps reconciliation active
- Environments isolated
- Policies enforced
- MCP agent available
- Health dashboard operational

## Cleanup

```bash
make clean
```

## Troubleshooting

- Ensure all Kranix components are running
- Check GitOps workflow status
- Verify namespace isolation
- Check policy enforcement logs
- Ensure MCP connectivity
