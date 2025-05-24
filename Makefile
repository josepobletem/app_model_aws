install:
	pip install -r docker/requirements.txt
	pip install pytest boto3 pylint

test:
	pytest

lint:
	pylint lambda/*.py sagemaker/*.py ec2/*.py

ci: install test lint
