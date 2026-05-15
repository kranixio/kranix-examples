# Multi Environment Promotion

Three branches (`dev`, `staging`, `main`) each map to a namespace. A GitHub Actions workflow promotes a workload image tag from dev → staging → production using the Kranix API, with a manual approval gate before production.

## What You'll Learn

- Multi-environment GitOps setup
- Branch-to-namespace mapping
- GitHub Actions integration
- Manual approval gates
- Image promotion workflow

## Prerequisites

- [`kranix-operator`](https://github.com/kranix-io/kranix-operator) installed
- [`kranix-api`](https://github.com/kranix-io/kranix-api) running
- GitHub repository with Actions enabled
- Three namespaces: dev, staging, production
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
- Workload deployed to dev
- Promotion to staging
- Manual approval required for production
- Production deployment after approval

## Cleanup

```bash
make clean
```

## Troubleshooting

- Ensure GitHub Actions has access to kranix-api
- Check API credentials are configured
- Verify namespaces exist
- Check workflow logs in GitHub
