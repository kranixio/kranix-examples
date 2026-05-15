# Custom MCP Agent

A minimal Python script that implements an MCP client and connects to `kranix-mcp`. Shows the raw MCP protocol flow — tool discovery, tool call, result handling — without relying on Claude or GPT.

## What You'll Learn

- How to implement an MCP client in Python
- Understand the MCP protocol flow
- Tool discovery and invocation
- Result handling and parsing

## Prerequisites

- [`kranix-mcp`](https://github.com/kranix-io/kranix-mcp) installed and running
- Python 3.8 or later
- Python MCP client library
- A running `kranix-api` instance

## Setup

```bash
make setup
```

## Running the Example

```bash
make run
```

## Expected Output

The script should:
- Connect to kranix-mcp
- Discover available tools
- Call a tool (e.g., list_namespaces)
- Display the result
- Handle errors gracefully

## Cleanup

```bash
make clean
```

## Troubleshooting

- Ensure kranix-mcp is running
- Check Python dependencies are installed
- Verify MCP server endpoint is accessible
