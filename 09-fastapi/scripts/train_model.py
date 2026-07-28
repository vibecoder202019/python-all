"""Train Iris model cho FastAPI demo"""
from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

MODEL_DIR = Path(__file__).parent.parent / "models"
MODEL_DIR.mkdir(exist_ok=True)


def main():
    print("=== Training Iris Classifier ===")
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)

    accuracy = accuracy_score(y_test, model.predict(X_test_scaled))
    print(f"Accuracy: {accuracy:.4f}")

    joblib.dump(model, MODEL_DIR / "iris_model.joblib")
    joblib.dump(scaler, MODEL_DIR / "iris_scaler.joblib")
    joblib.dump(
        {
            "model_type": "RandomForestClassifier",
            "features": list(iris.feature_names),
            "target_names": list(iris.target_names),
            "accuracy": accuracy,
        },
        MODEL_DIR / "metadata.joblib",
    )

    print(f"Model saved to {MODEL_DIR}/")
    print("Chạy API: uvicorn app.main:app --reload")


if __name__ == "__main__":
    main()
