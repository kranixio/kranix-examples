.PHONY: setup run verify clean

setup:
	@echo "Setting up Auto Rollback example..."
	@echo "Prerequisites: kranix-operator, kranix-core, kubectl"

run:
	@echo "Deploying healthy version..."
	kubectl apply -f manifests/healthy-kranixapp.yaml
	@echo "Wait for deployment to be healthy..."
	sleep 30
	@echo "Deploying bad version to trigger rollback..."
	kubectl apply -f manifests/bad-kranixapp.yaml

verify:
	@echo "Verifying rollback occurred..."
	kubectl get kranixapp -n production
	kubectl describe kranixapp api-server -n production | grep -A 10 Rollback

clean:
	@echo "Cleaning up resources..."
	kubectl delete -f manifests/healthy-kranixapp.yaml
	kubectl delete -f manifests/bad-kranixapp.yaml
