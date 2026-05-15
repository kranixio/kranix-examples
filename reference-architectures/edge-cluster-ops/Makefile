.PHONY: setup run verify clean

setup:
	@echo "Setting up Edge Cluster Ops example..."
	@echo "Prerequisites: kranix-core, kranix-runtime, kranix-mcp, kranix-api, central cluster, edge nodes"
	./scripts/setup-control-plane.sh
	./scripts/register-edge-nodes.sh

run:
	@echo "Labeling edge nodes..."
	kubectl label node edge-1 location=edge zone=zone-a
	kubectl label node edge-2 location=edge zone=zone-b
	kubectl label node edge-3 location=edge zone=zone-c
	@echo "Deploying workloads with node selectors..."
	kubectl apply -f manifests/namespaces.yaml
	kubectl apply -f manifests/edge-workloads.yaml
	@echo "Starting MCP agent for monitoring..."
	./scripts/start-edge-agent.sh

verify:
	@echo "Verifying edge cluster..."
	kubectl get nodes -L location,zone
	kubectl get pods -n edge-workloads -o wide
	./scripts/check-node-health.sh
	./scripts/test-redistribution.sh

clean:
	@echo "Cleaning up edge cluster..."
	kubectl delete -f manifests/edge-workloads.yaml
	kubectl delete -f manifests/namespaces.yaml
	./scripts/unregister-edge-nodes.sh
	./scripts/teardown-control-plane.sh
