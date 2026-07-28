"""Module 06 — NumPy basics"""
import numpy as np

print("=== Tạo mảng ===")
arr1d = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"1D: {arr1d}, shape={arr1d.shape}")
print(f"2D:\n{matrix}")

print("\n=== Vectorized operations ===")
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
print(f"a + b = {a + b}")
print(f"a * 2 = {a * 2}")
print(f"sqrt(a) = {np.sqrt(a)}")

print("\n=== Statistics ===")
data = np.random.randn(1000)
print(f"Mean: {data.mean():.4f}")
print(f"Std:  {data.std():.4f}")
print(f"Min:  {data.min():.4f}, Max: {data.max():.4f}")

print("\n=== Matrix operations ===")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(f"A @ B =\n{A @ B}")
print(f"Det(A) = {np.linalg.det(A):.2f}")

print("\n=== Boolean indexing ===")
scores = np.array([85, 92, 78, 95, 60, 88, 73, 91])
passed = scores[scores >= 70]
print(f"Scores: {scores}")
print(f"Passed (>=70): {passed}")

print("\n=== Broadcasting ===")
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row = np.array([10, 20, 30])
print(f"Matrix + row (broadcasting):\n{matrix + row}")
