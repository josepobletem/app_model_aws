import boto3

bucket = 'image-classification-results'

def list_my_objects():
    s3 = boto3.client("s3")
    return s3.list_objects_v2(...)

for obj in list_my_objects()['Contents']:
    print(obj['Key']).get('Contents', [])
    body = s3.get_object(Bucket=bucket, Key=obj['Key'])['Body'].read().decode()
    print(f"{obj['Key']}: {body}")
