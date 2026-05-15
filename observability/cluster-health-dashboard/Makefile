.PHONY: setup run verify clean

setup:
	@echo "Setting up Cluster Health Dashboard example..."
	@echo "Prerequisites: kranix-api, Node.js, npm, React"
	npm install

run:
	@echo "Starting React dashboard..."
	npm start

verify:
	@echo "Verifying dashboard is running..."
	curl http://localhost:3000

clean:
	@echo "Cleaning up resources..."
	pkill -f "npm start" || true
