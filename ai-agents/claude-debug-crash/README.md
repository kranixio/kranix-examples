# Claude Debug Crash

A deliberately broken deployment (bad image tag, OOM config) is handed to Claude. Claude uses `analyze_workload` to identify the crash reason, suggest a fix, and apply a corrected manifest.

## What You'll Learn

- How Claude analyzes failing workloads via kranix-mcp
- Understanding crash analysis outputs
- Applying suggested fixes
- Troubleshooting common deployment issues

## Prerequisites

- [`kranix-mcp`](https://github.com/kranix-io/kranix-mcp) installed and running
- Claude Desktop or Claude API access
- A running `kranix-api` instance
- A Kubernetes cluster

## Setup

```bash
make setup
```

## Running the Example

```bash
make run
```

Then in Claude, ask: "Analyze the failing deployment and suggest a fix"

## Expected Output

Claude should:
- Identify the crash reason (bad image tag or OOM)
- Suggest a corrected configuration
- Apply the fix
- Confirm the deployment is now healthy

## Cleanup

```bash
make clean
```

## Troubleshooting

- Ensure kranix-mcp is running
- Check cluster has sufficient resources for OOM test
- Verify Claude API access if using API instead of Desktop
