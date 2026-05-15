# Cluster Health Dashboard

A simple React dashboard that polls `kranix-api` for cluster health, workload statuses, and recent events — rendered in a browser. Shows how to build ops tooling directly on the Kranix API.

## What You'll Learn

- How to build a React dashboard
- Poll kranix-api for cluster data
- Display workload statuses
- Show recent events
- Use TypeScript SDK from kranix-packages

## Prerequisites

- [`kranix-api`](https://github.com/kranix-io/kranix-api) running
- [`kranix-packages`](https://github.com/kranix-io/kranix-packages) TypeScript SDK
- Node.js and npm
- React
- A web browser

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
- Cluster health overview
- Workload status table
- Recent events feed
- Real-time updates
- Responsive UI

## Cleanup

```bash
make clean
```

## Troubleshooting

- Ensure kranix-api is accessible
- Check CORS configuration
- Verify API credentials
- Check browser console for errors
- Ensure React dependencies are installed
