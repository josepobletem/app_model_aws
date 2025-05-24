import boto3
import sys

s3 = boto3.client('s3')
bucket = 'image-classification-input'

filename = sys.argv[1]
key = filename.split("/")[-1]

s3.upload_file(filename, bucket, key)
print(f"Imagen {key} subida a {bucket}")
