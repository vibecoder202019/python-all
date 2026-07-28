# Module 09: FastAPI & REST API

## Mục tiêu

- Hiểu REST API và HTTP methods
- Xây dựng API với FastAPI
- Validation với Pydantic
- Serve ML model qua API
- Test API với Swagger UI và httpx

---

## Lý thuyết nền tảng — API là gì?

**API (Application Programming Interface)** = "cửa sổ giao tiếp" giữa 2 phần mềm.

```
Mobile App  ──HTTP JSON──►  FastAPI Server  ──►  ML Model
Website     ──HTTP JSON──►  FastAPI Server  ──►  Database
```

App **không cần biết** model train thế nào — chỉ cần gửi JSON, nhận JSON.

### REST — quy ước thiết kế API

REST dùng **HTTP methods** + **URL** để thể hiện hành động:

| Hành động | HTTP | URL ví dụ |
|-----------|------|-----------|
| Xem danh sách | GET | `/users` |
| Xem 1 item | GET | `/users/42` |
| Tạo mới | POST | `/users` |
| Cập nhật | PUT | `/users/42` |
| Xóa | DELETE | `/users/42` |

### JSON — ngôn ngữ chung của API

```json
{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}
```

→ Server trả:
```json
{"species": "setosa", "confidence": 0.97}
```

### FastAPI — tại sao chọn?

| Ưu điểm | Giải thích |
|---------|------------|
| Nhanh | Dựa trên Starlette + Pydantic (async) |
| Tự document | Swagger UI `/docs` tự generate |
| Type hints | IDE gợi ý, ít bug |
| Validation tự động | Pydantic reject input sai → 422 |

### Pydantic — "cảnh sát giao thông" cho data

```python
class UserCreate(BaseModel):
    age: int = Field(ge=0, le=150)  # Tuổi 0-150, sai → lỗi 422
```

Client gửi `age: -5` → FastAPI **tự từ chối**, không cần viết if/else validation.

### Kiến trúc 3 lớp (best practice)

```
Router (HTTP)  →  Service (logic)  →  Model/Data (ML, DB)
predict.py          ml_service.py       iris_model.joblib
users.py            (CRUD logic)        (in-memory dict)
```

Tách lớp giúp: dễ test, dễ thay model, dễ maintain.

---

## 1. REST API là gì?

**REST** (Representational State Transfer) — kiến trúc giao tiếp client-server qua HTTP.

| Method | Mục đích | Ví dụ |
|--------|---------|-------|
| GET | Lấy dữ liệu | `GET /users/1` |
| POST | Tạo mới | `POST /users` |
| PUT | Cập nhật toàn bộ | `PUT /users/1` |
| PATCH | Cập nhật một phần | `PATCH /users/1` |
| DELETE | Xóa | `DELETE /users/1` |

**HTTP Status Codes:**
- `200` OK — thành công
- `201` Created — tạo mới thành công
- `400` Bad Request — dữ liệu không hợp lệ
- `404` Not Found — không tìm thấy
- `422` Unprocessable Entity — validation fail
- `500` Internal Server Error — lỗi server

---

## 2. FastAPI — Hello World

```python
from fastapi import FastAPI

app = FastAPI(title="My API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/health")
def health():
    return {"status": "healthy"}
```

Chạy:
```bash
uvicorn app.main:app --reload
# Swagger UI: http://localhost:8000/docs
# ReDoc:      http://localhost:8000/redoc
```

---

## 3. Path Parameters & Query Parameters

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/items")
def list_items(skip: int = 0, limit: int = 10, q: str | None = None):
    return {"skip": skip, "limit": limit, "query": q}
```

- **Path param** — `/users/42` → `user_id=42`
- **Query param** — `/items?skip=0&limit=10&q=python`

---

## 4. Pydantic Models — Request/Response Validation

```python
from pydantic import BaseModel, Field, EmailStr

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: str
    age: int = Field(..., ge=0, le=150)

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    return UserResponse(id=1, name=user.name, email=user.email)
```

FastAPI tự động:
- Validate input → trả 422 nếu sai
- Generate OpenAPI schema → Swagger UI
- Serialize response theo `response_model`

---

## 5. Dependency Injection

```python
from fastapi import Depends

def get_db():
    db = connect_db()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
def list_users(db=Depends(get_db)):
    return db.query(User).all()
```

Dùng cho: database connection, authentication, shared logic.

---

## 6. Error Handling

```python
from fastapi import HTTPException

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = find_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

---

## 7. Serve ML Model qua API

```python
import joblib
from pydantic import BaseModel

model = joblib.load("model.joblib")
scaler = joblib.load("scaler.joblib")

class PredictionInput(BaseModel):
    features: list[float]

class PredictionOutput(BaseModel):
    prediction: str
    confidence: float

@app.post("/predict", response_model=PredictionOutput)
def predict(input: PredictionInput):
    scaled = scaler.transform([input.features])
    pred = model.predict(scaled)[0]
    proba = model.predict_proba(scaled)[0].max()
    return PredictionOutput(prediction=str(pred), confidence=float(proba))
```

