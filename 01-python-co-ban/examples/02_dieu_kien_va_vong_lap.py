"""
Module 01 — Ví dụ 2: Điều kiện và Vòng lặp
Chạy: python examples/02_dieu_kien_va_vong_lap.py
"""


def classify_score(score: int) -> str:
    """Phân loại điểm thi."""
    if score >= 90:
        return "Xuất sắc"
    elif score >= 80:
        return "Giỏi"
    elif score >= 65:
        return "Khá"
    elif score >= 50:
        return "Trung bình"
    else:
        return "Yếu"


# --- if/elif/else ---
scores = [95, 82, 70, 55, 40]
print("=== Phân loại điểm ===")
for s in scores:
    print(f"  Điểm {s:3d} → {classify_score(s)}")

# --- for với range ---
print("\n=== Bảng cửu chương 5 ===")
for i in range(1, 11):
    print(f"  5 x {i:2d} = {5 * i}")

# --- enumerate ---
students = ["An", "Bình", "Chi", "Dung"]
print("\n=== Danh sách sinh viên ===")
for index, name in enumerate(students, start=1):
    print(f"  {index}. {name}")

# --- while ---
print("\n=== Đếm ngược ===")
countdown = 5
while countdown > 0:
    print(f"  {countdown}...")
    countdown -= 1
print("  Bắt đầu!")

# --- break & continue ---
print("\n=== Số lẻ từ 1-10 (bỏ qua 5) ===")
for n in range(1, 11):
    if n == 5:
        continue
    if n % 2 == 0:
        continue
    print(f"  {n}", end=" ")
print()

# --- Nested loop — ma trận 3x3 ---
print("\n=== Ma trận 3x3 ===")
for row in range(3):
    for col in range(3):
        print(f"  ({row},{col})", end="")
    print()
