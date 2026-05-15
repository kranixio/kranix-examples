# Auto Rollback

A `KranixApp` with `autoHeal: true` and a `healthCheckPath`. A bad deployment is introduced. The operator detects the health gate failure and automatically rolls back to the last known-good spec. Shows the full rollback event in the CRD status.

## What You'll Learn

- How to configure auto-healing in KranixApp
- Health check configuration
- Automatic rollback behavior
- Monitoring rollback events
- Understanding CRD status

## Prerequisites

- [`kranix-operator`](https://github.com/kranix-io/kranix-operator) installed
- [`kranix-core`](https://github.com/kranix-io/kranix-core) for health checks
- kubectl configured
- A Kubernetes cluster

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
- Initial healthy deployment
- Bad deployment introduced
- Health check failure detected
- Automatic rollback triggered
- Rollback event in CRD status

## Cleanup

```bash
make clean
```

## Troubleshooting

- Ensure operator is running
- Check health check endpoint is accessible
- Verify autoHeal is enabled in CRD
- Check operator logs for rollback events