---

## 8. Cấu trúc Project FastAPI

```
09-fastapi/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI app entry point
│   ├── models/           # Pydantic schemas
│   │   └── schemas.py
│   ├── routers/          # API routes
│   │   ├── users.py
│   │   └── predict.py
│   ├── services/         # Business logic
│   │   └── ml_service.py
│   └── dependencies.py   # Shared dependencies
├── tests/
│   └── test_api.py
└── requirements.txt
```

---

## 9. Test API

### Swagger UI (trình duyệt)
```
http://localhost:8000/docs
```

### curl
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

### Python httpx
```python
import httpx

response = httpx.post(
    "http://localhost:8000/predict",
    json={"features": [5.1, 3.5, 1.4, 0.2]},
)
print(response.json())
```

### pytest
```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
```

---

## Chạy project mẫu

```bash
cd 09-fastapi

# Cài dependencies (từ thư mục learn-python-ai)
pip install -r ../requirements.txt

# Train model trước (nếu chưa có)
python scripts/train_model.py

# Chạy API
uvicorn app.main:app --reload --port 8000

# Mở Swagger UI
open http://localhost:8000/docs
```

---

## API Endpoints

| Method | Endpoint | Mô tả |
|--------|----------|-------|
| GET | `/` | Welcome message |
| GET | `/health` | Health check |
| GET | `/docs` | Swagger UI |
| GET | `/users` | Danh sách users |
| GET | `/users/{id}` | Chi tiết user |
| POST | `/users` | Tạo user mới |
| PUT | `/users/{id}` | Cập nhật user |
| DELETE | `/users/{id}` | Xóa user |
| POST | `/predict` | Dự đoán Iris species |
| GET | `/predict/model-info` | Thông tin model |

---

---

## Giải thích chi tiết (Tự học)

### Lệnh chạy server

```bash
uvicorn app.main:app --reload --port 8000
```

| Phần | Ý nghĩa |
|------|---------|
| `uvicorn` | ASGI server — chạy ứng dụng async Python |
| `app.main` | Module `app/main.py` |
| `:app` | Biến `app = FastAPI(...)` trong file đó |
| `--reload` | Tự restart khi sửa code (chỉ dev) |
| `--port 8000` | Lắng nghe cổng 8000 |

```bash
python scripts/train_model.py
```
- Train RandomForest trên Iris → lưu `models/iris_model.joblib`, `iris_scaler.joblib`, `metadata.joblib`

---

### Cấu trúc code `app/`

**`app/main.py`** — entry point:
```python
app = FastAPI(title="...", lifespan=lifespan)
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(predict.router, prefix="/predict", tags=["ML Prediction"])
```
- `include_router` — gắn nhóm endpoint vào app chính
- `prefix="/users"` — mọi route trong router có prefix `/users`

**`app/models/schemas.py`** — Pydantic models:
```python
class PredictionInput(BaseModel):
    sepal_length: float = Field(..., ge=0, le=10)
```
- `Field(..., ge=0)` — bắt buộc, giá trị ≥ 0
- FastAPI tự validate → trả **422** nếu client gửi sai

**`app/routers/users.py`** — CRUD:
```python
@router.get("", response_model=list[UserResponse])
@router.post("", status_code=201)
@router.put("/{user_id}")
@router.delete("/{user_id}", status_code=204)
```
- `response_model` — filter/serialize output
- `HTTPException(404)` — trả lỗi chuẩn REST

**`app/services/ml_service.py`** — business logic:
```python
def predict(self, features):
    self._load()                              # Lazy load model
    scaled = self._scaler.transform([features])
    pred_idx = self._model.predict(scaled)[0]
```
- Tách logic ML khỏi router — dễ test và thay model

---

### Test với curl

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
```
- `-X POST` — method HTTP
- `-H` — header
- `-d` — body JSON

**Swagger UI** (`/docs`) — giao diện test API trực tiếp trên browser, tự generate từ Pydantic schemas.

---

### File `tests/test_api.py`

```python
from fastapi.testclient import TestClient
client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
```
- `TestClient` — gọi API **không cần** chạy server thật
- `assert` — pytest fail nếu điều kiện sai

---

## Câu hỏi thường gặp (FAQ)

**Q: FastAPI vs Flask?**  
A: FastAPI nhanh hơn, tự validation + docs. Flask linh hoạt, ecosystem lớn hơn.

**Q: 422 vs 400?**  
A: 422 = validation fail (Pydantic). 400 = bad request nói chung.

**Q: `--reload` dùng production được không?**  
A: **Không** — chỉ dev. Production dùng gunicorn/uvicorn workers.

**Q: Model load lúc nào?**  
A: Lazy load (khi request đầu) hoặc startup event — module này dùng lazy load.

---

## Bài tập

→ [exercises/bai_tap.md](exercises/bai_tap.md)

## Module tiếp theo

→ [Module 10: Dự án tổng hợp](../10-du-an-tong-hop/README.md)
