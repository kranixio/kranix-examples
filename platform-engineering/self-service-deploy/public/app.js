async function j(url, opts = {}) {
  const r = await fetch(url, opts);
  const t = await r.text();
  let body;
  try {
    body = JSON.parse(t);
  } catch {
    body = t;
  }
  if (!r.ok) throw new Error(`${r.status} ${typeof body === "string" ? body : JSON.stringify(body)}`);
  return body;
}

async function loadNamespaces() {
  const out = document.getElementById("namespaces-out");
  out.textContent = "Loading…";
  try {
    const data = await j("/api/namespaces");
    out.textContent = JSON.stringify(data, null, 2);
  } catch (e) {
    out.textContent = String(e);
  }
}

document.getElementById("refresh-ns").addEventListener("click", loadNamespaces);

document.getElementById("deploy-form").addEventListener("submit", async (ev) => {
  ev.preventDefault();
  const out = document.getElementById("deploy-out");
  const fd = new FormData(ev.target);
  const spec = {
    name: fd.get("name"),
    namespace: fd.get("namespace"),
    image: fd.get("image"),
    replicas: Number(fd.get("replicas")),
    backend: fd.get("backend") || "docker",
  };
  out.textContent = "Deploying…";
  try {
    const data = await j("/api/deploy", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(spec),
    });
    out.textContent = JSON.stringify(data, null, 2);
  } catch (e) {
    out.textContent = String(e);
  }
});

document.getElementById("list-wl").addEventListener("click", async () => {
  const out = document.getElementById("workloads-out");
  const ns = document.getElementById("list-namespace").value || "";
  out.textContent = "Loading…";
  try {
    const q = ns ? `?namespace=${encodeURIComponent(ns)}` : "";
    const data = await j(`/api/workloads${q}`);
    out.textContent = JSON.stringify(data, null, 2);
  } catch (e) {
    out.textContent = String(e);
  }
});

loadNamespaces();
