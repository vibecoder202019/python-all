# Hướng dẫn chạy Manual — Module 10: Dự án tổng hợp

> Copy từng lệnh và chạy **tuần tự**. Dùng thư mục `solution/` làm reference hoàn chỉnh.

## Điều kiện

- Hoàn thành Module 09
- Python 3.10+

## Bước 0: Vào solution reference

```bash
cd learn-python-ai/10-du-an-tong-hop/solution
source ../../.venv/bin/activate
pip install -r ../../requirements.txt
```

## Bước 1: Train model California Housing

> Tương ứng: `solution/scripts/train_model.py`

```bash
python scripts/train_model.py
```

**Kỳ vọng:** Tạo `models/*.joblib`.

## Bước 2: Chạy API

```bash
uvicorn app.main:app --reload --port 8000
```

## Bước 3: Test API (terminal mới)

```bash
curl http://localhost:8000/health
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features":[8.3,41.0,6.984127,1.023810,322.0,2.555556,78.9,37.88,-122.23]}'
```

## Bước 4: Chạy pytest

```bash
cd learn-python-ai/10-du-an-tong-hop/solution
source ../../.venv/bin/activate
pytest tests/ -v
```

## Bước 5: Tự làm bản của bạn (tùy chọn)

```bash
# Copy cấu trúc từ solution sang thư mục app/ riêng và làm theo README.md
cat ../README.md
```

## Bản đồ manual ↔ README

| Bước | Nội dung |
|------|----------|
| 1 | Train model |
| 2–4 | API + test end-to-end |
| 5 | Capstone tự implement |

## Gỡ / dọn dẹp

```bash
# Ctrl+C để dừng uvicorn
```
