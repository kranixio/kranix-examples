# ML Inference Platform

A machine learning inference platform: model server deployment, GPU workload scheduling, health-gated rollouts for new model versions, and an AI agent that monitors inference latency and triggers rollback when thresholds are breached.

## What You'll Learn

- Deploy ML model servers
- GPU workload scheduling
- Health-gated rollouts
- Monitor inference latency
- AI-driven rollback automation
- Model version management

## Prerequisites

- [`kranix-core`](https://github.com/kranix-io/kranix-core)
- [`kranix-mcp`](https://github.com/kranix-io/kranix-mcp)
- [`kranix-operator`](https://github.com/kranix-io/kranix-operator)
- KServe installed
- GPU-enabled Kubernetes cluster
- NVIDIA device plugins
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
- Model server deployed on GPU
- Inference endpoint available
- Health checks configured
- Latency monitoring active
- AI agent watching thresholds
- Rollback automation ready

## Cleanup

```bash
make clean
```

## Troubleshooting

- Ensure GPU nodes are available: `kubectl get nodes -l accelerator=nvidia-gpu`
- Check KServe installation
- Verify model server pods: `kubectl get pods -n inference`
- Check GPU allocation: `kubectl describe node`
- Ensure MCP agent is connected
