"""
Module 02 — Ví dụ 1: List và Tuple
Chạy: python examples/01_list_tuple.py

YÊU CẦU ĐỀ BÀI:
  - Thao tác list: sort, max, min, sum, append, extend, slice
  - Tuple: unpacking, dùng làm dict key, return nhiều giá trị
  - List of lists (ma trận) và transpose bằng zip(*matrix)

KẾT QUẢ MONG ĐỢI (khi chạy):
  - In list gốc, sorted, max/min/sum
  - List sau append/extend và các slice [2:5], [::-1]
  - RGB unpacking: R=255, G=128, B=0
  - Min=1, Max=5 từ min_max()
  - Ma trận 3x3 và transpose
"""
from typing import Any

# ── Thao tác List ──
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Gốc: {numbers}")
print(f"Sort: {sorted(numbers)}")
print(f"Max: {max(numbers)}, Min: {min(numbers)}, Sum: {sum(numbers)}")

numbers.append(5)
numbers.extend([7, 8])  # thêm nhiều phần tử cùng lúc
print(f"Sau append/extend: {numbers}")

# ── Slice ──
print(f"[2:5]: {numbers[2:5]}")
print(f"[::-1]: {numbers[::-1]}")  # đảo ngược toàn bộ list

# ── Tuple ──
rgb = (255, 128, 0)
r, g, b = rgb  # unpacking: gán từng phần tử vào biến
print(f"\nRGB: R={r}, G={g}, B={b}")

# Tuple làm dict key (list không được vì mutable)
color_map = {(255, 0, 0): "red", (0, 255, 0): "green"}
print(f"Màu (255,0,0): {color_map[(255, 0, 0)]}")

# ── Return nhiều giá trị ──
def min_max(numbers: list) -> tuple:
    return min(numbers), max(numbers)

lo, hi = min_max([3, 1, 4, 1, 5])
print(f"Min={lo}, Max={hi}")

# ── List of lists (ma trận) ──
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"\nMa trận:")
for row in matrix:
    print(f"  {row}")

transposed = list(zip(*matrix))  # zip(*) hoán vị hàng ↔ cột
print(f"Transpose: {transposed}")
