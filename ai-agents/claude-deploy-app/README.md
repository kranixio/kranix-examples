# Claude Deploy App

Connect Claude Desktop to `kranix-mcp` and use it to deploy an nginx workload, check its status, and stream logs — all through a natural language conversation.

## What You'll Learn

- How to configure Claude Desktop with kranix-mcp
- Use natural language to deploy workloads
- Monitor deployment status via Claude
- Stream logs through the AI agent

## Prerequisites

- [`kranix-mcp`](https://github.com/kranix-io/kranix-mcp) installed and running
- Claude Desktop installed
- A running `kranix-api` instance
- A Kubernetes cluster

## Setup

```bash
make setup
```

## Running the Example

```bash
make run
```

Then in Claude Desktop, ask: "Deploy nginx to the staging namespace with 2 replicas"

## Expected Output

Claude should respond with:
- Confirmation of deployment
- Status showing replicas ready
- Log output from the pods

## Cleanup

```bash
make clean
```

## Troubleshooting

- Ensure kranix-mcp is running and accessible
- Check Claude Desktop MCP configuration
- Verify kranix-api connectivity
