import boto3

bucket = 'image-classification-results'  # Asegurate de usar este nombre en el test

def list_my_objects():
    s3 = boto3.client("s3")
    return s3.list_objects_v2(Bucket=bucket)

# Esta parte se ejecuta al importar el script
response = list_my_objects()

if 'Contents' in response:
    for obj in response['Contents']:
        print("Archivo en el bucket:", obj['Key'])
else:
    print("El bucket está vacío o no existe.")
