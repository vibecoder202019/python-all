"""Test FastAPI endpoints"""
import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


class TestRoot:
    def test_root(self):
        response = client.get("/")
        assert response.status_code == 200
        assert "message" in response.json()

    def test_health(self):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"


class TestUsers:
    def test_list_users(self):
        response = client.get("/users")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_get_user(self):
        response = client.get("/users/1")
        assert response.status_code == 200
        assert response.json()["id"] == 1

    def test_get_user_not_found(self):
        response = client.get("/users/999")
        assert response.status_code == 404

    def test_create_user(self):
        response = client.post("/users", json={
            "name": "Test User",
            "email": "test@example.com",
            "age": 25,
        })
        assert response.status_code == 201
        assert response.json()["name"] == "Test User"

    def test_create_user_invalid(self):
        response = client.post("/users", json={
            "name": "A",
            "email": "invalid",
            "age": -1,
        })
        assert response.status_code == 422

    def test_delete_user(self):
        create_resp = client.post("/users", json={
            "name": "To Delete",
            "email": "delete@example.com",
            "age": 20,
        })
        user_id = create_resp.json()["id"]
        response = client.delete(f"/users/{user_id}")
        assert response.status_code == 204


class TestPredict:
    def test_predict(self):
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
        response = client.post("/predict", json={
            "sepal_length": -1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2,
        })
        assert response.status_code == 422
