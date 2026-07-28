# Module 03: Lập trình Hướng đối tượng (OOP)

## Mục tiêu

- Hiểu Class, Object, Instance
- Sử dụng Inheritance, Encapsulation, Polymorphism
- Biết magic methods và khi nào dùng OOP

---

## Lý thuyết nền tảng — OOP là gì?

**OOP (Lập trình hướng đối tượng)** mô hình hóa thế giới thật bằng **object** (đối tượng):

```
Class (khuôn)     →  Object (sản phẩm)
─────────────────────────────────────
Class Dog         →  dog1 = Dog("Buddy")
Class BankAccount →  acc = BankAccount("Minh", 1000000)
Class User        →  user = User("admin", role="admin")
```

### 4 trụ cột OOP

| Trụ cột | Ý nghĩa đơn giản | Ví dụ |
|---------|------------------|-------|
| **Encapsulation** | Giấu chi tiết bên trong, chỉ lộ interface | `_balance` private, truy cập qua `.deposit()` |
| **Inheritance** | Class con kế thừa class cha | `Dog(Animal)` — Dog có method của Animal |
| **Polymorphism** | Cùng method, hành vi khác nhau | `animal.speak()` — chó sủa, mèo kêu |
| **Abstraction** | Chỉ định nghĩa "cái gì", không "làm thế nào" | `Shape.area()` — mỗi hình tính khác nhau |

### Khi nào dùng OOP?

✅ **Nên dùng:** Model phức tạp (User, Order, ML Model), code cần mở rộng  
❌ **Không cần:** Script 20 dòng xử lý file — function đủ rồi

### Class variable vs Instance variable

```python
class Student:
    school = "AI Academy"   # CHUNG — mọi student cùng trường
    def __init__(self, name):
        self.name = name    # RIÊNG — mỗi student tên khác
```

---

## 1. Class và Object

```python
class Dog:
    species = "Canis familiaris"  # class variable — dùng chung

    def __init__(self, name: str, age: int):
        self.name = name          # instance variable
        self.age = age

    def bark(self) -> str:
        return f"{self.name} says Woof!"

    def __str__(self) -> str:
        return f"Dog(name={self.name}, age={self.age})"

dog = Dog("Buddy", 3)
print(dog.bark())   # Buddy says Woof!
print(dog)          # Dog(name=Buddy, age=3)
```

**`__init__`** — constructor, gọi khi tạo object  
**`self`** — tham chiếu đến instance hiện tại

---

## 2. Encapsulation — Đóng gói

```python
class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self._balance = balance       # protected (convention)
        self.__pin = "1234"           # private (name mangling)

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Số tiền phải > 0")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise ValueError("Số dư không đủ")
        self._balance -= amount
```

**Quy ước:**
- `public` — không prefix
- `_protected` — một dấu `_`
- `__private` — hai dấu `__` (name mangling)

---

## 3. Inheritance — Kế thừa

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError("Subclass phải implement")

class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says Meow!"

class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says Woof!"
```

**`super()`** — gọi method của class cha:
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
```

---

## 4. Polymorphism — Đa hình

```python
def animal_sound(animal: Animal):
    print(animal.speak())

animals = [Cat("Mimi"), Dog("Rex"), Cat("Luna")]
for a in animals:
    animal_sound(a)  # mỗi loại speak khác nhau
```

---

## 5. Magic Methods (Dunder)

| Method | Mô tả | Ví dụ |
|--------|-------|-------|
| `__init__` | Constructor | `obj = Class()` |
| `__str__` | String đẹp (print) | `print(obj)` |
| `__repr__` | String debug | `repr(obj)` |
| `__len__` | len(obj) | `len(my_list)` |
| `__eq__` | So sánh == | `a == b` |
| `__add__` | Toán tử + | `a + b` |
| `__getitem__` | Indexing | `obj[0]` |

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)
```

---

## 6. Static & Class Methods

```python
class MathUtils:
    PI = 3.14159

    @staticmethod
    def circle_area(radius: float) -> float:
        return MathUtils.PI * radius ** 2

    @classmethod
    def from_diameter(cls, diameter: float) -> "Circle":
        return cls(diameter / 2)
```

---

## 7. Abstract Base Class

```python
from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def train(self, X, y): ...
    @abstractmethod
    def predict(self, X): ...

class LinearModel(Model):
    def train(self, X, y):
        # implementation
        pass
    def predict(self, X):
        pass
```

> Pattern này rất quan trọng trong ML — mọi model đều có `fit()` và `predict()`.

---

## Chạy ví dụ

```bash
python examples/01_class_basics.py
python examples/02_inheritance.py
python examples/03_magic_methods.py
```

---

## Giải thích chi tiết (Tự học)

### File `examples/01_class_basics.py`

```python
class Student:
    school = "AI Academy"    # Class variable — CHUNG cho mọi instance

    def __init__(self, name, student_id, gpa=0.0):
        self.name = name           # Instance variable — riêng từng object
        self._gpa = gpa            # _ = protected (quy ước, không ép buộc)
```

```python
@property
def gpa(self):
    return self._gpa

@gpa.setter
def gpa(self, value):
    if not 0 <= value <= 4.0:
        raise ValueError(...)
    self._gpa = value
```

- `@property` — truy cập như attribute (`student.gpa`) nhưng chạy method
- `@gpa.setter` — kiểm soát giá trị khi gán (`student.gpa = 3.8`)

**`self`** — tham chiếu đến chính object đang được tạo/gọi method.

---

### File `examples/02_inheritance.py`

```python
class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...
```

- `ABC` = Abstract Base Class — **bắt buộc** class con implement method abstract
- Không thể tạo `Shape()` trực tiếp — phải tạo `Rectangle`, `Circle`

```python
def print_shape_info(shape: Shape):
    print(shape.area())
```

**Polymorphism:** Hàm nhận `Shape` nhưng chạy đúng `area()` của Rectangle hay Circle tùy object thực tế.

---

### File `examples/03_magic_methods.py`

| Gọi code | Magic method thực thi |
|----------|----------------------|
| `v1 + v2` | `__add__` |
| `v1 == v2` | `__eq__` |
| `len(cart)` | `__len__` |
| `cart[0]` | `__getitem__` |
| `print(cart)` | `__str__` |

```python
def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)
```

Cho phép dùng toán tử `+` tự nhiên thay vì `v1.add(v2)`.

---

## Câu hỏi thường gặp (FAQ)

**Q: OOP có bắt buộc trong Python không?**  
A: Không. Python hỗ trợ cả procedural và OOP — dùng khi model phức tạp.

**Q: `_private` và `__private` khác gì?**  
A: `_` = quy ước "đừng dùng từ ngoài". `__` = name mangling, khó truy cập hơn.

**Q: Khi nào dùng `@staticmethod`?**  
A: Hàm liên quan class nhưng không cần `self` — vd: utility `circle_area(r)`.

---

## Bài tập

→ [exercises/bai_tap.md](exercises/bai_tap.md)

## Module tiếp theo

→ [Module 04: File I/O](../04-xu-ly-file-va-module/README.md)
