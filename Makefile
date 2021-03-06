.PHONY: setup \
		run \
		test \

PIP_VERSION = 21.2.4
FILE_TO_BLACK = .

virtual_env: ## Alias for virtual environment
	python -m venv ve

setup: virtual_env ## Project setup
	. ve/bin/activate; pip install pip==${PIP_VERSION} wheel setuptools
	. ve/bin/activate; pip install --exists-action w -Ur requirements/dev.txt
	. ve/bin/activate; pre-commit install

run: virtual_env ## Run project
	. ve/bin/activate; python main.py


# Testing commands
test: virtual_env  ## Run tests
	. ve/bin/activate; python -m pytest -v

coverage: virtual_env  ## Run tests with coverage - load config from tests/config.yaml
	. ve/bin/activate; pip install --exists-action w -Ur requirements/dev.txt
	. ve/bin/activate; python -m pytest -vv --cov=directions tests/ --no-cov-on-fail --tb=no tests/

# Code style
lint: virtual_env ## Run linter (flake8)
	. ve/bin/activate; flake8

mypy: virtual_env ## Run mypy
	. ve/bin/activate; mypy ./directions

black: virtual_env ## Run isort and black
	. ve/bin/activate; isort $(FILE_TO_BLACK); black $(FILE_TO_BLACK)

# Clean commands
clean: clean-build clean-pyc clean-test ## Remove all build, test, coverage and Python artifacts
clean-build: ## Remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
clean-pyc: ## Remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
clean-test: ## Remove test and coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/
