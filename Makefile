PHONY: format
format:
	ruff format src tests


PHONY: lint
lint:
	ruff check src tests --fix
	mypy src tests
