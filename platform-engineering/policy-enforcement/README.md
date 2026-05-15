# Policy Enforcement

Demonstrates how `KranixPolicy` blocks a non-compliant workload (missing resource limits, privileged container) and emits a policy violation event — before it ever reaches the runtime.

## What You'll Learn

- How to define enforcement policies
- Block non-compliant workloads
- Understand policy violation events
- Configure resource limits enforcement
- Prevent privileged containers

## Prerequisites

- [`kranix-operator`](https://github.com/kranix-io/kranix-operator) installed
- [`kranix-core`](https://github.com/kranix-io/kranix-core) for policy engine
- KranixPolicy CRD available
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
- Policy created with enforcement rules
- Non-compliant workload rejected
- Policy violation event emitted
- Workload never reaches runtime
- Event logs showing violation details

## Cleanup

```bash
make clean
```

## Troubleshooting

- Ensure operator is running
- Check policy is enforced: `kubectl get kranixpolicy`
- View events: `kubectl get events --sort-by=.metadata.creationTimestamp`
- Verify policy engine is active
