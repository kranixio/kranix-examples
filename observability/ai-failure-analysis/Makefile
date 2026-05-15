.PHONY: setup run verify clean

setup:
	@echo "Setting up AI Failure Analysis example..."
	@echo "Prerequisites: kranix-cli, kranix-api, kranix-core, kubectl"

run:
	@echo "Deploying OOM scenario..."
	kubectl apply -f manifests/oom-scenario.yaml
	@echo "Running kranix analyze..."
	kranix analyze pod/oom-pod -n production
	@echo "Deploying CrashLoopBackOff scenario..."
	kubectl apply -f manifests/crashloop-scenario.yaml
	kranix analyze pod/crashloop-pod -n production
	@echo "Deploying missing ConfigMap scenario..."
	kubectl apply -f manifests/missing-configmap-scenario.yaml
	kranix analyze pod/missing-config-pod -n production

verify:
	@echo "Verifying analysis results..."
	kranix analyze pod/oom-pod -n production --output json

clean:
	@echo "Cleaning up resources..."
	kubectl delete -f manifests/oom-scenario.yaml --ignore-not-found=true
	kubectl delete -f manifests/crashloop-scenario.yaml --ignore-not-found=true
	kubectl delete -f manifests/missing-configmap-scenario.yaml --ignore-not-found=true
