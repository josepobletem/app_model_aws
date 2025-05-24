from Trainer.train import model_fn
import os

def test_model_loading():
    model = model_fn(".")
    assert model is not None
