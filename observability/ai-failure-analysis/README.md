# AI Failure Analysis

A simulated crash scenario (OOMKilled, CrashLoopBackOff, missing ConfigMap). Runs `kranix analyze` against each and shows the structured output: crash reason, probable fix, resource recommendation, and generated patch.

## What You'll Learn

- How to use kranix analyze for failure analysis
- Understand different crash scenarios
- Interpret structured analysis output
- Apply suggested fixes
- Resource recommendations

## Prerequisites

- [`kranix-cli`](https://github.com/kranix-io/kranix-cli) installed
- [`kranix-api`](https://github.com/kranix-io/kranix-api) running
- [`kranix-core`](https://github.com/kranix-io/kranix-core) for analysis
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

For each crash scenario, you should see:
- Crash reason identified
- Probable fix suggested
- Resource recommendations
- Generated patch YAML
- Confidence score

## Cleanup

```bash
make clean
```

## Troubleshooting

- Ensure kranix-api is running
- Check kranix-cli is configured
- Verify cluster has resources for OOM test
- Check analysis engine is active
