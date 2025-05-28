# pylint: disable=unused-import, import-outside-toplevel

import os
import tempfile

import boto3
from moto import mock_s3


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
    key = os.path.basename(filename) or "dummy.jpg"

    # Simular lo que haría el script real
    s3.upload_file(filename, bucket_name, key)

    # Forzar la importación para asegurar que no falla
    import ec2.upload_images  # noqa: F401

    os.remove(filename)  # limpiar
