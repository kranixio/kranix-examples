# IDP self-service portal (internal developer platform)

A minimal **internal developer portal (IDP)** on top of **`kranix-api`**: developers use a browser to **list namespaces**, **deploy** standard workloads from a form, and **inspect** API responses — without `kubectl` or the Kranix CLI.

This is the pattern Backstage, Compass, or an internal Next.js app would follow; here it stays tiny (**Express + static HTML**) so you can read the whole integration in one sitting.

## Architecture

```
Browser  →  Express BFF (`server.mjs`)  →  kranix-api  (/api/v1/*)
         →  static `public/` UI
```

The BFF forwards JSON and adds **`Authorization: Bearer …`** when `KRANIX_API_KEY` is set. Swap the raw `fetch` calls for **[`@kranix-io/sdk`](https://github.com/kranix-io/kranix-packages/tree/main/sdk/typescript)** when you want typed clients from **`kranix-packages`**.

## Prerequisites

- Node.js 18+ (global `fetch`)
- **`kranix-api`** or **`kranix-mock-api`** from [`kranix-packages`](https://github.com/kranix-io/kranix-packages)

## Quick start (mock API)

Terminal 1 — from your local [`kranix-packages`](https://github.com/kranix-io/kranix-packages) clone (any path):

```bash
go run ./cmd/kranix-mock-api -addr :18080 -skip-auth=true
```

Terminal 2:

```bash
cd platform-engineering/self-service-deploy
make setup
export KRANIX_API_URL=http://127.0.0.1:18080
make run
```

Open **http://localhost:3000** — deploy a workload and list workloads in `default`.

## Configuration

| Variable | Description |
|----------|-------------|
| `KRANIX_API_URL` | Base URL of the API (no trailing slash) |
| `KRANIX_API_KEY` | Optional `krane_*` key when auth is enabled |
| `PORT` | Portal listen port (default **3000**) |

## Ecosystem alignment

| Repo | Role |
|------|------|
| [`kranix-api`](https://github.com/kranix-io/kranix-api) | REST: `/api/v1/workloads`, `/api/v1/namespaces`, `/health` |
| [`kranix-packages`](https://github.com/kranix-io/kranix-packages) | **`@kranix-io/sdk`**, `kranix-io-sdk` (Python), shared types |
| [`kranix-web`](https://github.com/kranix-io/kranix-web) | Product docs; this example is self-hosted IDP surface area |
| [`kranix-cli`](https://github.com/kranix-io/kranix-cli) | Alternative UX for the same API |

## Makefile targets

| Target | Action |
|--------|--------|
| `make setup` | `npm install` |
| `make run` | `npm start` |
| `make verify` | HTTP GET to localhost:3000 |
| `make clean` | Remove `node_modules` (optional) |

## Troubleshooting

- **CORS**: the UI talks to **same-origin** `/api/*` only; the BFF calls kranix-api — no browser CORS issues.
- **401 from API**: set `KRANIX_API_KEY` or run **`kranix-mock-api -skip-auth=true`** for local demos.
