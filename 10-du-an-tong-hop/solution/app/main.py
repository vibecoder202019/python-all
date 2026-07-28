"""
Dự án tổng hợp — California Housing Price Predictor API.

MỤC ĐÍCH:
    API dự đoán giá nhà California từ 8 đặc trưng — tổng hợp kiến thức Module 10.

YÊU CẦU:
    - fastapi, uvicorn, scikit-learn, joblib
    - Model: python scripts/train_model.py

CÁCH CHẠY:
    uvicorn app.main:app --reload
    Swagger UI: http://localhost:8000/docs

KẾT QUẢ MONG ĐỢI:
    POST /model/predict trả giá nhà dự đoán (đơn vị $100k và USD).
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import predict


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Quản lý vòng đời app — log startup/shutdown."""
    print("🏠 House Price Predictor API starting...")
    yield
    print("👋 Shutting down...")


# FastAPI app — metadata hiển thị trên /docs
app = FastAPI(
    title="House Price Predictor",
    description="API dự đoán giá nhà California — Dự án tổng hợp Module 10",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS — cho phép client từ domain khác gọi API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router predict — prefix /model → /model/predict, /model/info
app.include_router(predict.router, prefix="/model", tags=["Model"])


@app.get("/", tags=["Root"])
def root():
    """Endpoint gốc — hướng dẫn các endpoint chính."""
    return {
        "project": "House Price Predictor API",
        "docs": "/docs",
        "endpoints": {
            "health": "/health",
            "predict": "POST /model/predict",
            "model_info": "GET /model/info",
        },
    }


@app.get("/health", tags=["Root"])
def health():
    """Health check — monitoring."""
    return {"status": "healthy"}
