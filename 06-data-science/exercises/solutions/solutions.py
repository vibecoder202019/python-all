"""Đáp án Module 06"""
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris


def matrix_stats(size: int = 5) -> dict:
    matrix = np.random.randint(1, 100, (size, size))
    return {
        "matrix": matrix,
        "row_sums": matrix.sum(axis=1),
        "col_sums": matrix.sum(axis=0),
        "total": matrix.sum(),
    }


def iris_eda() -> pd.DataFrame:
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["species"] = iris.target_names[iris.target]
    stats = df.groupby("species").agg(["mean", "std"])
    return stats


if __name__ == "__main__":
    stats = matrix_stats()
    print(f"Row sums: {stats['row_sums']}")
    print(f"Total: {stats['total']}")
    print(f"\nIris EDA:\n{iris_eda().round(2)}")
