# Hướng dẫn chạy Manual — Module 09: FastAPI

> Copy từng lệnh và chạy **tuần tự**. Tương đương automation trong README mục "Chạy project mẫu".

## Điều kiện

- Python 3.10+
- Port 8000 trống

## Bước 0: Vào module và cài dependencies

```bash
cd learn-python-ai
source .venv/bin/activate
pip install -r requirements.txt
cd 09-fastapi
```

## Bước 1: Train model Iris

> Tương ứng: `scripts/train_model.py`

```bash
python scripts/train_model.py
```

**Kỳ vọng:** Tạo file `models/*.joblib`.

## Bước 2: Chạy API server

> Terminal riêng — giữ chạy nền

```bash
cd learn-python-ai/09-fastapi
source ../.venv/bin/activate
uvicorn app.main:app --reload --port 8000
```

## Bước 3: Kiểm tra health (terminal mới)

```bash
curl http://localhost:8000/health
```

**Kỳ vọng:** `{"status":"healthy",...}`

## Bước 4: Mở Swagger UI

```bash
open http://localhost:8000/docs
```

## Bước 5: Chạy client demo (tùy chọn)

> Tương ứng: `examples/client_demo.py` — cần API đang chạy ở bước 2

```bash
cd learn-python-ai/09-fastapi
source ../.venv/bin/activate
python examples/client_demo.py
```

## Bước 6: Chạy tests (tùy chọn)

```bash
cd learn-python-ai/09-fastapi
source ../.venv/bin/activate
pytest tests/ -v
```

## Bản đồ script ↔ manual

| Automation | Bước manual |
|------------|-------------|
| `scripts/train_model.py` | Bước 1 |
| `uvicorn app.main:app` (README) | Bước 2 |
| `examples/client_demo.py` | Bước 5 |
| `pytest tests/` | Bước 6 |

## Gỡ / dọn dẹp

```bash
# Dừng uvicorn: Ctrl+C ở terminal đang chạy server
```
