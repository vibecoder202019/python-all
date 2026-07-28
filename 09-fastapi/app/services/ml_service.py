"""ML Service — load model và thực hiện prediction"""
from pathlib import Path

import joblib

from app.models.schemas import ModelInfo, PredictionOutput

MODEL_DIR = Path(__file__).parent.parent.parent / "models"


class MLService:
    def __init__(self):
        self._model = None
        self._scaler = None
        self._metadata = None

    def _load(self):
        if self._model is None:
            model_path = MODEL_DIR / "iris_model.joblib"
            scaler_path = MODEL_DIR / "iris_scaler.joblib"
            meta_path = MODEL_DIR / "metadata.joblib"

            if not model_path.exists():
                raise FileNotFoundError(f"Model not found: {model_path}")

            self._model = joblib.load(model_path)
            self._scaler = joblib.load(scaler_path)
            self._metadata = joblib.load(meta_path)

    def predict(self, features: list[float]) -> PredictionOutput:
        self._load()
        scaled = self._scaler.transform([features])
        pred_idx = self._model.predict(scaled)[0]
        probas = self._model.predict_proba(scaled)[0]

        target_names = self._metadata["target_names"]
        species = target_names[pred_idx]
        confidence = float(probas[pred_idx])
        all_probs = {name: float(p) for name, p in zip(target_names, probas)}

        return PredictionOutput(
            species=species,
            confidence=confidence,
            all_probabilities=all_probs,
        )

    def get_model_info(self) -> ModelInfo:
        self._load()
        return ModelInfo(
            model_type=self._metadata["model_type"],
            features=self._metadata["features"],
            target_classes=self._metadata["target_names"],
            accuracy=self._metadata["accuracy"],
        )
