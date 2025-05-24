install:
	pip install -r docker/requirements.txt
	pip install pytest boto3 pylint

test:
	pytest

lint:
	pylint lambda/*.py sagemaker/*.py ec2/*.py

ci: install test lint


PYTHON = .venv/bin/python
PIP = .venv/bin/pip
PYLINT = .venv/bin/pylint
PYTEST = .venv/bin/pytest

export PYTHONPATH := $(shell pwd)

.venv:
	python3 -m venv .venv
	$(PIP) install -r docker/requirements.txt

install: .venv
	$(PIP) install -r docker/requirements.txt

test:
	$(PYTEST) tests/

lint:
	$(PYLINT) ec2/*.py lambda_fn/*.py trainer/*.py

ci: install test lint
