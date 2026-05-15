# Docker Hello World

Deploy your first container using `kranix-cli`. No Kubernetes required. Shows the full deploy → status → logs → teardown loop in under 5 minutes.

## What You'll Learn

- How to use kranix-cli to deploy a container
- Check deployment status
- Stream logs from the container
- Clean up resources

## Prerequisites

- [`kranix-cli`](https://github.com/kranix-io/kranix-cli) installed
- Docker Desktop or a Docker daemon running
- A running `kranix-runtime` (Docker backend)

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
- Container deployed successfully
- Status showing as "Running"
- Logs displaying the hello world message

## Cleanup

```bash
make clean
```

## Troubleshooting

- Ensure Docker daemon is running
- Check that kranix-runtime is accessible
- Verify kranix-cli is properly configured
