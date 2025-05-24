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


## CI/CD con GitHub Actions

Este repositorio incluye una pipeline de GitHub Actions para ejecutar pruebas automáticas con `pytest`.

### Estructura

- `.github/workflows/ci.yml`: configura la integración continua
- `tests/`: pruebas unitarias de cada módulo (Lambda, entrenamiento, EC2)

### Cómo funciona

Cada push o pull request a la rama `main` dispara:

1. Instalación de dependencias
2. Ejecución de pruebas con `pytest`

### Ejecutar pruebas localmente

```bash
pip install -r docker/requirements.txt
pip install pytest boto3
pytest
```


## Análisis de calidad con Pylint

Este proyecto incluye verificación de estilo y calidad de código con `pylint`.

### Ejecutar localmente

```bash
pip install pylint
pylint lambda/*.py sagemaker/*.py ec2/*.py
```

### Integración continua

GitHub Actions también ejecuta `pylint` automáticamente en cada push o PR.


## Makefile

Puedes usar `make` para facilitar comandos comunes:

```bash
make install   # Instala dependencias
make test      # Ejecuta pruebas con pytest
make lint      # Ejecuta pylint
make ci        # Ejecuta pruebas y lint (lo que usa GitHub Actions)
```
