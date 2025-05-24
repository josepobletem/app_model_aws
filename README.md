# app_model_aws
Proyecto de generar una app de un modelo via request preguntarle predicciones,  tanto con lambda function como con segmaker

# Image Classifier with AWS EC2, S3, Lambda & SageMaker

Este proyecto implementa un sistema de clasificación de imágenes utilizando servicios de AWS.

## Arquitectura

- **S3**: almacenamiento de imágenes y resultados
- **Lambda**: ejecución automática al subir imagen
- **SageMaker**: entrenamiento y despliegue del modelo
- **EC2**: scripts para interacción manual

## Pasos para desplegar

### 1. Entrenar y desplegar el modelo

```bash
cd sagemaker
python deploy.py
```
Esto entrenará un modelo y lo desplegará en SageMaker.

## 2. Crear buckets en S3
```bash
aws s3 mb s3://image-classification-input
aws s3 mb s3://image-classification-results
```
## 3. Crear la función Lambda

- Usa lambda/lambda_function.py
- Asocia un trigger S3 (al bucket image-classification-input)
- Asigna permisos para usar SageMaker

## 4. Usar scripts en EC2
```bash
python ec2/upload_images.py ruta/a/imagen.jpg
python ec2/get_results.py
```
### Requisitos

- AWS CLI configurado
- Python 3.8+
- SageMaker y Lambda con permisos adecuados

## Estructura del proyecto con Docker
```python
image-classifier/
│
├── docker/
│   ├── Dockerfile.train              # Docker para entrenamiento local
│   ├── Dockerfile.lambda             # (opcional) Docker para Lambda
│   ├── run_train.sh                  # Script de ejecución local
│   └── requirements.txt              # Dependencias para entrenamiento
│
├── lambda/
│   └── lambda_function.py
│
├── sagemaker/
│   ├── train.py
│   └── deploy.py
│
├── ec2/
│   ├── upload_images.py
│   └── get_results.py
│
├── README.md
└── .gitignore
```

### 1. docker/Dockerfile.train

```Dockerfile
### 1. docker/Dockerfile.train
FROM python:3.10-slim

WORKDIR /app

COPY docker/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY sagemaker/train.py .

CMD ["python", "train.py"]
```
### 2. docker/requirements.txt

```bash
scikit-learn
joblib
```
### 3. docker/run_train.sh

```bash
#!/bin/bash
docker build -f docker/Dockerfile.train -t image-classifier-train .
docker run --rm -v $(pwd)/output:/app/output image-classifier-train
```
