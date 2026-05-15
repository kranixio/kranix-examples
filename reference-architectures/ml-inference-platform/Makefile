.PHONY: setup run verify clean

setup:
	@echo "Setting up ML Inference Platform example..."
	@echo "Prerequisites: kranix-core, kranix-mcp, kranix-operator, KServe, GPU cluster"
	./scripts/setup-gpu-cluster.sh
	./scripts/install-kserve.sh
	./scripts/install-kranix.sh

run:
	@echo "Deploying model server..."
	kubectl apply -f manifests/namespaces.yaml
	kubectl apply -f manifests/model-server.yaml
	@echo "Configuring health-gated rollout..."
	kubectl apply -f manifests/rollout-policy.yaml
	@echo "Starting AI agent for monitoring..."
	./scripts/start-monitoring-agent.sh

verify:
	@echo "Verifying inference platform..."
	kubectl get pods -n inference
	kubectl get inferenceservice -n inference
	./scripts/test-inference.sh
	./scripts/check-latency.sh

clean:
	@echo "Cleaning up platform..."
	kubectl delete -f manifests/rollout-policy.yaml
	kubectl delete -f manifests/model-server.yaml
	kubectl delete -f manifests/namespaces.yaml
	./scripts/teardown-kserve.sh
