# Namespace Per Team

Three teams, three namespaces, one cluster. Each namespace has a `KranixPolicy` enforcing CPU/memory limits, network isolation, and image pull restrictions. Shows how platform teams can define policy once and apply it consistently.

## What You'll Learn

- How to create isolated namespaces per team
- Define KranixPolicy for resource limits
- Configure network isolation
- Set image pull restrictions
- Apply policies consistently across teams

## Prerequisites

- [`kranix-operator`](https://github.com/kranix-io/kranix-operator) installed
- KranixPolicy CRD available
- KranixNamespace CRD available
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
- Three namespaces created (team-a, team-b, team-c)
- KranixPolicy applied to each namespace
- Resource limits enforced
- Network policies configured
- Image restrictions in place

## Cleanup

```bash
make clean
```

## Troubleshooting

- Ensure operator is running
- Check CRDs are registered
- Verify policies are applied: `kubectl get kranixpolicy`
- Check namespace status
