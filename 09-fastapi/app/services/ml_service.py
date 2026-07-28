"""
ML Service — load model và thực hiện prediction.

MỤC ĐÍCH:
    Tách business logic ML khỏi router — dễ test, dễ thay model.

YÊU CẦU:
    - models/iris_model.joblib, iris_scaler.joblib, metadata.joblib
    - Tạo bằng: python scripts/train_model.py

KẾT QUẢ MONG ĐỢI:
    predict() trả PredictionOutput (species, confidence, all_probabilities)
    get_model_info() trả ModelInfo (model_type, features, accuracy)
"""
from pathlib import Path

import joblib

from app.models.schemas import ModelInfo, PredictionOutput

# Đường dẫn thư mục chứa model (tương đối từ file này)
MODEL_DIR = Path(__file__).parent.parent.parent / "models"


class MLService:
    """Service bọc model Iris — lazy load, scale features, predict."""

    def __init__(self):
        self._model = None      # RandomForestClassifier — load khi cần
        self._scaler = None     # StandardScaler đã fit lúc train
        self._metadata = None   # accuracy, feature names, target names

    def _load(self):
        """Lazy load — chỉ đọc file joblib lần đầu có request predict."""
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
        """
        Dự đoán loài Iris từ vector 4 đặc trưng.

        Pipeline: scale → predict → predict_proba → map index → species name.
        """
        self._load()
        # Bước 1: chuẩn hóa features (cùng scaler lúc train)
        scaled = self._scaler.transform([features])
        # Bước 2: dự đoán class index
        pred_idx = self._model.predict(scaled)[0]
        # Bước 3: xác suất từng class
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
        """Trả metadata model đã lưu lúc train."""
        self._load()
        return ModelInfo(
            model_type=self._metadata["model_type"],
            features=self._metadata["features"],
            target_classes=self._metadata["target_names"],
            accuracy=self._metadata["accuracy"],
        )
