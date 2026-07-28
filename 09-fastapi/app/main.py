"""
FastAPI Application — Entry Point (Điểm khởi tạo ứng dụng)

MỤC ĐÍCH:
    Tạo FastAPI app, cấu hình CORS, đăng ký routers (users + predict),
    và expose các endpoint gốc (/, /health).

YÊU CẦU:
    - Đã cài: fastapi, uvicorn
    - Model ML (tuỳ chọn): chạy `python scripts/train_model.py` trước khi dùng /predict

CÁCH CHẠY:
    uvicorn app.main:app --reload
    Swagger UI: http://localhost:8000/docs

KẾT QUẢ MONG ĐỢI:
    Server chạy tại localhost:8000, trả JSON cho CRUD users và dự đoán Iris.
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import predict, users


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Quản lý vòng đời app: log khi khởi động và tắt server."""
    print("🚀 Starting ML API server...")
    yield
    print("👋 Shutting down...")


# Khởi tạo FastAPI app — title/description hiển thị trên Swagger UI
app = FastAPI(
    title="Python AI Learning API",
    description="API học FastAPI — CRUD users + ML prediction (Iris classifier)",
    version="1.0.0",
    lifespan=lifespan,  # Hook startup/shutdown
)

# CORS middleware — cho phép frontend gọi API từ domain khác
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Dev: cho phép mọi origin
    allow_methods=["*"],
    allow_headers=["*"],
)

# include_router — gắn nhóm endpoint vào app chính, prefix là tiền tố URL
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(predict.router, prefix="/predict", tags=["ML Prediction"])


@app.get("/", tags=["Root"])
def root():
    """Endpoint gốc — trả thông tin API và danh sách endpoint chính."""
    return {
        "message": "Chào mừng đến Python AI Learning API!",
        "docs": "/docs",
        "endpoints": {
            "users": "/users",
            "predict": "/predict",
            "health": "/health",
        },
    }


@app.get("/health", tags=["Root"])
def health():
    """Health check — dùng để kiểm tra server còn sống (monitoring, load balancer)."""
    return {"status": "healthy", "version": "1.0.0"}
