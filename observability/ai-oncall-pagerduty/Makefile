.PHONY: setup run-bridge run-demo verify clean

PYTHON ?= python3
export KRANIX_API_URL ?= http://127.0.0.1:8080
export BRIDGE_ADDR ?= :8090

setup:
	$(PYTHON) -m pip install -r requirements.txt

run-bridge:
	$(PYTHON) src/pagerduty_bridge.py

run-demo:
	$(PYTHON) src/agent_demo.py

verify:
	curl -sf http://127.0.0.1:8090/health || true

clean:
	@echo "No cluster resources for mock demo."
