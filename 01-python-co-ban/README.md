# Module 01: Python Cơ bản

## Mục tiêu

Sau module này bạn sẽ:
- Hiểu cú pháp Python cơ bản
- Sử dụng biến, kiểu dữ liệu, toán tử
- Viết điều kiện và vòng lặp
- Định nghĩa và gọi hàm

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

## Bài tập

→ Xem [exercises/bai_tap.md](exercises/bai_tap.md)

## Module tiếp theo

→ [Module 02: Cấu trúc dữ liệu](../02-cau-truc-du-lieu/README.md)
