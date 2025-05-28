import os
import sys
import joblib

# Agregar la ruta del proyecto para que funcione el import relativo
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from trainer.train import model_fn

def test_model_loading(tmp_path):
    # Crear modelo de prueba
    model_path = tmp_path / "model.joblib"
    joblib.dump({"modelo": "dummy"}, model_path)

    model = model_fn(tmp_path)
    assert "modelo" in model