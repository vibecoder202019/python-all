# Module 01: Python Cơ bản

## Mục tiêu

Sau module này bạn sẽ:
- Hiểu cú pháp Python cơ bản
- Sử dụng biến, kiểu dữ liệu, toán tử
- Viết điều kiện và vòng lặp
- Định nghĩa và gọi hàm

---

## Lý thuyết nền tảng — Python là gì?

**Python** là ngôn ngữ lập trình bậc cao, đọc gần giống tiếng Anh/tiếng Việt tự nhiên. Mục tiêu thiết kế: *code dễ đọc hơn code dễ viết*.

**Ví von:** Nếu C/Java là "công thức nấu ăn chi tiết từng gram", Python là "nấu soup: cho thịt, rau, nước — xong". Bạn tập trung **logic**, không lo cú pháp rườm rà.

### Tại sao bắt đầu với Python?

| Lý do | Giải thích |
|-------|------------|
| Dễ học | Cú pháp ít, không cần `{}` hay khai báo kiểu |
| Đa dụng | Web, AI, automation, game, DevOps đều dùng được |
| Cộng đồng lớn | Hỏi Google/Stack Overflow luôn có đáp án |
| Thư viện phong phú | `pip install` là có sẵn công cụ mạnh |

### Biến — hộp đựng dữ liệu

Hãy tưởng tượng **biến = nhãn dán trên hộp**:
- `name = "Minh"` → hộp có nhãn `name`, bên trong là chữ "Minh"
- Gán lại `name = "Lan"` → thay nội dung hộp, nhãn vẫn là `name`

**Dynamically typed** nghĩa là Python tự biết hộp đang chứa số hay chữ — bạn không cần viết `int name` như C.

### Indentation — thụt lề bắt buộc

Python dùng **khoảng trắng đầu dòng** (thường 4 spaces) để nhóm code thuộc cùng block:

```python
if score >= 50:
    print("Đậu")      # Thuộc block if — phải thụt vào
    print("Chúc mừng")
print("Kết thúc")     # Ngoài block if — không thụt
```

Quên thụt lề → `IndentationError`. Đây là điểm khác biệt lớn nhất so với C/Java/JavaScript.

### Hàm — công thức tái sử dụng

Hàm giống **công thức nấu ăn**: định nghĩa 1 lần, gọi nhiều lần với nguyên liệu khác nhau.

```python
def tinh_diem_tb(a, b, c):
    return (a + b + c) / 3

# Gọi 3 lần — không lặp code
tb1 = tinh_diem_tb(8, 9, 7)
tb2 = tinh_diem_tb(6, 7, 8)
```

---

## 1. Biến và Kiểu dữ liệu

Python là **ngôn ngữ dynamically typed** — không cần khai báo kiểu khi gán biến.

| Kiểu | Ví dụ | Mô tả |
|------|-------|-------|
| `int` | `42`, `-7` | Số nguyên |
| `float` | `3.14`, `1e-5` | Số thực |
| `str` | `"hello"`, `'world'` | Chuỗi ký tự |
| `bool` | `True`, `False` | Boolean |
| `None` | `None` | Giá trị rỗng |

```python
name = "Minh"          # str
age = 25               # int
height = 1.75          # float
is_student = True      # bool
```

**Kiểm tra kiểu:** `type(x)` hoặc `isinstance(x, int)`

**Ép kiểu (casting):**
```python
int("42")      # → 42
float("3.14")  # → 3.14
str(100)       # → "100"
```

---

## 2. Toán tử

### Số học
```python
10 + 3   # 13
10 - 3   # 7
10 * 3   # 30
10 / 3   # 3.333... (luôn trả float)
10 // 3  # 3 (chia lấy phần nguyên)
10 % 3   # 1 (modulo — phần dư)
2 ** 10  # 1024 (lũy thừa)
```

### So sánh (trả về bool)
```python
5 == 5   # True
5 != 3   # True
5 > 3    # True
5 >= 5   # True
```

### Logic
```python
True and False  # False
True or False   # True
not True        # False
```

---

## 3. Chuỗi (String)

```python
s = "Hello, World!"
s.lower()           # "hello, world!"
s.upper()           # "HELLO, WORLD!"
s.split(", ")       # ["Hello", "World!"]
", ".join(["a","b"]) # "a, b"
s.replace("World", "Python")
len(s)              # 13
s[0]                # "H" (index bắt đầu từ 0)
s[-1]               # "!" (index âm — đếm từ cuối)
s[0:5]              # "Hello" (slice)
f"Tôi {age} tuổi"   # f-string (Python 3.6+)
```

---

## 4. Điều kiện (if / elif / else)

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

**Lưu ý:** Python dùng **indentation** (thụt lề 4 spaces) thay vì `{}`.

---

## 5. Vòng lặp

### for — lặp qua iterable
```python
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

### while — lặp khi điều kiện đúng
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### break & continue
```python
for i in range(10):
    if i == 3:
        continue   # bỏ qua lần lặp này
    if i == 7:
        break      # thoát vòng lặp
    print(i)
```

---

## 6. Hàm (Functions)

```python
def greet(name: str, greeting: str = "Xin chào") -> str:
    """Trả về lời chào — docstring mô tả hàm."""
    return f"{greeting}, {name}!"

result = greet("Minh")           # "Xin chào, Minh!"
result = greet("Minh", "Hi")     # "Hi, Minh!"
```

### *args và **kwargs
```python
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4)  # 10

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Minh", age=25)
```

### Lambda — hàm ẩn danh
```python
square = lambda x: x ** 2
square(5)  # 25

numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]
```

---

## 7. List Comprehension

Cách viết ngắn gọn để tạo list:

```python
# Cách thường
squares = []
for x in range(10):
    squares.append(x ** 2)

# List comprehension
squares = [x ** 2 for x in range(10)]

# Có điều kiện
evens = [x for x in range(20) if x % 2 == 0]
```

---

## 8. Exception Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Lỗi: {e}")
except Exception as e:
    print(f"Lỗi không xác định: {e}")
else:
    print("Không có lỗi")
finally:
    print("Luôn chạy — dùng để cleanup")
```

---

## Chạy ví dụ

```bash
python examples/01_bien_va_kieu_du_lieu.py
python examples/02_dieu_kien_va_vong_lap.py
python examples/03_ham_va_lambda.py
python examples/04_list_comprehension.py
```

---

## Câu hỏi thường gặp (FAQ)

**Q: Python 2 hay Python 3?**  
A: Luôn dùng **Python 3.10+**. Python 2 đã ngừng hỗ trợ từ 2020.

**Q: `==` và `=` khác nhau thế nào?**  
A: `=` gán giá trị; `==` so sánh bằng. `if x = 5` là **sai cú pháp**.

**Q: List comprehension có bắt buộc không?**  
A: Không, nhưng nên học — code ngắn, thường nhanh hơn vòng lặp thường.

**Q: Lỗi `NameError: name 'x' is not defined`?**  
A: Biến `x` chưa được gán trước khi dùng — kiểm tra tên biến và thứ tự code.

---

## Giải thích chi tiết (Tự học)

### Lệnh chạy ví dụ

```bash
python examples/01_bien_va_kieu_du_lieu.py
```

| Phần lệnh | Ý nghĩa |
|-----------|---------|
| `python` | Gọi trình thông dịch Python (cần Python 3.10+ trong PATH) |
| `examples/01_...py` | Đường dẫn file script — Python đọc và thực thi từ trên xuống |

**Cách đọc output:** Mỗi dòng `print()` in ra terminal. Nếu có lỗi, Python hiện `Traceback` — đọc dòng cuối để biết lỗi gì.

**Mẹo:** Chạy từ thư mục module (`01-python-co-ban/`), hoặc dùng đường dẫn đầy đủ từ root repo.

---

### File `examples/01_bien_va_kieu_du_lieu.py`

```python
name = "Nguyễn Văn A"      # Gán chuỗi vào biến name
age = 28                    # Số nguyên
salary = 15_000_000.50      # Dấu _ giúp đọc số dễ hơn, Python bỏ qua _
is_employed = True          # Boolean: đúng/sai
```

- `type(age)` → trả `"int"` — kiểm tra kiểu runtime
- `int("42")` → `"42"` là chuỗi, ép sang số `42`
- `f"Tên: {name}"` → **f-string**: chèn giá trị biến vào chuỗi

**Toán tử quan trọng:**
- `/` luôn cho kết quả float: `10 / 4 = 2.5`
- `//` chia lấy phần nguyên: `10 // 4 = 2`
- `%` phần dư: `10 % 4 = 2`

---

### File `examples/02_dieu_kien_va_vong_lap.py`

```python
def classify_score(score: int) -> str:
    if score >= 90:
        return "Xuất sắc"
    elif score >= 80:
        return "Giỏi"
    ...
```

- `def` định nghĩa hàm; `score: int` là **type hint** (gợi ý kiểu, không bắt buộc)
- `-> str` gợi ý hàm trả về chuỗi
- `elif` = "else if" — kiểm tra điều kiện tiếp nếu điều kiện trước sai

```python
for index, name in enumerate(students, start=1):
```

- `enumerate` trả cặp `(index, phần_tử)` — tiện khi cần cả số thứ tự và giá trị
- `start=1` đếm từ 1 thay vì 0

```python
while countdown > 0:
    countdown -= 1   # tương đương countdown = countdown - 1
```

- `while` lặp **đến khi** điều kiện False — cẩn thận vòng lặp vô hạn nếu quên giảm biến

---

### File `examples/03_ham_va_lambda.py`

```python
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    if height_m <= 0 or weight_kg <= 0:
        raise ValueError("...")
    return weight_kg / (height_m ** 2)
```

- `raise ValueError(...)` **chủ động ném lỗi** khi input không hợp lệ
- `** 2` = lũy thừa 2

```python
def sum_all(*numbers):   # *numbers nhận mọi tham số dư thành tuple
def build_profile(**info):  # **info nhận keyword args thành dict
```

```python
sorted(students, key=lambda s: s["score"], reverse=True)
```

- `lambda s: s["score"]` — hàm nhỏ không tên, trả điểm để sắp xếp
- `reverse=True` — sắp xếp giảm dần

---

### File `examples/04_list_comprehension.py`

```python
squares = [x ** 2 for x in range(1, 11)]
```

Tương đương vòng lặp:
```python
squares = []
for x in range(1, 11):
    squares.append(x ** 2)
```

```python
evens = [x for x in range(20) if x % 2 == 0]
```

- Phần `if` ở cuối = **lọc** — chỉ lấy phần tử thỏa điều kiện
- `x % 2 == 0` → số chia hết cho 2 (số chẵn)

**Dict/Set comprehension** — cùng cú pháp nhưng tạo `{}` thay vì `[]`.

---

## Bài tập

→ Xem [exercises/bai_tap.md](exercises/bai_tap.md)

## Module tiếp theo

→ [Module 02: Cấu trúc dữ liệu](../02-cau-truc-du-lieu/README.md)
