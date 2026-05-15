.PHONY: setup run verify clean

setup:
	@echo "Setting up Single App GitOps example..."
	@echo "Prerequisites: kranix-operator, kranix-charts, kind, kubectl"

run:
	@echo "Creating KranixApp CRD..."
	kubectl apply -f manifests/kranixapp.yaml

verify:
	@echo "Verifying GitOps reconciliation..."
	kubectl get kranixapp -n production
	kubectl describe kranixapp api-server -n production

clean:
	@echo "Cleaning up resources..."
	kubectl delete -f manifests/kranixapp.yaml
