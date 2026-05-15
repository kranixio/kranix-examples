.PHONY: setup run verify clean

setup:
	@echo "Setting up Local Kubernetes Cluster example..."
	@echo "Prerequisites: kind, helm, kranix-cli, Docker, kubectl"
	kind create cluster --name kranix-local
	helm repo add kranix https://charts.kranix.io
	helm repo update

run:
	@echo "Installing kranix-charts..."
	helm install kranix kranix/kranix -n kranix-system --create-namespace
	@echo "Waiting for operator to be ready..."
	kubectl wait --for=condition=available --timeout=300s deployment/kranix-operator -n kranix-system
	@echo "Creating test namespace..."
	kubectl create namespace test
	@echo "Deploying sample app..."
	kubectl apply -f manifests/sample-app.yaml

verify:
	@echo "Verifying installation..."
	kubectl get pods -n kranix-system
	kubectl get pods -n test
	kubectl get kranixapp -n test

clean:
	@echo "Cleaning up resources..."
	kubectl delete namespace test
	helm uninstall kranix -n kranix-system
	kind delete cluster --name kranix-local
