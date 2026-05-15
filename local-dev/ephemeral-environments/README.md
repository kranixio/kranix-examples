# Ephemeral Environments

Creates a fresh namespace + workload on demand (e.g. per Git branch or PR), runs a test suite against it, then tears the whole environment down. Shows how to use the Kranix API in CI for ephemeral test environments.

## What You'll Learn

- How to create ephemeral environments
- Integrate with CI/CD pipelines
- Run tests against ephemeral envs
- Automatic cleanup after tests
- Use kranix-api in CI workflows

## Prerequisites

- [`kranix-api`](https://github.com/kranix-io/kranix-api) running
- [`kranix-packages`](https://github.com/kranix-io/kranix-packages) Go SDK
- Go installed
- A Kubernetes cluster
- CI system (GitHub Actions, GitLab CI, etc.)

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
- Ephemeral namespace created
- Workload deployed
- Tests executed
- Test results displayed
- Environment torn down

## Cleanup

```bash
make clean
```

## Troubleshooting

- Ensure kranix-api is accessible
- Check API credentials in CI
- Verify cluster has capacity
- Check test suite configuration
- Ensure cleanup runs even on failure
