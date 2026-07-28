"""Module 08 — Neural Network basics (Perceptron from scratch)"""
import numpy as np


class Perceptron:
    """Perceptron đơn giản — 1 neuron."""

    def __init__(self, learning_rate: float = 0.1, n_iterations: int = 100):
        self.lr = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

    def sigmoid_derivative(self, x):
        s = self.sigmoid(x)
        return s * (1 - s)

    def fit(self, X: np.ndarray, y: np.ndarray):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iterations):
            for i in range(n_samples):
                linear = np.dot(X[i], self.weights) + self.bias
                prediction = self.sigmoid(linear)
                error = y[i] - prediction
                self.weights += self.lr * error * X[i]
                self.bias += self.lr * error

    def predict(self, X: np.ndarray) -> np.ndarray:
        linear = np.dot(X, self.weights) + self.bias
        return (self.sigmoid(linear) >= 0.5).astype(int)


# Demo: XOR problem (Perceptron không giải được — cần hidden layer)
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

print("\n=== Activation Functions ===")
x = np.linspace(-5, 5, 100)

def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)

print(f"  ReLU(-2) = {relu(-2):.1f}, ReLU(3) = {relu(3):.1f}")
print(f"  Sigmoid(0) = {1/(1+np.exp(0)):.4f}")
print(f"  Tanh(0) = {tanh(0):.4f}")
