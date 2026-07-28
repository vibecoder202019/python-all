"""
Module 01 — Ví dụ 3: Hàm và Lambda
Chạy: python examples/03_ham_va_lambda.py
"""
from typing import Optional


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Tính chỉ số BMI = cân nặng / chiều cao²."""
    if height_m <= 0 or weight_kg <= 0:
        raise ValueError("Cân nặng và chiều cao phải > 0")
    return weight_kg / (height_m ** 2)


def bmi_category(bmi: float) -> str:
    """Phân loại BMI theo WHO."""
    if bmi < 18.5:
        return "Thiếu cân"
    elif bmi < 25:
        return "Bình thường"
    elif bmi < 30:
        return "Thừa cân"
    return "Béo phì"


def sum_all(*numbers: float) -> float:
    """Tính tổng số lượng tùy ý tham số."""
    return sum(numbers)


def build_profile(**info) -> dict:
    """Tạo profile từ keyword arguments."""
    return info


# --- Demo ---
print("=== BMI Calculator ===")
people = [
    ("An", 65, 1.70),
    ("Bình", 80, 1.75),
    ("Chi", 55, 1.60),
]

for name, weight, height in people:
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    print(f"  {name}: BMI={bmi:.1f} → {category}")

print(f"\n=== *args: sum_all(1,2,3,4,5) = {sum_all(1, 2, 3, 4, 5)} ===")

profile = build_profile(name="Minh", age=25, city="Hà Nội")
print(f"=== **kwargs: {profile} ===")

# --- Lambda ---
print("\n=== Lambda & map/filter ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = list(map(lambda x: x ** 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(f"  Gốc:    {numbers}")
print(f"  Bình phương: {squares}")
print(f"  Chẵn:   {evens}")

# Lambda trong sorted
students = [
    {"name": "An", "score": 85},
    {"name": "Bình", "score": 92},
    {"name": "Chi", "score": 78},
]
sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)
print(f"\n=== Sắp xếp theo điểm ===")
for s in sorted_students:
    print(f"  {s['name']}: {s['score']}")
