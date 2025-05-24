import joblib
import os

def test_model_loading(tmp_path):
    # Crear modelo de prueba
    model_path = tmp_path / "model.joblib"
    joblib.dump({"modelo": "dummy"}, model_path)

    from Trainer.train import model_fn
    model = model_fn(tmp_path)
    assert "modelo" in model
