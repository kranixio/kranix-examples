.PHONY: setup run verify clean

setup:
	@test -f scripts/failover-drill.sh && chmod +x scripts/failover-drill.sh || true

run:
	@./scripts/failover-drill.sh

verify:
	@curl -sf "$${KRANIX_API_URL:-http://127.0.0.1:8080}/health" && echo OK

clean:
	@echo "No resources."
