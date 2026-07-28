"""
Train House Price model — California Housing Regressor.

MỤC ĐÍCH:
    Train RandomForestRegressor, đánh giá R²/RMSE, lưu model cho API.

YÊU CẦU:
    scikit-learn, joblib

CÁCH CHẠY:
    python scripts/train_model.py

KẾT QUẢ MONG ĐỢI:
    - models/house_model.joblib, house_scaler.joblib, metadata.joblib
    - R² thường > 0.7 trên test set
    - Sau đó: uvicorn app.main:app --reload
"""
from pathlib import Path

import joblib
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

MODEL_DIR = Path(__file__).parent.parent / "models"
MODEL_DIR.mkdir(exist_ok=True)


def main():
    """Pipeline train: load → split → scale → fit → evaluate → save."""
    print("=== Training House Price Predictor ===")

    # Bước 1: Load California Housing — 8 features, target = giá ($100k)
    housing = fetch_california_housing()
    # Bước 2: Chia train/test 80/20
    X_train, X_test, y_train, y_test = train_test_split(
        housing.data, housing.target, test_size=0.2, random_state=42
    )

    # Bước 3: Chuẩn hóa — fit trên train
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Bước 4: Train RandomForestRegressor — n_jobs=-1 dùng tất cả CPU
    model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train_scaled, y_train)

    # Bước 5: Đánh giá R² và RMSE trên test set
    y_pred = model.predict(X_test_scaled)
    r2 = r2_score(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred) ** 0.5
    print(f"R²: {r2:.4f}, RMSE: {rmse:.4f}")

    # Bước 6: Lưu model, scaler, metadata
    joblib.dump(model, MODEL_DIR / "house_model.joblib")
    joblib.dump(scaler, MODEL_DIR / "house_scaler.joblib")
    joblib.dump(
        {"model_type": "RandomForestRegressor", "features": list(housing.feature_names), "r2_score": r2, "rmse": rmse},
        MODEL_DIR / "metadata.joblib",
    )
    print(f"Model saved to {MODEL_DIR}/")


if __name__ == "__main__":
    main()
