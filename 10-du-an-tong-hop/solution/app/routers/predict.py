"""
Prediction router — House Price Predictor endpoints.

MỤC ĐÍCH:
    Expose API dự đoán giá nhà (đơn lẻ và batch) và xem thông tin model.

YÊU CẦU:
    Model đã train: python scripts/train_model.py

KẾT QUẢ MONG ĐỢI:
    - POST /model/predict — dự đoán 1 căn nhà
    - POST /model/predict/batch — dự đoán nhiều căn
    - GET /model/info — R², RMSE, features
"""
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
    """
    Dự đoán giá nhà từ 8 features California Housing.

    Pydantic validate input → to_features() → MLService.predict().
    """
    try:
        return ml_service.predict(house.to_features())
    except FileNotFoundError:
        raise HTTPException(status_code=503, detail="Model chưa train. Chạy: python scripts/train_model.py")


@router.post("/predict/batch", response_model=BatchPredictionOutput)
def predict_batch(input_data: BatchPredictionInput):
    """Dự đoán giá nhiều căn nhà — lặp qua list HouseFeatures."""
    try:
        predictions = [ml_service.predict(h.to_features()) for h in input_data.houses]
        return BatchPredictionOutput(predictions=predictions)
    except FileNotFoundError:
        raise HTTPException(status_code=503, detail="Model chưa train.")


@router.get("/info", response_model=ModelInfo)
def model_info():
    """Thông tin model — loại, features, R², RMSE."""
    try:
        return ml_service.get_model_info()
    except FileNotFoundError:
        raise HTTPException(status_code=503, detail="Model chưa train.")
