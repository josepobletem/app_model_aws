# Importa tu módulo Lambda (ajusta el nombre si es diferente)
import lambda_fn.lambda_function as lf
from unittest.mock import patch, MagicMock

@patch("boto3.client")
def test_lambda_handler_mock_sagemaker(mock_boto_client):
    # Simulación del cliente de S3
    mock_s3 = MagicMock()
    mock_s3.get_object.return_value = {
        'Body': MagicMock(read=lambda: b'test image bytes')
    }

    # Simulación del cliente de SageMaker Runtime
    mock_runtime = MagicMock()
    mock_runtime.invoke_endpoint.return_value = {
        'Body': MagicMock(read=lambda: b'{"predicted_label": "cat"}')
    }

    # Dependiendo del nombre del servicio, devolvemos el mock adecuado
    mock_boto_client.side_effect = lambda service_name, *args, **kwargs: (
        mock_s3 if service_name == 's3' else mock_runtime
    )

    # Evento de prueba simulado
    event = {
        "Records": [
            {
                "s3": {
                    "bucket": {"name": "my-bucket"},
                    "object": {"key": "image.png"}
                }
            }
        ]
    }

    # Ejecuta la función con el evento simulado
    response = lf.lambda_handler(event, None)

    # Verifica que la respuesta sea la esperada
    assert response['statusCode'] == 200
