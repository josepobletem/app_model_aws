PYTHON = .venv/bin/python
PIP = .venv/bin/pip
PYLINT = .venv/bin/pylint
PYTEST = .venv/bin/pytest

export PYTHONPATH := $(shell pwd)

.venv:
	python3 -m venv .venv
	$(PIP) install -r docker/requirements.txt
	$(PIP) install pytest boto3 pylint

install: .venv

test:
	PYTHONPATH=. $(PYTEST)

lint:
	$(PYLINT) ec2/*.py lambda_fn/*.py trainer/*.py tests/*.py

train:
	$(PYTHON) trainer/train.py

ci: install test lint train
