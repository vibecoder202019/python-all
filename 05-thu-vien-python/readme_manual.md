# Hướng dẫn chạy Manual — Module 05: Thư viện Python

## Phần 0 — Kiểm tra

```bash
python3 --version
curl --version
```

**Kiểm tra mạng:**

```bash
curl -sf -o /dev/null -w "%{http_code}\n" https://httpbin.org/get
```

**Kỳ vọng:** `200`.

## Phần A — Cài đặt

```bash
cd learn-python-ai
source .venv/bin/activate 2>/dev/null || { python3 -m venv .venv && source .venv/bin/activate; }
pip install --upgrade pip
pip install requests
```

**Kiểm tra:**

```bash
python -c "import requests; print(requests.__version__)"
```

## Phần B — Chạy ví dụ

```bash
cd learn-python-ai/05-thu-vien-python
python examples/01_requests.py
python examples/02_datetime_regex.py
python examples/03_logging.py
```

## Bản đồ manual

| Script | Manual |
|--------|--------|
| *(không có)* | A (pip requests) + B |
