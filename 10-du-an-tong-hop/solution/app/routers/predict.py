"""Prediction router"""
from fastapi import APIRouter, HTTPException

from app.models.schemas import (
    BatchPredictionInput,
    BatchPredictionOutput,
    HouseFeatures,
    ModelInfo,
    PricePrediction,
)
from app.services.ml_service import MLService

router = APIRouter()
ml_service = MLService()


@router.post("/predict", response_model=PricePrediction)
def predict(house: HouseFeatures):
    """Dự đoán giá nhà từ 8 features."""
    try:
        return ml_service.predict(house.to_features())
    except FileNotFoundError:
        raise HTTPException(status_code=503, detail="Model chưa train. Chạy: python scripts/train_model.py")


@router.post("/predict/batch", response_model=BatchPredictionOutput)
def predict_batch(input_data: BatchPredictionInput):
    """Dự đoán giá nhiều căn nhà."""
    try:
        predictions = [ml_service.predict(h.to_features()) for h in input_data.houses]
        return BatchPredictionOutput(predictions=predictions)
    except FileNotFoundError:
        raise HTTPException(status_code=503, detail="Model chưa train.")


@router.get("/info", response_model=ModelInfo)
def model_info():
    """Thông tin model."""
    try:
        return ml_service.get_model_info()
    except FileNotFoundError:
        raise HTTPException(status_code=503, detail="Model chưa train.")
