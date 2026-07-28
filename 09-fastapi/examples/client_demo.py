"""Ví dụ gọi API bằng httpx — client-side"""
import httpx

BASE_URL = "http://localhost:8000"


def demo():
    print("=== FastAPI Client Demo ===\n")

    # Health check
    response = httpx.get(f"{BASE_URL}/health")
    print(f"Health: {response.json()}")

    # List users
    response = httpx.get(f"{BASE_URL}/users")
    users = response.json()
    print(f"\nUsers ({len(users)}):")
    for u in users:
        print(f"  [{u['id']}] {u['name']} — {u['email']}")

    # Create user
    response = httpx.post(f"{BASE_URL}/users", json={
        "name": "Client Demo User",
        "email": "client@demo.com",
        "age": 28,
    })
    if response.status_code == 201:
        new_user = response.json()
        print(f"\nCreated user: {new_user}")

    # ML Prediction
    response = httpx.post(f"{BASE_URL}/predict", json={
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
    })
    if response.status_code == 200:
        pred = response.json()
        print(f"\nPrediction:")
        print(f"  Species: {pred['species']}")
        print(f"  Confidence: {pred['confidence']:.2%}")
        print(f"  All probabilities: {pred['all_probabilities']}")
    else:
        print(f"\nPrediction failed: {response.status_code} — {response.json()}")
        print("Chạy: python scripts/train_model.py trước")

    # Model info
    response = httpx.get(f"{BASE_URL}/predict/model-info")
    if response.status_code == 200:
        info = response.json()
        print(f"\nModel Info:")
        print(f"  Type: {info['model_type']}")
        print(f"  Accuracy: {info['accuracy']:.2%}")
        print(f"  Classes: {info['target_classes']}")


if __name__ == "__main__":
    demo()
