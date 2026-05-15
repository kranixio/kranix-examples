.PHONY: setup run verify clean

setup:
	@echo "Setting up Multi Environment Promotion example..."
	@echo "Prerequisites: kranix-operator, kranix-api, GitHub, kubectl"
	kubectl create namespace dev
	kubectl create namespace staging
	kubectl create namespace production

run:
	@echo "Deploying to dev environment..."
	kubectl apply -f manifests/dev-kranixapp.yaml
	@echo "To promote: push to staging branch, then main branch with approval"

verify:
	@echo "Verifying deployments..."
	kubectl get kranixapp -n dev
	kubectl get kranixapp -n staging
	kubectl get kranixapp -n production

clean:
	@echo "Cleaning up resources..."
	kubectl delete namespace dev staging production
