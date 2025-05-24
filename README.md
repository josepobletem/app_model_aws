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
3. Crear la función Lambda
    \cdot Usa lambda/lambda_function.py

    \cdot Asocia un trigger S3 (al bucket image-classification-input)

    \cdot Asigna permisos para usar SageMaker

## 4. Usar scripts en EC2
```bash
python ec2/upload_images.py ruta/a/imagen.jpg
python ec2/get_results.py
```
### Requisitos

   \cdot AWS CLI configurado
   \cdot Python 3.8+
   \cdot SageMaker y Lambda con permisos adecuados
