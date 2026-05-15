# Self Service Deploy

A minimal internal developer portal (HTML + JS) that calls `kranix-api` directly, allowing developers to deploy pre-approved workloads to their own namespace without needing `kubectl` or CLI access.

## What You'll Learn

- How to build a simple developer portal
- Call kranix-api from web applications
- Implement self-service deployment
- Use TypeScript SDK from kranix-packages
- Manage authentication and authorization

## Prerequisites

- [`kranix-api`](https://github.com/kranix-io/kranix-api) running
- [`kranix-packages`](https://github.com/kranix-io/kranix-packages) TypeScript SDK
- Node.js and npm
- A web browser
- Pre-approved workload templates

## Setup

```bash
make setup
```

## Running the Example

```bash
make run
```

Then open `http://localhost:3000` in your browser.

## Expected Output

You should see:
- Developer portal UI
- Form to select workload template
- Deployment status updates
- Log streaming interface

## Cleanup

```bash
make clean
```

## Troubleshooting

- Ensure kranix-api is accessible
- Check CORS configuration on API
- Verify API credentials are set
- Check browser console for errors
