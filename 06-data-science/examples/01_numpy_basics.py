"""
Module 06 — Ví dụ 1: NumPy cơ bản
Chạy: python examples/01_numpy_basics.py

YÊU CẦU ĐỀ BÀI:
  - Tạo mảng 1D và ma trận 2D bằng np.array
  - Thực hiện phép toán vectorized (cộng, nhân, sqrt)
  - Tính thống kê: mean, std, min, max
  - Nhân ma trận, tính định thức, boolean indexing, broadcasting

KẾT QUẢ MONG ĐỢI (khi chạy):
  - In shape và nội dung mảng 1D, ma trận 2D
  - In kết quả phép toán vectorized
  - In thống kê mẫu ngẫu nhiên 1000 phần tử
  - In ma trận tích A @ B và det(A)
  - In điểm đạt (>= 70) và demo broadcasting
"""

import numpy as np

# ── Tạo mảng ──
print("=== Tạo mảng ===")
arr1d = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"1D: {arr1d}, shape={arr1d.shape}")
print(f"2D:\n{matrix}")

# ── Phép toán vectorized — áp dụng cho từng phần tử, không cần vòng lặp ──
print("\n=== Vectorized operations ===")
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
print(f"a + b = {a + b}")
print(f"a * 2 = {a * 2}")
print(f"sqrt(a) = {np.sqrt(a)}")

# ── Thống kê ──
print("\n=== Statistics ===")
data = np.random.randn(1000)  # phân phối chuẩn N(0, 1)
print(f"Mean: {data.mean():.4f}")
print(f"Std:  {data.std():.4f}")
print(f"Min:  {data.min():.4f}, Max: {data.max():.4f}")

# ── Phép toán ma trận ──
print("\n=== Matrix operations ===")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(f"A @ B =\n{A @ B}")  # @ là toán tử nhân ma trận
print(f"Det(A) = {np.linalg.det(A):.2f}")

# ── Boolean indexing — lọc phần tử theo điều kiện ──
print("\n=== Boolean indexing ===")
scores = np.array([85, 92, 78, 95, 60, 88, 73, 91])
passed = scores[scores >= 70]  # chỉ lấy phần tử >= 70
print(f"Scores: {scores}")
print(f"Passed (>=70): {passed}")

# ── Broadcasting — tự động mở rộng shape để tính toán ──
print("\n=== Broadcasting ===")
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row = np.array([10, 20, 30])  # (3,) broadcast thành (3,3)
print(f"Matrix + row (broadcasting):\n{matrix + row}")
