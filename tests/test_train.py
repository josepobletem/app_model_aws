import joblib

def test_model_loading(tmp_path):
    # Crear modelo de prueba
    model_path = tmp_path / "model.joblib"
    joblib.dump({"modelo": "dummy"}, model_path)

    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

    from trainer.train import model_fn
    model = model_fn(tmp_path)
    assert "modelo" in model
