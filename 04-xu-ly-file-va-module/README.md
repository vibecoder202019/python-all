# Module 04: Xử lý File & Module

## Mục tiêu

- Đọc/ghi file text, CSV, JSON
- Hiểu import và cấu trúc package
- Sử dụng `pathlib` thay cho `os.path`

---

## 1. Đọc/Ghi file Text

```python
# Ghi file
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Dòng 1\n")
    f.writelines(["Dòng 2\n", "Dòng 3\n"])

# Đọc file
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()       # toàn bộ
    lines = f.readlines()    # list các dòng
    for line in f:           # iterate từng dòng (tiết kiệm RAM)
        print(line.strip())
```

**`with` statement** — tự đóng file, kể cả khi có exception.

---

## 2. JSON

```python
import json

data = {"name": "Minh", "skills": ["Python", "ML"], "age": 25}

# Ghi JSON
with open("profile.json", "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Đọc JSON
with open("profile.json") as f:
    loaded = json.load(f)
```

---

## 3. CSV

```python
import csv

# Ghi CSV
rows = [
    ["name", "age", "city"],
    ["An", "25", "Hà Nội"],
    ["Bình", "30", "TP.HCM"],
]
with open("people.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# Đọc CSV
with open("people.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])
```

---

## 4. pathlib — Quản lý đường dẫn

```python
from pathlib import Path

base = Path("data")
base.mkdir(exist_ok=True)

file = base / "output" / "result.txt"
file.parent.mkdir(parents=True, exist_ok=True)

file.write_text("Hello", encoding="utf-8")
content = file.read_text(encoding="utf-8")

for p in base.glob("**/*.csv"):
    print(p.name, p.stat().st_size)
```

---

## 5. Import & Module

```
my_package/
├── __init__.py
├── utils.py
└── models/
    ├── __init__.py
    └── classifier.py
```

```python
# utils.py
def helper():
    return "help"

# main.py
from my_package.utils import helper
from my_package.models.classifier import MyModel

if __name__ == "__main__":
    print(helper())
```

**`if __name__ == "__main__"`** — code chỉ chạy khi file được execute trực tiếp, không khi import.

---

## Chạy ví dụ

```bash
python examples/01_file_io.py
python examples/02_json_csv.py
python examples/03_pathlib.py
```

## Bài tập

→ [exercises/bai_tap.md](exercises/bai_tap.md)

## Module tiếp theo

→ [Module 05: Thư viện Python](../05-thu-vien-python/README.md)
