# Hướng dẫn chạy Manual — Module 08: Deep Learning

## Phần 0 — Kiểm tra

```bash
python3 --version
```

## Phần A — Cài đặt

```bash
cd learn-python-ai
source .venv/bin/activate 2>/dev/null || { python3 -m venv .venv && source .venv/bin/activate; }
pip install --upgrade pip
pip install tensorflow
```

**Kiểm tra:**

```bash
python -c "import tensorflow as tf; print(tf.__version__)"
```

## Phần B — Chạy ví dụ

```bash
cd learn-python-ai/08-deep-learning
python examples/01_neural_network_basics.py
python examples/02_mnist_classifier.py
```

**Kiểm tra:** Bước 2 có thể mất vài phút (tải MNIST + train).

## Bản đồ manual

| Nguồn | Manual |
|-------|--------|
| README — pip tensorflow | A |
| examples/ | B |
