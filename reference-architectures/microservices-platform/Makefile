.PHONY: setup run verify clean

setup:
	@echo "Setting up Microservices Platform example..."
	@echo "Prerequisites: kranix-core, kranix-api, kranix-mcp, kranix-operator, kranix-charts, GitHub Actions"
	./scripts/setup-cluster.sh
	./scripts/install-kranix.sh

run:
	@echo "Deploying microservices..."
	kubectl apply -f manifests/namespaces.yaml
	kubectl apply -f manifests/policies.yaml
	kubectl apply -f manifests/microservices/
	@echo "Starting MCP server..."
	./scripts/start-mcp.sh

verify:
	@echo "Verifying platform..."
	kubectl get pods -A
	kubectl get kranixapp -A
	kubectl get kranixpolicy -A
	./scripts/verify-health.sh

clean:
	@echo "Cleaning up platform..."
	kubectl delete -f manifests/microservices/
	kubectl delete -f manifests/policies.yaml
	kubectl delete -f manifests/namespaces.yaml
	./scripts/teardown-cluster.sh
