# GPT Cluster Ops

GPT-4 connects via the HTTP/SSE transport of `kranix-mcp` and performs a full ops workflow: list namespaces, check cluster health, restart a degraded workload, and confirm recovery.

## What You'll Learn

- How to use HTTP/SSE transport with kranix-mcp
- Connect GPT-4 to Kranix via MCP
- Perform cluster operations through AI
- Monitor and recover from workload issues

## Prerequisites

- [`kranix-mcp`](https://github.com/kranix-io/kranix-mcp) running with HTTP transport
- OpenAI API key
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

Then interact with GPT-4 to perform cluster operations.

## Expected Output

GPT-4 should:
- List all namespaces
- Check cluster health status
- Identify degraded workloads
- Restart the workload
- Confirm recovery

## Cleanup

```bash
make clean
```

## Troubleshooting

- Ensure kranix-mcp HTTP transport is configured
- Verify OpenAI API key is set
- Check kranix-api connectivity
