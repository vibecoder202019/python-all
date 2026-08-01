# Hướng dẫn chạy Manual — Module 07: Machine Learning

> Copy từng lệnh và chạy **tuần tự**. Module này **không có script automation**.

## Bước 0: Cài dependencies

```bash
cd learn-python-ai
source .venv/bin/activate
pip install -r requirements.txt
```

## Bước 1: Classification (Iris)

```bash
cd 07-machine-learning
python examples/01_classification_iris.py
```

## Bước 2: Regression

```bash
python examples/02_regression.py
```

## Bước 3: Cross-validation

```bash
python examples/03_cross_validation.py
```

## Bước 4: Lưu/tải model

```bash
python examples/04_save_load_model.py
```

**Kỳ vọng:** Tạo file model trong thư mục làm việc (thường `models/` hoặc `.joblib`).

## Bản đồ manual ↔ README

| Bước | File |
|------|------|
| 1 | `01_classification_iris.py` |
| 2 | `02_regression.py` |
| 3 | `03_cross_validation.py` |
| 4 | `04_save_load_model.py` |
