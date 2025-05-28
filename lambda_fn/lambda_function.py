# lambda_fn/lambda_function.py

import json
import os
import boto3

os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'  # o la región que uses

def lambda_handler(event, _context):
    # Crear los clientes dentro de la función para que puedan ser "mockeados"
    s3 = boto3.client('s3')
    sagemaker = boto3.client('sagemaker-runtime')

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

    return {"statusCode": 200, "body": prediction}

