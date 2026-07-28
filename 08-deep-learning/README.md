# Module 08: Deep Learning cơ bản

## Mục tiêu

- Hiểu neural network: neuron, layer, activation, loss
- Xây dựng model với Keras/TensorFlow
- Train model phân loại MNIST

---

## 1. Neural Network là gì?

```
Input Layer    Hidden Layer(s)    Output Layer
  (784)    →     (128, 64)     →    (10)
   │              │    │              │
   x₁ ──→ [w,b] → ReLU → ... → Softmax → class
```

**Thành phần:**
- **Neuron** — tính `output = activation(Σ(wᵢxᵢ) + b)`
- **Activation** — ReLU, Sigmoid, Softmax
- **Loss** — đo sai số (CrossEntropy, MSE)
- **Optimizer** — cập nhật weights (Adam, SGD)

---

## 2. Keras Sequential API

```python
import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(64, activation="relu"),
    keras.layers.Dense(10, activation="softmax"),
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

model.fit(X_train, y_train, epochs=10, validation_split=0.2)
```

---

## 3. Key Concepts

| Khái niệm | Giải thích |
|-----------|-----------|
| Epoch | 1 lần duyệt toàn bộ training data |
| Batch size | Số samples mỗi bước cập nhật weight |
| Learning rate | Tốc độ học — quá cao → không hội tụ |
| Overfitting | Model học thuộc training data, kém trên test |
| Dropout | Tắt ngẫu nhiên neurons → chống overfitting |
| Early stopping | Dừng train khi validation loss không giảm |

---

## Chạy ví dụ

```bash
python examples/01_neural_network_basics.py
python examples/02_mnist_classifier.py
```

> **Lưu ý:** TensorFlow cần cài riêng. Chạy `pip install tensorflow` nếu chưa có.

## Bài tập

→ [exercises/bai_tap.md](exercises/bai_tap.md)

## Module tiếp theo

→ [Module 09: FastAPI](../09-fastapi/README.md)
