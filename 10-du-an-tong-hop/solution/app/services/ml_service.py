"""ML Service — House Price Predictor"""
from pathlib import Path

import joblib

from app.models.schemas import ModelInfo, PricePrediction

MODEL_DIR = Path(__file__).parent.parent.parent / "models"


class MLService:
    def __init__(self):
        self._model = None
        self._scaler = None
        self._metadata = None

    def _load(self):
        if self._model is None:
            model_path = MODEL_DIR / "house_model.joblib"
            if not model_path.exists():
                raise FileNotFoundError(f"Model not found: {model_path}")
            self._model = joblib.load(model_path)
            self._scaler = joblib.load(MODEL_DIR / "house_scaler.joblib")
            self._metadata = joblib.load(MODEL_DIR / "metadata.joblib")

    def predict(self, features: list[float]) -> PricePrediction:
        self._load()
        scaled = self._scaler.transform([features])
        price = float(self._model.predict(scaled)[0])
        return PricePrediction(
            predicted_price=round(price, 4),
            predicted_price_usd=round(price * 100_000, 2),
        )

    def get_model_info(self) -> ModelInfo:
        self._load()
        return ModelInfo(
            model_type=self._metadata["model_type"],
            features=self._metadata["features"],
            r2_score=self._metadata["r2_score"],
            rmse=self._metadata["rmse"],
        )
