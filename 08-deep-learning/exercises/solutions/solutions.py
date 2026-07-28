"""
Module 08 — Đáp án bài tập (Perceptron AND/OR)
Chạy: python exercises/solutions/solutions.py

YÊU CẦU ĐỀ BÀI:
  - Implement class Perceptron với step function (output 0 hoặc 1)
  - Train trên AND gate và OR gate
  - In accuracy, weights và bias cho mỗi gate

KẾT QUẢ MONG ĐỢI (khi chạy):
  - AND gate: accuracy 100%
  - OR gate: accuracy 100%
  - In weights và bias đã học được
"""

import numpy as np


# ── Perceptron với step function ──
class Perceptron:
    """Perceptron đơn giản với step function."""

    def __init__(self, lr=0.1, epochs=100):
        self.lr = lr
        self.epochs = epochs
        self.weights = None
        self.bias = 0

    def fit(self, X, y):
        """Huấn luyện bằng Perceptron learning rule."""
        n_features = X.shape[1]
        self.weights = np.zeros(n_features)
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                # Step function: output 1 nếu tổng >= 0, ngược lại 0
                pred = 1 if np.dot(xi, self.weights) + self.bias >= 0 else 0
                error = target - pred
                self.weights += self.lr * error * xi  # cập nhật trọng số
                self.bias += self.lr * error

    def predict(self, X):
        """Dự đoán nhãn 0 hoặc 1 cho từng mẫu."""
        return np.array([1 if np.dot(xi, self.weights) + self.bias >= 0 else 0 for xi in X])


# ── Demo AND và OR gate ──
if __name__ == "__main__":
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    for gate, y in [("AND", [0, 0, 0, 1]), ("OR", [0, 1, 1, 1])]:
        p = Perceptron(epochs=100)
        p.fit(X, np.array(y))
        preds = p.predict(X)
        acc = (preds == y).mean()
        print(f"{gate} gate: accuracy={acc:.0%}, weights={p.weights}, bias={p.bias}")
