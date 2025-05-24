import os
import boto3
import json

os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'  # o la región que uses
sagemaker = boto3.client('sagemaker-runtime')

sagemaker = boto3.client('sagemaker-runtime')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    image = s3.get_object(Bucket=bucket, Key=key)['Body'].read()

    response = sagemaker.invoke_endpoint(
        EndpointName='image-classifier-endpoint',
        ContentType='application/x-image',
        Body=image
    )

    prediction = response['Body'].read().decode()

    s3.put_object(
        Bucket='image-classification-results',
        Key=f"{key}.json",
        Body=json.dumps({'prediction': prediction})
    )

    return {"statusCode": 200, "body":  prediction}
