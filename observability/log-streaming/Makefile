.PHONY: setup run verify clean

setup:
	@echo "Setting up Log Streaming example..."
	@echo "Prerequisites: kranix-cli, kranix-api, kubectl"

run:
	@echo "Deploying multi-replica workload..."
	kubectl apply -f manifests/workload.yaml
	@echo "Streaming logs via CLI..."
	kranix logs deployment/api-server -n production --follow &
	@echo "Streaming logs via SSE endpoint..."
	curl -N http://localhost:8080/api/v1/pods/api-server-*/logs

verify:
	@echo "Verifying log streaming..."
	kubectl get pods -n production
	kranix logs deployment/api-server -n production --tail=10

clean:
	@echo "Cleaning up resources..."
	kubectl delete -f manifests/workload.yaml
	pkill -f "kranix logs" || true
