PYTHON = .venv/bin/python
PIP = .venv/bin/pip
PYLINT = .venv/bin/pylint
PYTEST = .venv/bin/pytest

export PYTHONPATH := $(shell pwd)

.venv:
	python3 -m venv .venv
	$(PIP) install --upgrade pip

install: .venv
	$(PIP) install -r requirements.txt

test:
	$(PYTEST) tests/

lint:
	$(PYLINT) ec2/*.py lambda_fn/*.py trainer/*.py

ci: install test lint
