"""
ML Service — House Price Predictor.

MỤC ĐÍCH:
    Load model regression, scale features, predict giá nhà California.

YÊU CẦU:
    models/house_model.joblib, house_scaler.joblib, metadata.joblib
    Tạo bằng: python scripts/train_model.py

KẾT QUẢ MONG ĐỢI:
    predict() trả PricePrediction (giá $100k và USD)
    get_model_info() trả R², RMSE, danh sách features
"""
from pathlib import Path

import joblib

from app.models.schemas import ModelInfo, PricePrediction

MODEL_DIR = Path(__file__).parent.parent.parent / "models"


class MLService:
    """Service bọc RandomForestRegressor — lazy load, scale, predict giá nhà."""

    def __init__(self):
        self._model = None      # RandomForestRegressor
        self._scaler = None     # StandardScaler
        self._metadata = None   # r2_score, rmse, feature names

    def _load(self):
        """Lazy load model artifacts từ thư mục models/."""
        if self._model is None:
            model_path = MODEL_DIR / "house_model.joblib"
            if not model_path.exists():
                raise FileNotFoundError(f"Model not found: {model_path}")
            self._model = joblib.load(model_path)
            self._scaler = joblib.load(MODEL_DIR / "house_scaler.joblib")
            self._metadata = joblib.load(MODEL_DIR / "metadata.joblib")

    def predict(self, features: list[float]) -> PricePrediction:
        """
        Dự đoán giá nhà từ vector 8 features.

        Pipeline: scale → predict → chuyển đơn vị $100k sang USD.
        """
        self._load()
        # Bước 1: chuẩn hóa features
        scaled = self._scaler.transform([features])
        # Bước 2: predict — target California Housing đơn vị $100,000
        price = float(self._model.predict(scaled)[0])
        return PricePrediction(
            predicted_price=round(price, 4),
            predicted_price_usd=round(price * 100_000, 2),  # Nhân 100k → USD thực
        )

    def get_model_info(self) -> ModelInfo:
        """Trả metadata model (R², RMSE, features)."""
        self._load()
        return ModelInfo(
            model_type=self._metadata["model_type"],
            features=self._metadata["features"],
            r2_score=self._metadata["r2_score"],
            rmse=self._metadata["rmse"],
        )
