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
