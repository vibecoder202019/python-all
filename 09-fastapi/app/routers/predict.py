"""ML Prediction router — serve Iris classifier"""
from fastapi import APIRouter, HTTPException

from app.models.schemas import ModelInfo, PredictionInput, PredictionOutput
from app.services.ml_service import MLService

router = APIRouter()
ml_service = MLService()


@router.post("", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
    """
    Dự đoán loài Iris từ 4 đặc trưng hoa.

    - **sepal_length**: Chiều dài đài hoa (cm)
    - **sepal_width**: Chiều rộng đài hoa (cm)
    - **petal_length**: Chiều dài cánh hoa (cm)
    - **petal_width**: Chiều rộng cánh hoa (cm)
    """
    try:
        return ml_service.predict(input_data.to_features())
    except FileNotFoundError:
        raise HTTPException(
            status_code=503,
            detail="Model chưa được train. Chạy: python scripts/train_model.py",
        )


@router.get("/model-info", response_model=ModelInfo)
def model_info():
    """Thông tin về model ML đang sử dụng."""
    try:
        return ml_service.get_model_info()
    except FileNotFoundError:
        raise HTTPException(
            status_code=503,
            detail="Model chưa được train. Chạy: python scripts/train_model.py",
        )
