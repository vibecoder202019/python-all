# Hướng dẫn chạy Manual — Module 09: FastAPI

> Lệnh trích từ README + `scripts/train_model.py`. Không có `setup.sh` riêng.

## Phần 0 — Kiểm tra

```bash
python3 --version
lsof -i :8000 2>/dev/null || echo "port 8000 trống"
```

## Phần A — Cài đặt

```bash
cd learn-python-ai
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

**Kiểm tra sau cài đặt:**

```bash
python -c "import fastapi, uvicorn, sklearn; print('OK')"
uvicorn --version
```

## Phần B — Train model (`scripts/train_model.py`)

```bash
cd learn-python-ai/09-fastapi
source ../.venv/bin/activate
python scripts/train_model.py
```

**Kiểm tra:**

```bash
ls -la models/
python -c "import joblib; print(joblib.load('models/iris_model.joblib'))"
```

**Kỳ vọng:** Có `iris_model.joblib`, `iris_scaler.joblib`, `metadata.joblib`.

## Phần C — Chạy API server

```bash
cd learn-python-ai/09-fastapi
source ../.venv/bin/activate
uvicorn app.main:app --reload --port 8000
```

**Kiểm tra (terminal mới):**

```bash
curl -sf http://localhost:8000/health
curl -sf http://localhost:8000/docs -o /dev/null -w "%{http_code}\n"
```

## Phần D — Client demo + tests

```bash
cd learn-python-ai/09-fastapi
source ../.venv/bin/activate
python examples/client_demo.py
pytest tests/ -v
```

## Bản đồ script ↔ manual

| Script / file | Phần |
|---------------|------|
| `pip install -r requirements.txt` | A |
| `scripts/train_model.py` | B |
| `uvicorn app.main:app` | C |
| `examples/client_demo.py`, `pytest` | D |
