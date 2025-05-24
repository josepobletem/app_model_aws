# Image Classifier with AWS EC2, S3, Lambda & SageMaker

Este proyecto implementa un sistema de clasificación de imágenes utilizando servicios de AWS.

## Arquitectura

- **S3**: almacenamiento de imágenes y resultados
- **Lambda**: ejecución automática al subir imagen
- **SageMaker**: entrenamiento y despliegue del modelo
- **EC2**: scripts para interacción manual
- **Docker**: ejecución y pruebas locales

## Pasos para desplegar

### 1. Entrenar y desplegar el modelo con SageMaker

```bash
cd sagemaker
python deploy.py
```

### 2. Crear buckets en S3

```bash
aws s3 mb s3://image-classification-input
aws s3 mb s3://image-classification-results
```

### 3. Crear la función Lambda

- Usa `lambda/lambda_function.py`
- Asocia un trigger S3 (al bucket `image-classification-input`)
- Asigna permisos para usar SageMaker

### 4. Ejecutar scripts en EC2

```bash
python ec2/upload_images.py ruta/a/imagen.jpg
python ec2/get_results.py
```

## Uso de Docker

### Entrenamiento local

```bash
chmod +x docker/run_train.sh
./docker/run_train.sh
```

### (Opcional) Ejecutar Lambda en Docker

```bash
docker build -f docker/Dockerfile.lambda -t lambda-image .
docker run -p 9000:8080 lambda-image
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```

## Requisitos

- AWS CLI configurado
- Python 3.8+
- Docker
