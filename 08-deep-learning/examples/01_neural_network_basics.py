"""
Module 08 — Ví dụ 1: Neural Network cơ bản (Perceptron từ scratch)
Chạy: python examples/01_neural_network_basics.py

YÊU CẦU ĐỀ BÀI:
  - Implement class Perceptron với sigmoid activation
  - Train trên bài toán AND gate (2 input → 1 output)
  - Demo các hàm kích hoạt: ReLU, Sigmoid, Tanh

KẾT QUẢ MONG ĐỢI (khi chạy):
  - In weights, bias sau training
  - In từng dòng input → expected vs predicted với dấu ✓/✗
  - In accuracy 100% trên AND gate
  - In giá trị mẫu của ReLU, Sigmoid, Tanh
"""

import numpy as np


class Perceptron:
    """Perceptron đơn giản — 1 neuron."""

    def __init__(self, learning_rate: float = 0.1, n_iterations: int = 100):
        self.lr = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None

    def sigmoid(self, x):
        """Hàm kích hoạt sigmoid — đưa output về khoảng (0, 1)."""
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))  # clip tránh overflow

    def sigmoid_derivative(self, x):
        """Đạo hàm sigmoid — dùng khi backpropagation."""
        s = self.sigmoid(x)
        return s * (1 - s)

    def fit(self, X: np.ndarray, y: np.ndarray):
        """Huấn luyện Perceptron bằng gradient descent đơn giản."""
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iterations):
            for i in range(n_samples):
                linear = np.dot(X[i], self.weights) + self.bias  # tổng có trọng số
                prediction = self.sigmoid(linear)
                error = y[i] - prediction  # sai số
                # Cập nhật trọng số theo learning rate
                self.weights += self.lr * error * X[i]
                self.bias += self.lr * error

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Dự đoán nhãn 0 hoặc 1 (ngưỡng 0.5)."""
        linear = np.dot(X, self.weights) + self.bias
        return (self.sigmoid(linear) >= 0.5).astype(int)


# ── Demo: AND gate (Perceptron 1 lớp giải được) ──
print("=== Perceptron: AND gate ===")
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([0, 0, 0, 1])

model = Perceptron(learning_rate=0.1, n_iterations=1000)
model.fit(X, y_and)
predictions = model.predict(X)

print(f"  Weights: {model.weights}, Bias: {model.bias:.4f}")
for xi, yi, pred in zip(X, y_and, predictions):
    status = "✓" if yi == pred else "✗"
    print(f"  {xi} → expected={yi}, predicted={pred} {status}")

print(f"\n  Accuracy: {(predictions == y_and).mean():.0%}")

# ── Demo các hàm kích hoạt phổ biến ──
print("\n=== Activation Functions ===")
x = np.linspace(-5, 5, 100)

def relu(x):
    """ReLU: max(0, x) — phổ biến trong hidden layer."""
    return np.maximum(0, x)

def tanh(x):
    """Tanh: output trong (-1, 1)."""
    return np.tanh(x)

print(f"  ReLU(-2) = {relu(-2):.1f}, ReLU(3) = {relu(3):.1f}")
print(f"  Sigmoid(0) = {1/(1+np.exp(0)):.4f}")
print(f"  Tanh(0) = {tanh(0):.4f}")
