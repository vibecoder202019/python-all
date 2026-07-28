"""
Test FastAPI endpoints — kiểm thử API không cần chạy server thật.

MỤC ĐÍCH:
    Verify các endpoint root, users CRUD, và ML predict hoạt động đúng.

YÊU CẦU:
    pytest, fastapi, httpx (TestClient)

CÁCH CHẠY:
    pytest tests/test_api.py -v
    (Model predict: chạy scripts/train_model.py trước, hoặc test skip nếu 503)

KẾT QUẢ MONG ĐỢI:
    Tất cả test pass — status code và JSON body đúng kỳ vọng.
"""
import pytest
from fastapi.testclient import TestClient

from app.main import app

# TestClient — gọi API in-process, không cần uvicorn
client = TestClient(app)


class TestRoot:
    """Test endpoint gốc và health check."""

    def test_root(self):
        """GET / trả 200 và có field message."""
        response = client.get("/")
        assert response.status_code == 200
        assert "message" in response.json()

    def test_health(self):
        """GET /health trả status healthy."""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"


class TestUsers:
    """Test CRUD users — in-memory database."""

    def test_list_users(self):
        """GET /users trả danh sách."""
        response = client.get("/users")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_get_user(self):
        """GET /users/1 — user seed data có sẵn."""
        response = client.get("/users/1")
        assert response.status_code == 200
        assert response.json()["id"] == 1

    def test_get_user_not_found(self):
        """GET /users/999 — user không tồn tại → 404."""
        response = client.get("/users/999")
        assert response.status_code == 404

    def test_create_user(self):
        """POST /users hợp lệ → 201 Created."""
        response = client.post("/users", json={
            "name": "Test User",
            "email": "test@example.com",
            "age": 25,
        })
        assert response.status_code == 201
        assert response.json()["name"] == "Test User"

    def test_create_user_invalid(self):
        """POST /users sai validation (age âm, email invalid) → 422."""
        response = client.post("/users", json={
            "name": "A",
            "email": "invalid",
            "age": -1,
        })
        assert response.status_code == 422

    def test_delete_user(self):
        """DELETE /users/{id} sau khi tạo → 204 No Content."""
        create_resp = client.post("/users", json={
            "name": "To Delete",
            "email": "delete@example.com",
            "age": 20,
        })
        user_id = create_resp.json()["id"]
        response = client.delete(f"/users/{user_id}")
        assert response.status_code == 204


class TestPredict:
    """Test ML prediction endpoint."""

    def test_predict(self):
        """POST /predict — trả species và confidence nếu model đã train."""
        response = client.post("/predict", json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2,
        })
        if response.status_code == 503:
            pytest.skip("Model chưa train — chạy: python scripts/train_model.py")
        assert response.status_code == 200
        data = response.json()
        assert "species" in data
        assert "confidence" in data
        assert data["confidence"] > 0

    def test_predict_invalid(self):
        """POST /predict với sepal_length âm → 422 validation error."""
        response = client.post("/predict", json={
            "sepal_length": -1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2,
        })
        assert response.status_code == 422
