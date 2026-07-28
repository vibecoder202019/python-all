"""
Train Iris model cho FastAPI demo.

MỤC ĐÍCH:
    Train RandomForestClassifier trên dataset Iris, lưu model + scaler + metadata.

YÊU CẦU:
    scikit-learn, joblib

CÁCH CHẠY:
    python scripts/train_model.py

KẾT QUẢ MONG ĐỢI:
    - models/iris_model.joblib, iris_scaler.joblib, metadata.joblib
    - Accuracy in ~0.95+ trên test set
    - Sau đó: uvicorn app.main:app --reload
"""
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
    """Pipeline train: load data → split → scale → fit → evaluate → save."""
    print("=== Training Iris Classifier ===")

    # Bước 1: Load dataset Iris (150 mẫu, 4 features, 3 classes)
    iris = load_iris()
    # Bước 2: Chia train/test 80/20, stratify giữ tỷ lệ class
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target
    )

    # Bước 3: Chuẩn hóa features — fit trên train, transform cả train và test
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Bước 4: Train RandomForest — ensemble 100 cây quyết định
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)

    # Bước 5: Đánh giá accuracy trên test set
    accuracy = accuracy_score(y_test, model.predict(X_test_scaled))
    print(f"Accuracy: {accuracy:.4f}")

    # Bước 6: Lưu artifacts — model, scaler, metadata cho API
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
