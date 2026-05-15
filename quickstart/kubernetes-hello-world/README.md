# Kubernetes Hello World

Deploy a workload to a local Kubernetes cluster (`kind`). Covers namespace creation, deployment, and log streaming via the CLI.

## What You'll Learn

- How to deploy to Kubernetes using kranix-cli
- Create and manage namespaces
- Stream logs from Kubernetes pods
- Clean up Kubernetes resources

## Prerequisites

- [`kranix-cli`](https://github.com/kranix-io/kranix-cli) installed
- `kind` installed (`brew install kind` or equivalent)
- A running `kranix-api` instance
- kubectl configured

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
- Kind cluster created
- Namespace created
- Workload deployed
- Pods running
- Logs streaming

## Cleanup

```bash
make clean
```

## Troubleshooting

- Ensure kind is installed and working
- Check kranix-api is running
- Verify kubectl context is correct
