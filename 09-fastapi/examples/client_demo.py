"""
Ví dụ gọi API bằng httpx — client-side demo.

MỤC ĐÍCH:
    Minh họa cách gọi REST API từ Python (không cần browser/curl).

YÊU CẦU:
    - Server đang chạy: uvicorn app.main:app --reload
    - httpx đã cài
    - Model (tuỳ chọn): python scripts/train_model.py

CÁCH CHẠY:
    python examples/client_demo.py

KẾT QUẢ MONG ĐỢI:
    In ra health, danh sách users, user mới, prediction Iris, model info.
"""
import httpx

BASE_URL = "http://localhost:8000"


def demo():
    """Chạy demo gọi tuần tự các endpoint API."""
    print("=== FastAPI Client Demo ===\n")

    # Health check — kiểm tra server sống
    response = httpx.get(f"{BASE_URL}/health")
    print(f"Health: {response.json()}")

    # List users — GET với query params mặc định
    response = httpx.get(f"{BASE_URL}/users")
    users = response.json()
    print(f"\nUsers ({len(users)}):")
    for u in users:
        print(f"  [{u['id']}] {u['name']} — {u['email']}")

    # Create user — POST JSON body
    response = httpx.post(f"{BASE_URL}/users", json={
        "name": "Client Demo User",
        "email": "client@demo.com",
        "age": 28,
    })
    if response.status_code == 201:
        new_user = response.json()
        print(f"\nCreated user: {new_user}")

    # ML Prediction — POST 4 features Iris
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

    # Model info — GET metadata
    response = httpx.get(f"{BASE_URL}/predict/model-info")
    if response.status_code == 200:
        info = response.json()
        print(f"\nModel Info:")
        print(f"  Type: {info['model_type']}")
        print(f"  Accuracy: {info['accuracy']:.2%}")
        print(f"  Classes: {info['target_classes']}")


if __name__ == "__main__":
    demo()
