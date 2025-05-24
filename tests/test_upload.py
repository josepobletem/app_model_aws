from moto import mock_aws
import boto3
import tempfile
import os

@mock_s3
def test_upload_image_script_import():
    bucket_name = "image-classification-input"
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket=bucket_name)

    # Crear archivo temporal
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b"dummy image content")
        filename = tmp.name

    # Crear clave válida
    key = os.path.basename(filename)

    # Este código simula lo que haría upload_images.py
    s3.upload_file(filename, bucket_name, key)

    # Importa tu script después del setup
    import ec2.upload_images

    os.remove(filename)  # limpiar
