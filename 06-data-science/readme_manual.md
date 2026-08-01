# Hướng dẫn chạy Manual — Module 06: Data Science

## Phần 0 — Kiểm tra

```bash
python3 --version
```

## Phần A — Cài đặt (tương đương `pip install -r requirements.txt`)

```bash
cd learn-python-ai
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

**Kiểm tra sau cài đặt:**

```bash
python -c "import numpy, pandas, matplotlib; print('numpy', numpy.__version__)"
```

## Phần B — Chạy ví dụ

```bash
cd learn-python-ai/06-data-science
python examples/01_numpy_basics.py
python examples/02_pandas_basics.py
python examples/03_visualization.py
```

**Kiểm tra:** Exit code 0; bước 3 có thể mở cửa sổ plot hoặc lưu ảnh.

## Bản đồ manual

| Nguồn | Manual |
|-------|--------|
| `README.md` — pip requirements | Phần A |
| `examples/` | Phần B |
