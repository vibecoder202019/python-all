"""
Module 06 — Ví dụ 2: Pandas cơ bản
Chạy: python examples/02_pandas_basics.py

YÊU CẦU ĐỀ BÀI:
  - Tạo DataFrame từ dict, xem head/describe
  - Lọc dữ liệu theo điều kiện (filter)
  - Nhóm theo department và tính aggregate (groupby)
  - Sắp xếp, xếp hạng và thêm cột tính toán

KẾT QUẢ MONG ĐỢI (khi chạy):
  - In 5 dòng đầu, shape và thống kê mô tả
  - In danh sách nhân viên Engineering và high performers
  - In bảng thống kê theo department
  - In top 3 lương cao nhất và bảng salary_rank
"""

import pandas as pd
import numpy as np

# ── Tạo DataFrame mẫu ──
np.random.seed(42)  # seed cố định để kết quả tái lập được
df = pd.DataFrame({
    "name": ["An", "Bình", "Chi", "Dung", "Em", "Phương", "Giang", "Hà"],
    "department": ["Engineering", "Sales", "Engineering", "Sales",
                   "Engineering", "Marketing", "Marketing", "Engineering"],
    "age": [28, 35, 26, 42, 31, 29, 33, 27],
    "salary": [25_000_000, 18_000_000, 22_000_000, 20_000_000,
               30_000_000, 15_000_000, 17_000_000, 24_000_000],
    "performance": [4.2, 3.8, 4.5, 3.5, 4.8, 3.2, 3.9, 4.1],
})

# ── Tổng quan DataFrame ──
print("=== DataFrame Overview ===")
print(df.head())
print(f"\nShape: {df.shape}")
print(f"\n{df.describe().round(2)}")

# ── Lọc & chọn cột ──
print("\n=== Filter & Select ===")
eng = df[df["department"] == "Engineering"]  # boolean mask lọc hàng
high_perf = df[df["performance"] >= 4.0]
print(f"Engineering ({len(eng)}): {eng['name'].tolist()}")
print(f"High performers: {high_perf['name'].tolist()}")

# ── Groupby — nhóm theo cột rồi aggregate ──
print("\n=== Groupby ===")
dept_stats = df.groupby("department").agg(
    count=("name", "count"),
    avg_salary=("salary", "mean"),
    avg_age=("age", "mean"),
    avg_perf=("performance", "mean"),
).round(0)
print(dept_stats)

# ── Sắp xếp & xếp hạng ──
print("\n=== Sort & Rank ===")
top_earners = df.nlargest(3, "salary")[["name", "salary", "department"]]
print(f"\nTop 3 earners:\n{top_earners.to_string(index=False)}")

# ── Thêm cột tính toán ──
print("\n=== Add computed column ===")
df["salary_rank"] = df["salary"].rank(ascending=False, method="min").astype(int)
print(df[["name", "salary", "salary_rank"]].sort_values("salary_rank"))
