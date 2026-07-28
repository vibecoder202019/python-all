"""
Module 02 — Ví dụ 3: Module Collections
Chạy: python examples/03_collections.py

YÊU CẦU ĐỀ BÀI:
  - deque: mô phỏng Queue (FIFO) và Stack (LIFO)
  - Counter: đếm tần suất từ, lấy top N phổ biến
  - defaultdict: nhóm phần tử theo key tự động
  - namedtuple: struct nhẹ với truy cập theo tên thuộc tính

KẾT QUẢ MONG ĐỢI (khi chạy):
  - Enqueue/dequeue 3 task theo thứ tự FIFO
  - Push/pop 3 trang theo thứ tự LIFO
  - Top 5 từ xuất hiện nhiều nhất
  - Nhóm nhân viên theo phòng ban
  - Point(3,4) với khoảng cách ≈ 5.00
"""
from collections import deque, Counter, defaultdict, namedtuple

# ── deque: Queue (FIFO) ──
print("=== Queue (FIFO) ===")
queue = deque()
for item in ["task1", "task2", "task3"]:
    queue.append(item)  # thêm vào cuối
    print(f"  Enqueue: {item} → queue={list(queue)}")

while queue:
    task = queue.popleft()  # lấy từ đầu (First In First Out)
    print(f"  Dequeue: {task} → queue={list(queue)}")

# ── deque: Stack (LIFO) ──
print("\n=== Stack (LIFO) ===")
stack = deque()
for page in ["home", "products", "detail"]:
    stack.append(page)
    print(f"  Push: {page}")

while stack:
    page = stack.pop()  # lấy từ cuối (Last In First Out)
    print(f"  Pop: {page} → back to {stack[-1] if stack else 'start'}")

# ── Counter ──
text = "machine learning is fun and machine learning is powerful"
word_count = Counter(text.split())
print(f"\n=== Word count ===")
for word, count in word_count.most_common(5):  # top 5 từ phổ biến
    print(f"  '{word}': {count}")

# ── defaultdict ──
print("\n=== Group by department ===")
employees = [
    ("An", "Engineering"), ("Bình", "Sales"),
    ("Chi", "Engineering"), ("Dung", "Sales"), ("Em", "Engineering"),
]
by_dept = defaultdict(list)  # key mới tự tạo list rỗng
for name, dept in employees:
    by_dept[dept].append(name)

for dept, members in by_dept.items():
    print(f"  {dept}: {members}")

# ── namedtuple ──
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(f"\n=== namedtuple ===")
print(f"Point: x={p.x}, y={p.y}, distance={((p.x**2 + p.y**2)**0.5):.2f}")
