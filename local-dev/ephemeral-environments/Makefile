.PHONY: setup run verify clean

setup:
	@echo "Setting up Ephemeral Environments example..."
	@echo "Prerequisites: kranix-api, Go, Kubernetes"
	go mod download

run:
	@echo "Creating ephemeral environment..."
	go run scripts/create-env.go --branch $${BRANCH_NAME:-test-branch}
	@echo "Running tests..."
	go run scripts/run-tests.go
	@echo "Tearing down environment..."
	go run scripts/delete-env.go --branch $${BRANCH_NAME:-test-branch}

verify:
	@echo "Verifying environment lifecycle..."
	go run scripts/verify-env.go

clean:
	@echo "Cleaning up any remaining environments..."
	go run scripts/cleanup-all.go
