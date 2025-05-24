from moto.s3 import mock_s3
import boto3
import pytest

@mock_s3
def test_get_results_script_import():
    bucket_name = "my-test-bucket"
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket=bucket_name)

    s3.put_object(Bucket=bucket_name, Key="test.txt", Body=b"hello")

    # Simula la importación del script (después de crear recursos)
    import ec2.get_results
