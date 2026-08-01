# Hướng dẫn chạy Manual — Module 07: Machine Learning

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
python -c "import sklearn; print(sklearn.__version__)"
```

## Phần B — Chạy ví dụ

```bash
cd learn-python-ai/07-machine-learning
python examples/01_classification_iris.py
python examples/02_regression.py
python examples/03_cross_validation.py
python examples/04_save_load_model.py
```

**Kiểm tra bước 4:**

```bash
ls -la *.joblib models/ 2>/dev/null || ls -la
```

## Bản đồ manual

| Nguồn | Manual |
|-------|--------|
| requirements.txt | A |
| examples/ | B |
