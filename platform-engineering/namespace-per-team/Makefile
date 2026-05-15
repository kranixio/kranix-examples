.PHONY: setup run verify clean

setup:
	@echo "Setting up Namespace Per Team example..."
	@echo "Prerequisites: kranix-operator, KranixPolicy CRD, kubectl"

run:
	@echo "Creating namespaces and policies..."
	kubectl apply -f manifests/namespaces.yaml
	kubectl apply -f manifests/policies.yaml

verify:
	@echo "Verifying namespace isolation..."
	kubectl get namespaces
	kubectl get kranixpolicy -A
	kubectl describe kranixpolicy team-a-policy -n team-a

clean:
	@echo "Cleaning up resources..."
	kubectl delete -f manifests/policies.yaml
	kubectl delete -f manifests/namespaces.yaml
