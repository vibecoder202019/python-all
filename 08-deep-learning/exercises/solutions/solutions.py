"""Đáp án Module 08 — Perceptron AND/OR"""
import numpy as np


class Perceptron:
    def __init__(self, lr=0.1, epochs=100):
        self.lr = lr
        self.epochs = epochs
        self.weights = None
        self.bias = 0

    def fit(self, X, y):
        n_features = X.shape[1]
        self.weights = np.zeros(n_features)
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                pred = 1 if np.dot(xi, self.weights) + self.bias >= 0 else 0
                error = target - pred
                self.weights += self.lr * error * xi
                self.bias += self.lr * error

    def predict(self, X):
        return np.array([1 if np.dot(xi, self.weights) + self.bias >= 0 else 0 for xi in X])


if __name__ == "__main__":
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    for gate, y in [("AND", [0, 0, 0, 1]), ("OR", [0, 1, 1, 1])]:
        p = Perceptron(epochs=100)
        p.fit(X, np.array(y))
        preds = p.predict(X)
        acc = (preds == y).mean()
        print(f"{gate} gate: accuracy={acc:.0%}, weights={p.weights}, bias={p.bias}")
