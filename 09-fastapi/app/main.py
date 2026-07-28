"""FastAPI Application — Entry Point"""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import predict, users


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Starting ML API server...")
    yield
    print("👋 Shutting down...")


app = FastAPI(
    title="Python AI Learning API",
    description="API học FastAPI — CRUD users + ML prediction (Iris classifier)",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(predict.router, prefix="/predict", tags=["ML Prediction"])


@app.get("/", tags=["Root"])
def root():
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
    return {"status": "healthy", "version": "1.0.0"}
