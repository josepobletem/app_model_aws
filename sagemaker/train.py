from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import joblib
import os

def model_fn(model_dir):
    return joblib.load(os.path.join(model_dir, "model.joblib"))

if __name__ == '__main__':
    iris = load_iris()
    X, y = iris.data, iris.target
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)

    joblib.dump(model, "model.joblib")
