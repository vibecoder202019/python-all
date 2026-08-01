# Hướng dẫn chạy Manual — Module 10: Dự án tổng hợp

> Cài đặt giống Module 09; train qua `solution/scripts/train_model.py`.

## Phần 0 — Kiểm tra

```bash
python3 --version
```

## Phần A — Cài đặt

```bash
cd learn-python-ai
source .venv/bin/activate 2>/dev/null || { python3 -m venv .venv && source .venv/bin/activate; }
pip install --upgrade pip
pip install -r requirements.txt
```

**Kiểm tra:**

```bash
python -c "import fastapi, sklearn; print('OK')"
```

## Phần B — Train (`solution/scripts/train_model.py`)

```bash
cd learn-python-ai/10-du-an-tong-hop/solution
source ../../.venv/bin/activate
python scripts/train_model.py
```

**Kiểm tra:**

```bash
ls -la models/
```

## Phần C — Chạy API

```bash
cd learn-python-ai/10-du-an-tong-hop/solution
source ../../.venv/bin/activate
uvicorn app.main:app --reload --port 8000
```

**Kiểm tra:**

```bash
curl -sf http://localhost:8000/health
curl -sf -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features":[8.3,41.0,6.984127,1.023810,322.0,2.555556,78.9,37.88,-122.23]}'
```

## Phần D — Tests

```bash
cd learn-python-ai/10-du-an-tong-hop/solution
source ../../.venv/bin/activate
pytest tests/ -v
```

## Bản đồ manual

| File | Phần |
|------|------|
| `solution/scripts/train_model.py` | B |
| `uvicorn` | C |
| `pytest tests/` | D |
