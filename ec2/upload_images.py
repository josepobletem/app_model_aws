import boto3
import sys
import os

s3 = boto3.client('s3')
bucket = 'image-classification-input'

filename = sys.argv[1]
key = key = os.path.basename(filename) or "default.jpg"

s3.upload_file(filename, bucket, key)
print(f"Imagen {key} subida a {bucket}")
