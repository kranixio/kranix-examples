# Backstage — Kranix workload catalog

Integrate **Kranix** into **[Backstage](https://backstage.io)** so developers see **live workloads** (from **`kranix-api`**) next to catalog components.

This folder provides:

1. **`config/`** — `app-config` snippets: **proxy** to `kranix-api` and optional **annotations** on catalog entities.
2. **`preview-ui/`** — a tiny **Vite + React** app that matches what a Backstage plugin page would render; builds without a full Backstage monorepo. Copy the fetch logic into a real `@backstage/plugin-kranix-workloads` package when you are ready.

## Ecosystem alignment

| Repo | Role |
|------|------|
| [`kranix-api`](https://github.com/kranix-io/kranix-api) | `GET /api/v1/workloads`, `GET /api/v1/namespaces` |
| [`kranix-packages`](https://github.com/kranix-io/kranix-packages) | Optional **`@kranix-io/sdk`** instead of raw `fetch` |
| [`kranix-web`](https://github.com/kranix-io/kranix-web) | Public docs linking from your service catalog |
| **Backstage** | Catalog, auth, and organizational context |

## 1. Proxy `kranix-api` in Backstage

Merge **`config/backstage-proxy-snippet.yaml`** into your `app-config.yaml` so the browser calls same-origin `/api/proxy/kranix/...` (Backstage injects auth cookies / OIDC).

## 2. Link catalog entities to Kranix

Use annotations (example):

```yaml
metadata:
  annotations:
    kranix.io/namespace: team-payments
    kranix.io/workload-selector: app=payments-api
```

Your plugin reads annotations and filters **`/api/v1/workloads?namespace=...`**.

## 3. Build the preview UI (optional)

```bash
cd preview-ui
npm install
npm run build
```

Set **`VITE_KRANIX_PROXY_TARGET`** when using `vite dev` (defaults to `http://127.0.0.1:18080` for **`kranix-mock-api`**).

## Production notes

- Lock **`kranix-api`** to SSO / service accounts; do not expose cluster-admin keys to the browser — use Backstage backend plugin with a **backend-to-kranix** token.
- Map **Backstage owner** to **Kranix namespace** via `catalog-model` annotations.

## Makefile (repo root for this example)

```bash
make setup   # cd preview-ui && npm install
make build   # cd preview-ui && npm run build
```
