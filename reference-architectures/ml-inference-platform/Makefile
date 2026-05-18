.PHONY: setup setup-k8s run-local run-k8s verify verify-k8s clean clean-k8s

PYTHON ?= python3
export KRANIX_API_URL ?= http://127.0.0.1:8080

setup:
	@echo "Python deps for local agent..."
	$(PYTHON) -m pip install -r requirements.txt

setup-k8s:
	@echo "Optional: install KServe / GPU operators (customize scripts/* for your org)"
	test -f scripts/setup-gpu-cluster.sh && ./scripts/setup-gpu-cluster.sh || true

run-local:
	$(PYTHON) src/latency_agent.py

run-k8s:
	@echo "Deploying to Kubernetes (requires kubectl + manifests)..."
	kubectl apply -f manifests/namespaces.yaml 2>/dev/null || true
	kubectl apply -f manifests/model-server.yaml 2>/dev/null || true
	kubectl apply -f manifests/rollout-policy.yaml 2>/dev/null || true
	./scripts/start-monitoring-agent.sh 2>/dev/null || $(PYTHON) src/latency_agent.py

verify:
	@echo "With mock API, inspect stdout from run-local. With k8s:"
	@$(MAKE) verify-k8s || true

verify-k8s:
	kubectl get pods -n inference 2>/dev/null || true
	./scripts/test-inference.sh 2>/dev/null || true

clean:
	@echo "No resources for pure local mock path."

clean-k8s:
	kubectl delete -f manifests/rollout-policy.yaml 2>/dev/null || true
	kubectl delete -f manifests/model-server.yaml 2>/dev/null || true
	kubectl delete -f manifests/namespaces.yaml 2>/dev/null || true
