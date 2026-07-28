"""
Module 02 — Ví dụ 2: Dict và Set
Chạy: python examples/02_dict_set.py

YÊU CẦU ĐỀ BÀI:
  - Truy cập dict lồng nhau, dùng get() với giá trị mặc định
  - Merge dict bằng toán tử | (Python 3.9+)
  - Phép toán set: union, intersection, difference
  - Loại bỏ phần tử trùng bằng set
  - Dict comprehension tính giá trị kho

KẾT QUẢ MONG ĐỢI (khi chạy):
  - Thông tin sinh viên và điểm Toán
  - Phone mặc định "Chưa có"
  - Union/intersection/difference của 2 set tags
  - Unique emails từ list có trùng
  - Dict giá trị kho: Laptop, Mouse, Keyboard
"""

# ── Dict ──
student = {
    "id": "SV001",
    "name": "Nguyễn Văn A",
    "scores": {"math": 85, "english": 90, "physics": 78},
}

print("=== Dict ===")
print(f"Tên: {student['name']}")
print(f"Điểm Toán: {student['scores']['math']}")
print(f"Phone (default): {student.get('phone', 'Chưa có')}")  # get tránh KeyError

for key, value in student.items():
    print(f"  {key}: {value}")

# ── Merge dicts (Python 3.9+) ──
defaults = {"city": "Hà Nội", "country": "VN"}
profile = defaults | student  # gộp, key trùng lấy bên phải
print(f"\nMerged keys: {list(profile.keys())}")

# ── Set ──
tags_a = {"python", "ml", "api", "fastapi"}
tags_b = {"python", "web", "django", "api"}

print(f"\n=== Set operations ===")
print(f"A: {tags_a}")
print(f"B: {tags_b}")
print(f"Union:        {tags_a | tags_b}")  # hợp
print(f"Intersection: {tags_a & tags_b}")  # giao
print(f"Difference:   {tags_a - tags_b}")  # hiệu A \ B

# ── Loại bỏ trùng ──
emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com"]
unique_emails = list(set(emails))  # set tự loại trùng
print(f"\nUnique emails: {unique_emails}")

# ── Dict comprehension ──
products = [
    {"name": "Laptop", "price": 15000000, "qty": 5},
    {"name": "Mouse", "price": 200000, "qty": 50},
    {"name": "Keyboard", "price": 800000, "qty": 20},
]
inventory_value = {p["name"]: p["price"] * p["qty"] for p in products}
print(f"\nGiá trị kho: {inventory_value}")
