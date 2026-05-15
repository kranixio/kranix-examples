# Single App GitOps

A single `KranixApp` manifest committed to a Git repo. The Kranix operator watches the CRD and reconciles on every commit. Demonstrates the full GitOps loop: commit → operator detects change → runtime applies → status updated.

## What You'll Learn

- How to create a KranixApp CRD
- GitOps workflow with Kranix operator
- Operator reconciliation behavior
- Status updates in CRD

## Prerequisites

- [`kranix-operator`](https://github.com/kranix-io/kranix-operator) installed
- [`kranix-charts`](https://github.com/kranix-io/kranix-charts) installed
- `kind` for local Kubernetes cluster
- kubectl configured
- Git repository

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
- KranixApp CRD created
- Operator detects the change
- Workload deployed
- Status updated in CRD

## Cleanup

```bash
make clean
```

## Troubleshooting

- Ensure operator is running: `kubectl get pods -n kranix-system`
- Check CRD is registered: `kubectl get crd kranixapps.kranix.io`
- Verify kubectl context is correct
