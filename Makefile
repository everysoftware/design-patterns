PHONY: format
format:
	ruff format patterns tests


PHONY: lint
lint:
	ruff check patterns tests --fix
	mypy patterns tests --ignore-missing-imports
