"""Module 02 — Collections module"""
from collections import deque, Counter, defaultdict, namedtuple

# --- deque: Queue & Stack ---
print("=== Queue (FIFO) ===")
queue = deque()
for item in ["task1", "task2", "task3"]:
    queue.append(item)
    print(f"  Enqueue: {item} → queue={list(queue)}")

while queue:
    task = queue.popleft()
    print(f"  Dequeue: {task} → queue={list(queue)}")

print("\n=== Stack (LIFO) ===")
stack = deque()
for page in ["home", "products", "detail"]:
    stack.append(page)
    print(f"  Push: {page}")

while stack:
    page = stack.pop()
    print(f"  Pop: {page} → back to {stack[-1] if stack else 'start'}")

# --- Counter ---
text = "machine learning is fun and machine learning is powerful"
word_count = Counter(text.split())
print(f"\n=== Word count ===")
for word, count in word_count.most_common(5):
    print(f"  '{word}': {count}")

# --- defaultdict ---
print("\n=== Group by department ===")
employees = [
    ("An", "Engineering"), ("Bình", "Sales"),
    ("Chi", "Engineering"), ("Dung", "Sales"), ("Em", "Engineering"),
]
by_dept = defaultdict(list)
for name, dept in employees:
    by_dept[dept].append(name)

for dept, members in by_dept.items():
    print(f"  {dept}: {members}")

# --- namedtuple ---
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(f"\n=== namedtuple ===")
print(f"Point: x={p.x}, y={p.y}, distance={((p.x**2 + p.y**2)**0.5):.2f}")
