format:
	black ./src
	isort ./src

test:
	cd src/
	pytest .
