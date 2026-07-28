# Bài tập Module 09: FastAPI

> Chạy server trước: `uvicorn app.main:app --reload`

## Bài 1: Thêm endpoint GET /users/search (Dễ)
Query param `q` — tìm user theo tên (case-insensitive).

## Bài 2: Thêm validation email (Dễ)
Dùng regex validate email format trong UserCreate.

## Bài 3: Batch prediction (Trung bình)
POST `/predict/batch` — nhận list features, trả list predictions.

## Bài 4: Middleware logging (Trung bình)
Thêm middleware log mỗi request: method, path, status_code, duration.

## Bài 5: Authentication cơ bản (Khó)
Thêm API key authentication qua header `X-API-Key`.

## Bài 6: Full CRUD + ML API (Khó)
Mở rộng project: thêm endpoint upload CSV → train model mới → predict.

---

## Hướng dẫn test

```bash
# Terminal 1: chạy server
cd 09-fastapi
python scripts/train_model.py
uvicorn app.main:app --reload

# Terminal 2: test
pytest tests/ -v
python examples/client_demo.py

# Hoặc dùng curl
curl http://localhost:8000/health
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
```

Đáp án: [solutions/solutions.py](solutions/solutions.py)
