"""Module 02 — Dict và Set"""

# --- Dict ---
student = {
    "id": "SV001",
    "name": "Nguyễn Văn A",
    "scores": {"math": 85, "english": 90, "physics": 78},
}

print("=== Dict ===")
print(f"Tên: {student['name']}")
print(f"Điểm Toán: {student['scores']['math']}")
print(f"Phone (default): {student.get('phone', 'Chưa có')}")

for key, value in student.items():
    print(f"  {key}: {value}")

# Merge dicts (Python 3.9+)
defaults = {"city": "Hà Nội", "country": "VN"}
profile = defaults | student
print(f"\nMerged keys: {list(profile.keys())}")

# --- Set ---
tags_a = {"python", "ml", "api", "fastapi"}
tags_b = {"python", "web", "django", "api"}

print(f"\n=== Set operations ===")
print(f"A: {tags_a}")
print(f"B: {tags_b}")
print(f"Union:        {tags_a | tags_b}")
print(f"Intersection: {tags_a & tags_b}")
print(f"Difference:   {tags_a - tags_b}")

# Loại bỏ trùng
emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com"]
unique_emails = list(set(emails))
print(f"\nUnique emails: {unique_emails}")

# --- Dict comprehension ---
products = [
    {"name": "Laptop", "price": 15000000, "qty": 5},
    {"name": "Mouse", "price": 200000, "qty": 50},
    {"name": "Keyboard", "price": 800000, "qty": 20},
]
inventory_value = {p["name"]: p["price"] * p["qty"] for p in products}
print(f"\nGiá trị kho: {inventory_value}")
