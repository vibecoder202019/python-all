# Module 05: Thư viện Python Quan trọng

## Mục tiêu

- Gọi HTTP API với `requests`
- Xử lý datetime, regex, logging
- Hiểu virtual environment và pip

---

## 1. requests — HTTP Client

```python
import requests

# GET request
response = requests.get("https://api.github.com/users/python")
response.raise_for_status()  # raise nếu status >= 400
data = response.json()
print(data["name"], data["public_repos"])

# POST request
payload = {"name": "Minh", "email": "minh@example.com"}
response = requests.post("https://httpbin.org/post", json=payload)
print(response.status_code, response.json())

# Headers & params
response = requests.get(
    "https://api.example.com/search",
    params={"q": "python", "limit": 10},
    headers={"Authorization": "Bearer TOKEN"},
    timeout=30,
)
```

---

## 2. datetime

```python
from datetime import datetime, timedelta, timezone

now = datetime.now()
today = now.date()

# Format
now.strftime("%Y-%m-%d %H:%M:%S")  # "2024-01-15 10:30:00"
datetime.strptime("2024-01-15", "%Y-%m-%d")

# Tính toán
tomorrow = now + timedelta(days=1)
week_ago = now - timedelta(weeks=1)
diff = tomorrow - now
print(diff.total_seconds())
```

---

## 3. regex — Regular Expressions

```python
import re

text = "Email: minh@example.com, Phone: 0901234567"

# Tìm email
emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)

# Validate phone VN
phone_pattern = r"0\d{9}"
phones = re.findall(phone_pattern, text)

# Replace
cleaned = re.sub(r"\s+", " ", text.strip())
```

---

## 4. logging

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

logger.info("Application started")
logger.warning("Deprecated API used")
logger.error("Connection failed", exc_info=True)
```

---

## 5. os & sys

```python
import os
import sys

os.getenv("API_KEY", "default")
os.makedirs("data/output", exist_ok=True)
sys.path.insert(0, "src")  # thêm vào Python path
```

---

## Chạy ví dụ

```bash
python examples/01_requests.py
python examples/02_datetime_regex.py
python examples/03_logging.py
```

## Bài tập

→ [exercises/bai_tap.md](exercises/bai_tap.md)

## Module tiếp theo

→ [Module 06: Data Science](../06-data-science/README.md)
