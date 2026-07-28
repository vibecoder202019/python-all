"""
ML Prediction router — serve Iris classifier qua REST API.

MỤC ĐÍCH:
    Expose endpoint dự đoán loài Iris và xem thông tin model.

YÊU CẦU:
    - Model đã train: `python scripts/train_model.py`
    - File model trong thư mục models/

KẾT QUẢ MONG ĐỢI:
    - POST /predict — dự đoán species + confidence
    - GET /predict/model-info — metadata model (accuracy, features, classes)
    - 503 nếu model chưa train
"""
from fastapi import APIRouter, HTTPException

from app.models.schemas import ModelInfo, PredictionInput, PredictionOutput
from app.services.ml_service import MLService

router = APIRouter()
ml_service = MLService()  # Singleton service — lazy load model khi predict


@router.post("", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
    """
    Dự đoán loài Iris từ 4 đặc trưng hoa.

    - **sepal_length**: Chiều dài đài hoa (cm)
    - **sepal_width**: Chiều rộng đài hoa (cm)
    - **petal_length**: Chiều dài cánh hoa (cm)
    - **petal_width**: Chiều rộng cánh hoa (cm)

    response_model=PredictionOutput — serialize output theo schema Pydantic.
    """
    try:
        # to_features() chuyển Pydantic model → list[float] cho sklearn
        return ml_service.predict(input_data.to_features())
    except FileNotFoundError:
        raise HTTPException(
            status_code=503,
            detail="Model chưa được train. Chạy: python scripts/train_model.py",
        )


@router.get("/model-info", response_model=ModelInfo)
def model_info():
    """Thông tin về model ML đang sử dụng (loại model, accuracy, features)."""
    try:
        return ml_service.get_model_info()
    except FileNotFoundError:
        raise HTTPException(
            status_code=503,
            detail="Model chưa được train. Chạy: python scripts/train_model.py",
        )
