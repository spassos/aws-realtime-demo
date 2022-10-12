clean:
	rm -rf .venv *.checkpoint .pytest_cache .coverage

init: clean
	pip install poetry
	poetry install
