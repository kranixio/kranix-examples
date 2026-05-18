import { defineConfig, loadEnv } from "vite";

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), "");
  const target =
    env.VITE_KRANIX_PROXY_TARGET || "http://127.0.0.1:8080";
  return {
    server: {
      proxy: {
        "/kranix": {
          target,
          changeOrigin: true,
          rewrite: (p) => p.replace(/^\/kranix/, ""),
        },
      },
    },
  };
});
