import { useEffect, useState } from "react";

type Workload = {
  id: string;
  name: string;
  namespace: string;
  spec?: { image?: string; replicas?: number; backend?: string };
  status?: { phase?: string; readyReplicas?: number };
  labels?: Record<string, string>;
};

const API_PREFIX = "/kranix";

export default function App() {
  const [ns, setNs] = useState("default");
  const [data, setData] = useState<unknown>(null);
  const [err, setErr] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;
    (async () => {
      setErr(null);
      try {
        const r = await fetch(
          `${API_PREFIX}/api/v1/workloads?namespace=${encodeURIComponent(ns)}`
        );
        const j = await r.json();
        if (!r.ok) throw new Error(JSON.stringify(j));
        if (!cancelled) setData(j);
      } catch (e) {
        if (!cancelled) setErr(String(e));
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [ns]);

  const workloads: Workload[] = Array.isArray(data)
    ? (data as Workload[])
    : ((data as { workloads?: Workload[] })?.workloads ?? []);

  return (
    <div style={{ fontFamily: "system-ui", padding: "1.5rem", maxWidth: 960 }}>
      <h1>Kranix workload catalog (preview)</h1>
      <p>
        Mirrors a Backstage plugin page: workloads for a namespace, fed by{" "}
        <code>kranix-api</code>. Dev server proxies <code>/kranix →</code>{" "}
        <code>VITE_KRANIX_PROXY_TARGET</code>.
      </p>
      <label>
        Namespace{" "}
        <input value={ns} onChange={(e) => setNs(e.target.value)} />
      </label>
      {err && <pre style={{ color: "tomato" }}>{err}</pre>}
      <table
        cellPadding={8}
        style={{ borderCollapse: "collapse", marginTop: 16, width: "100%" }}
      >
        <thead>
          <tr style={{ textAlign: "left", borderBottom: "1px solid #ccc" }}>
            <th>ID</th>
            <th>Name</th>
            <th>Phase</th>
            <th>Image</th>
            <th>Labels</th>
          </tr>
        </thead>
        <tbody>
          {workloads.map((w) => (
            <tr key={w.id} style={{ borderBottom: "1px solid #eee" }}>
              <td>{w.id}</td>
              <td>{w.name}</td>
              <td>{w.status?.phase}</td>
              <td>{w.spec?.image}</td>
              <td>
                <small>{JSON.stringify(w.labels ?? {})}</small>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      {workloads.length === 0 && !err && <p>No workloads (deploy via mock or API).</p>}
    </div>
  );
}
