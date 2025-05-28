import os
import boto3

s3 = boto3.client("s3")
FOLDER = "tests"  # o el path real
BUCKET = "image-classification-input"

for filename in os.listdir(FOLDER):
    filepath = os.path.join(FOLDER, filename)
    if os.path.isfile(filepath):
        key = os.path.basename(filepath)
        s3.upload_file(filepath, BUCKET, key)
