import json
from unittest.mock import patch, MagicMock

@patch("boto3.client")
def test_lambda_handler_mock_sagemaker(mock_boto_client):
    mock_runtime = MagicMock()
    mock_runtime.invoke_endpoint.return_value = {
        "Body": MagicMock(read=lambda: b'{"predicted_label": "cat"}')
    }
    mock_boto_client.return_value = mock_runtime

    import lambda_fn.lambda_function as lf

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
    response = lf.lambda_handler(event, None)

    assert "predicted_label" in json.loads(response["body"])
    assert response["predicted_label"] == "cat"
