.PHONY: setup run verify clean

setup:
	@echo "Setting up Docker Compose Stack example..."
	@echo "Prerequisites: kranix-runtime, kranix-cli, Docker, Docker Compose"

run:
	@echo "Deploying Compose stack..."
	kranix compose up -f manifests/docker-compose.yaml
	@echo "Waiting for services to be healthy..."
	sleep 10

verify:
	@echo "Verifying stack status..."
	kranix compose ps
	@echo "Checking logs..."
	kranix logs --tail=20

clean:
	@echo "Tearing down Compose stack..."
	kranix compose down -f manifests/docker-compose.yaml
