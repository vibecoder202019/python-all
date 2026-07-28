# Module 02: Cấu trúc Dữ liệu

## Mục tiêu

- Nắm vững List, Tuple, Set, Dict
- Hiểu khi nào dùng cấu trúc nào
- Sử dụng collections (deque, Counter, defaultdict)

---

## 1. List — Danh sách có thể thay đổi

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("date")       # thêm cuối
fruits.insert(0, "apricot") # chèn vị trí
fruits.remove("banana")     # xóa theo giá trị
last = fruits.pop()         # xóa và trả phần tử cuối
fruits.sort()                 # sắp xếp tại chỗ
fruits.reverse()
len(fruits)
"apple" in fruits           # True
```

**Slice:** `lst[start:stop:step]`

---

## 2. Tuple — Bất biến (immutable)

```python
point = (3, 4)
x, y = point                # unpacking
# point[0] = 5              # ❌ Lỗi — không thể sửa

# Dùng khi: tọa độ, return nhiều giá trị, dict key
```

---

## 3. Set — Tập hợp không trùng lặp

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b   # union: {1,2,3,4,5,6}
a & b   # intersection: {3,4}
a - b   # difference: {1,2}
a ^ b   # symmetric diff: {1,2,5,6}

# Loại bỏ trùng lặp
unique = list(set([1, 2, 2, 3, 3, 3]))  # [1, 2, 3]
```

---

## 4. Dict — Ánh xạ key → value

```python
person = {"name": "Minh", "age": 25, "city": "Hà Nội"}

person["email"] = "minh@example.com"  # thêm/sửa
person.get("phone", "N/A")            # an toàn — không KeyError
del person["city"]

for key, value in person.items():
    print(f"{key}: {value}")

# Dict comprehension
squares = {x: x**2 for x in range(5)}
```

---

## 5. So sánh nhanh

| Cấu trúc | Mutable | Ordered | Duplicate | Use case |
|----------|---------|---------|-----------|----------|
| List | ✅ | ✅ | ✅ | Danh sách đơn hàng |
| Tuple | ❌ | ✅ | ✅ | Tọa độ, config |
| Set | ✅ | ❌ | ❌ | Unique IDs |
| Dict | ✅ | ✅* | Keys: ❌ | User profile |

*Dict giữ thứ tự insert từ Python 3.7+

---

## 6. Collections module

```python
from collections import deque, Counter, defaultdict

# deque — queue/stack hiệu quả
queue = deque([1, 2, 3])
queue.append(4)       # thêm cuối
queue.popleft()       # lấy đầu — O(1)

# Counter — đếm tần suất
words = ["apple", "banana", "apple", "cherry", "apple"]
Counter(words)  # Counter({'apple': 3, 'banana': 1, 'cherry': 1})

# defaultdict — giá trị mặc định
groups = defaultdict(list)
groups["team_a"].append("An")
groups["team_a"].append("Bình")
```

---

## 7. Algorithm cơ bản

### Linear Search — O(n)
```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
```

### Binary Search — O(log n) — cần mảng đã sort
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

---

## Chạy ví dụ

```bash
python examples/01_list_tuple.py
python examples/02_dict_set.py
python examples/03_collections.py
python examples/04_algorithms.py
```

---

## Giải thích chi tiết (Tự học)

### File `examples/01_list_tuple.py`

```python
sorted(numbers)        # Trả list MỚI đã sort — không đổi list gốc
numbers.append(5)      # Thêm 1 phần tử cuối
numbers.extend([7,8]) # Thêm nhiều phần tử (mở rộng list)
numbers[2:5]           # Slice: lấy index 2,3,4 (không lấy 5)
numbers[::-1]          # Đảo ngược — bước nhảy -1
```

```python
r, g, b = rgb          # Unpacking: gán 3 giá trị tuple vào 3 biến
list(zip(*matrix))     # zip ghép cột thành hàng → transpose ma trận
```

**List vs Tuple:** List `[...]` có thể sửa; Tuple `(...)` **bất biến** — dùng khi dữ liệu không đổi (tọa độ, config).

---

### File `examples/02_dict_set.py`

```python
student.get("phone", "N/A")   # An toàn — không KeyError nếu thiếu key
defaults | student            # Merge 2 dict (Python 3.9+)
tags_a | tags_b               # Union — hợp 2 set
tags_a & tags_b               # Intersection — phần tử chung
```

**Khi nào dùng gì:**
- **List** — thứ tự quan trọng, cho phép trùng
- **Dict** — tra cứu theo key (O(1))
- **Set** — loại trùng, phép toán tập hợp

---

### File `examples/03_collections.py`

```python
from collections import deque
queue.append(x)      # Thêm cuối
queue.popleft()      # Lấy đầu — O(1), nhanh hơn list.pop(0)
```

```python
Counter(text.split())           # Đếm tần suất từ
Counter(words).most_common(5)   # Top 5 từ xuất hiện nhiều nhất
```

```python
defaultdict(list)    # Key mới tự tạo list rỗng — tiện group-by
```

---

### File `examples/04_algorithms.py`

**Linear search** O(n): duyệt từng phần tử — đơn giản, chậm với mảng lớn.

**Binary search** O(log n): chia đôi mảng **đã sort** — nhanh hơn nhiều.

```python
mid = (left + right) // 2
if arr[mid] < target:
    left = mid + 1    # Tìm nửa phải
else:
    right = mid - 1   # Tìm nửa trái
```

**Two Sum** — dùng dict lưu `{giá_trị: index}` → tìm complement trong O(n).

---

## Bài tập

→ [exercises/bai_tap.md](exercises/bai_tap.md)

## Module tiếp theo

→ [Module 03: OOP](../03-oop/README.md)
