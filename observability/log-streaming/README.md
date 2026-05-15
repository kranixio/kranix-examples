# Log Streaming

Streams logs from a multi-replica workload in real time using both `kranix logs --follow` (CLI) and the SSE endpoint directly (`/api/v1/pods/:id/logs`). Useful for understanding how to build log tooling on top of Kranix.

## What You'll Learn

- How to stream logs with kranix-cli
- Use SSE endpoint for log streaming
- Handle multi-replica log aggregation
- Build custom log tooling
- Log filtering and parsing

## Prerequisites

- [`kranix-cli`](https://github.com/kranix-io/kranix-cli) installed
- [`kranix-api`](https://github.com/kranix-io/kranix-api) running
- kubectl configured
- A Kubernetes cluster
- curl or similar tool for SSE testing

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
- Multi-replica workload deployed
- Logs streaming in real-time via CLI
- Logs streaming via SSE endpoint
- Log aggregation from all replicas
- Timestamp and pod information

## Cleanup

```bash
make clean
```

## Troubleshooting

- Ensure kranix-api is running
- Check workload has multiple replicas
- Verify SSE endpoint is accessible
- Check network connectivity
