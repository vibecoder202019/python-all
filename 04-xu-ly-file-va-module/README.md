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

---

## Giải thích chi tiết (Tự học)

### File `examples/01_file_io.py`

```python
with open(filepath, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
```

| Thành phần | Ý nghĩa |
|-----------|---------|
| `with open(...) as f` | Mở file, **tự đóng** khi ra khỏi block — kể cả khi lỗi |
| `"w"` | Write — ghi đè; `"a"` append; `"r"` read |
| `encoding="utf-8"` | Hỗ trợ tiếng Việt và emoji |

```python
for line in f:              # Đọc từng dòng — tiết kiệm RAM với file lớn
    print(line.strip())     # strip() bỏ \n và khoảng trắng đầu/cuối
```

---

### File `examples/02_json_csv.py`

```python
json.dump(data, f, indent=2, ensure_ascii=False)
```

- `dump` — Python dict → file JSON
- `ensure_ascii=False` — giữ tiếng Việt (không escape thành `\uXXXX`)
- `load` — file JSON → Python dict

```python
writer = csv.DictWriter(f, fieldnames=students[0].keys())
writer.writeheader()
writer.writerows(students)
```

- Mỗi dict = 1 dòng CSV; key = tên cột
- `DictReader` đọc ngược — mỗi dòng thành dict

---

### File `examples/03_pathlib.py`

```python
from pathlib import Path
base = Path(__file__).parent / "data"
```

- `Path` thay cho chuỗi đường dẫn — `/` nối path cross-platform
- `__file__` = đường dẫn file script hiện tại
- `.mkdir(exist_ok=True)` — tạo thư mục, không lỗi nếu đã tồn tại
- `.read_text()` / `.write_text()` — đọc/ghi file ngắn gọn

```python
for p in base.rglob("*"):   # Duyệt đệ quy mọi file
    p.stat().st_size        # Kích thước bytes
```

---

### `if __name__ == "__main__"`

```python
if __name__ == "__main__":
    main()
```

- Khi chạy trực tiếp: `__name__ == "__main__"` → chạy `main()`
- Khi import module: `__name__ == "tên_module"` → **không** chạy — tránh side effect

---

## Bài tập

→ [exercises/bai_tap.md](exercises/bai_tap.md)

## Module tiếp theo

→ [Module 05: Thư viện Python](../05-thu-vien-python/README.md)
