"""Dự án tổng hợp — California Housing Price Predictor API"""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import predict


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🏠 House Price Predictor API starting...")
    yield
    print("👋 Shutting down...")


app = FastAPI(
    title="House Price Predictor",
    description="API dự đoán giá nhà California — Dự án tổng hợp Module 10",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(predict.router, prefix="/model", tags=["Model"])


@app.get("/", tags=["Root"])
def root():
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
    return {"status": "healthy"}
