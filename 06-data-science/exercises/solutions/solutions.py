"""
Module 06 — Đáp án bài tập
Chạy: python exercises/solutions/solutions.py

YÊU CẦU ĐỀ BÀI:
  - Viết hàm matrix_stats: tạo ma trận ngẫu nhiên và tính tổng theo hàng/cột
  - Viết hàm iris_eda: load Iris dataset, groupby species, tính mean và std

KẾT QUẢ MONG ĐỢI (khi chạy):
  - In row sums và total của ma trận ngẫu nhiên 5x5
  - In bảng thống kê mean/std theo species của Iris
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris


# ── Bài 1: Thống kê ma trận NumPy ──
def matrix_stats(size: int = 5) -> dict:
    """Tạo ma trận ngẫu nhiên và tính thống kê tổng."""
    matrix = np.random.randint(1, 100, (size, size))
    return {
        "matrix": matrix,
        "row_sums": matrix.sum(axis=1),  # tổng theo hàng (axis=1)
        "col_sums": matrix.sum(axis=0),  # tổng theo cột (axis=0)
        "total": matrix.sum(),
    }


# ── Bài 2: EDA dataset Iris ──
def iris_eda() -> pd.DataFrame:
    """Phân tích khám phá dữ liệu Iris — mean/std theo loài."""
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["species"] = iris.target_names[iris.target]  # chuyển mã số → tên loài
    stats = df.groupby("species").agg(["mean", "std"])
    return stats


if __name__ == "__main__":
    stats = matrix_stats()
    print(f"Row sums: {stats['row_sums']}")
    print(f"Total: {stats['total']}")
    print(f"\nIris EDA:\n{iris_eda().round(2)}")
