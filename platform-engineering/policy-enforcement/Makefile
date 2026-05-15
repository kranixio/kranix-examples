.PHONY: setup run verify clean

setup:
	@echo "Setting up Policy Enforcement example..."
	@echo "Prerequisites: kranix-operator, kranix-core, kubectl"

run:
	@echo "Creating enforcement policy..."
	kubectl apply -f manifests/policy.yaml
	@echo "Attempting to deploy non-compliant workload..."
	kubectl apply -f manifests/non-compliant-workload.yaml || echo "Expected: Deployment blocked by policy"

verify:
	@echo "Verifying policy violation..."
	kubectl get events --sort-by=.metadata.creationTimestamp | grep PolicyViolation
	kubectl describe kranixapp -n production

clean:
	@echo "Cleaning up resources..."
	kubectl delete -f manifests/non-compliant-workload.yaml --ignore-not-found=true
	kubectl delete -f manifests/policy.yaml
