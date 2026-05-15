# Local Kubernetes Cluster

Full local Kranix setup on a `kind` cluster — installs `kranix-charts`, verifies operator health, creates a test namespace, and deploys a sample app. The recommended starting point before any cloud deployment.

## What You'll Learn

- How to create a local kind cluster
- Install kranix-charts via Helm
- Verify operator health
- Create test namespaces
- Deploy sample applications
- Full local development workflow

## Prerequisites

- `kind` installed (`brew install kind` or equivalent)
- `helm` installed (`brew install helm` or equivalent)
- [`kranix-cli`](https://github.com/kranix-io/kranix-cli) installed
- [`kranix-charts`](https://github.com/kranix-io/kranix-charts)
- Docker Desktop running
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
- Kranix charts installed
- Operator pods running
- Test namespace created
- Sample app deployed
- Health checks passing

## Cleanup

```bash
make clean
```

## Troubleshooting

- Ensure Docker daemon is running
- Check kind cluster status: `kind get clusters`
- Verify Helm chart installation: `helm list -n kranix-system`
- Check operator logs: `kubectl logs -n kranix-system -l app=kranix-operator`
