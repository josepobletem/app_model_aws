import os
import boto3

s3 = boto3.client("s3")
folder = "tests"  # o el path real
bucket = "image-classification-input"

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if os.path.isfile(filepath):
        key = os.path.basename(filepath)
        s3.upload_file(filepath, bucket, key)
