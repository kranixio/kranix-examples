.PHONY: setup run verify clean

setup:
	@echo "Setting up Self Service Deploy example..."
	@echo "Prerequisites: kranix-api, Node.js, npm"
	npm install

run:
	@echo "Starting developer portal..."
	npm start

verify:
	@echo "Verifying portal is running..."
	curl http://localhost:3000

clean:
	@echo "Cleaning up resources..."
	# Stop the portal if running
	pkill -f "npm start" || true
