.PHONY: setup run seed-overprovisioned clean

PYTHON ?= python3
export KRANIX_API_URL ?= http://127.0.0.1:8080
export RIGHTSIZING_DRY_RUN ?= 0

setup:
	$(PYTHON) -m pip install -r requirements.txt

run:
	$(PYTHON) src/rightsizing_agent.py

seed-overprovisioned:
	@echo "Posting over-provisioned workload to $$KRANIX_API_URL ..."
	@curl -sS -X POST "$${KRANIX_API_URL%/}/api/v1/workloads" \
	  -H 'Content-Type: application/json' \
	  -d '{"name":"cost-demo-fat","namespace":"default","image":"nginx:latest","replicas":2,"backend":"docker","resources":{"cpuRequest":"500m","cpuLimit":"8000m","memoryRequest":"256Mi","memoryLimit":"512Mi"},"labels":{"kranix.io/demo-cpu-utilization":"12"}}' | tee /tmp/kranix-cost-seed.json

clean:
	@echo "No local artifacts."
