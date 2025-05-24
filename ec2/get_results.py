import boto3

s3 = boto3.client('s3')
bucket = 'image-classification-results'

response = s3.list_objects_v2(Bucket=bucket)
for obj in response.get('Contents', []):
    body = s3.get_object(Bucket=bucket, Key=obj['Key'])['Body'].read().decode()
    print(f"{obj['Key']}: {body}")
