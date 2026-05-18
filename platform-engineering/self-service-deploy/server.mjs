/**
 * Minimal IDP-style portal: static UI + BFF that proxies to kranix-api.
 * Set KRANIX_API_URL (and KRANIX_API_KEY for authenticated APIs).
 */
import express from "express";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const app = express();
const PORT = Number(process.env.PORT || 3000);
const BASE = (process.env.KRANIX_API_URL || "http://127.0.0.1:8080").replace(/\/$/, "");
const API_KEY = process.env.KRANIX_API_KEY || "";

function apiHeaders(json = false) {
  const h = { Accept: "application/json" };
  if (API_KEY) h.Authorization = `Bearer ${API_KEY}`;
  if (json) h["Content-Type"] = "application/json";
  return h;
}

app.use(express.json({ limit: "1mb" }));
app.use(express.static(path.join(__dirname, "public")));

app.get("/api/health", async (_req, res) => {
  try {
    const r = await fetch(`${BASE}/health`);
    const t = await r.text();
    res.status(r.status).type("application/json").send(t || "{}");
  } catch (e) {
    res.status(502).json({ error: String(e) });
  }
});

app.get("/api/namespaces", async (_req, res) => {
  try {
    const r = await fetch(`${BASE}/api/v1/namespaces`, { headers: apiHeaders() });
    const j = await r.json();
    res.status(r.status).json(j);
  } catch (e) {
    res.status(502).json({ error: String(e) });
  }
});

app.get("/api/workloads", async (req, res) => {
  const ns = req.query.namespace ? `?namespace=${encodeURIComponent(req.query.namespace)}` : "";
  try {
    const r = await fetch(`${BASE}/api/v1/workloads${ns}`, { headers: apiHeaders() });
    const j = await r.json();
    res.status(r.status).json(j);
  } catch (e) {
    res.status(502).json({ error: String(e) });
  }
});

app.post("/api/deploy", async (req, res) => {
  try {
    const r = await fetch(`${BASE}/api/v1/workloads`, {
      method: "POST",
      headers: apiHeaders(true),
      body: JSON.stringify(req.body),
    });
    const j = await r.json().catch(() => ({}));
    res.status(r.status).json(j);
  } catch (e) {
    res.status(502).json({ error: String(e) });
  }
});

app.listen(PORT, () => {
  console.error(`IDP portal listening on http://localhost:${PORT}`);
  console.error(`Proxying kranix-api at ${BASE}`);
});
