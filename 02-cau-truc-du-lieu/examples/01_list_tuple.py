"""Module 02 — List và Tuple"""
from typing import Any

# --- List operations ---
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Gốc: {numbers}")
print(f"Sort: {sorted(numbers)}")
print(f"Max: {max(numbers)}, Min: {min(numbers)}, Sum: {sum(numbers)}")

numbers.append(5)
numbers.extend([7, 8])
print(f"Sau append/extend: {numbers}")

# Slice
print(f"[2:5]: {numbers[2:5]}")
print(f"[::-1]: {numbers[::-1]}")  # đảo ngược

# --- Tuple ---
rgb = (255, 128, 0)
r, g, b = rgb
print(f"\nRGB: R={r}, G={g}, B={b}")

# Tuple làm dict key
color_map = {(255, 0, 0): "red", (0, 255, 0): "green"}
print(f"Màu (255,0,0): {color_map[(255, 0, 0)]}")

# Return nhiều giá trị
def min_max(numbers: list) -> tuple:
    return min(numbers), max(numbers)

lo, hi = min_max([3, 1, 4, 1, 5])
print(f"Min={lo}, Max={hi}")

# --- List of lists (matrix) ---
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"\nMa trận:")
for row in matrix:
    print(f"  {row}")

transposed = list(zip(*matrix))
print(f"Transpose: {transposed}")
