.PHONY: setup run verify clean

setup:
	npm install

run:
	npm start

verify:
	curl -sf http://localhost:3000/ >/dev/null && echo OK

clean:
	rm -rf node_modules
