# Docker Compose Stack

A three-service Compose stack (API, worker, Postgres) managed by the Kranix Docker runtime. Demonstrates compose lifecycle management, inter-service networking, and log aggregation through Kranix.

## What You'll Learn

- How to manage Compose stacks with Kranix
- Inter-service networking
- Log aggregation across services
- Compose lifecycle management
- Using kranix-runtime with Compose backend

## Prerequisites

- [`kranix-runtime`](https://github.com/kranix-io/kranix-runtime) with Compose backend
- [`kranix-cli`](https://github.com/kranix-io/kranix-cli) installed
- Docker Desktop or Docker daemon running
- Docker Compose

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
- Compose stack deployed
- Three services running (API, worker, Postgres)
- Inter-service networking configured
- Logs aggregated from all services
- Health checks passing

## Cleanup

```bash
make clean
```

## Troubleshooting

- Ensure Docker daemon is running
- Check kranix-runtime is accessible
- Verify Compose file syntax
- Check service logs: `kranix logs`
- Ensure ports are not already in use
