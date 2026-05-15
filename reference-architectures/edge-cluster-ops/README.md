# Edge Cluster Ops

Remote node management: three edge nodes connected to a central Kranix control plane. Workloads are deployed to specific nodes by label selector, and an MCP-connected agent monitors node health and redistributes workloads on node failure.

## What You'll Learn

- Edge node management
- Remote workload deployment
- Node label selectors
- Health monitoring at edge
- Automatic workload redistribution
- MCP agent for edge operations

## Prerequisites

- [`kranix-core`](https://github.com/kranix-io/kranix-core)
- [`kranix-runtime`](https://github.com/kranix-io/kranix-runtime) with remote backend
- [`kranix-mcp`](https://github.com/kranix-io/kranix-mcp)
- [`kranix-api`](https://github.com/kranix-io/kranix-api)
- Central Kubernetes cluster
- Three edge nodes (VMs or bare metal)
- Network connectivity between control plane and edge nodes

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
- Edge nodes registered
- Workloads deployed to specific nodes
- Health monitoring active
- MCP agent connected
- Node labels configured
- Redistribution policy ready

## Cleanup

```bash
make clean
```

## Troubleshooting

- Ensure edge nodes can reach control plane
- Check node registration: `kubectl get nodes`
- Verify labels: `kubectl get nodes --show-labels`
- Check MCP agent connectivity
- Verify network connectivity
- Check runtime backend configuration
