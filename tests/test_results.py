from moto import mock_s3
import boto3

@mock_s3
def test_get_results_script_import():
    bucket_name = "image-classification-results"  # Debe coincidir con el script
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket=bucket_name)

    s3.put_object(Bucket=bucket_name, Key="test.txt", Body=b"hello")
