# Module 08: Deep Learning cơ bản

## Mục tiêu

- Hiểu neural network: neuron, layer, activation, loss
- Xây dựng model với Keras/TensorFlow
- Train model phân loại MNIST

---

## Lý thuyết nền tảng — Deep Learning là gì?

**Deep Learning** = Machine Learning dùng **neural network nhiều lớp** (deep = sâu = nhiều layer).

```
ML truyền thống:  Features → Algorithm (RandomForest, SVM)
Deep Learning:    Raw data → Neural Network → Output
                  (tự học features!)
```

### Neuron — đơn vị cơ bản

Một neuron tính:
```
output = activation(w1×x1 + w2×x2 + ... + b)
```

- **w** (weights) — trọng số, học được qua training
- **b** (bias) — hệ số chặn
- **activation** — hàm phi tuyến (ReLU, Sigmoid)

### Tại sao cần activation function?

Không có activation → nhiều layer chỉ = 1 phép tính tuyến tính → **không học được pattern phức tạp**.

### Các layer trong network

```
Input (784 pixel)  →  Hidden (128 neuron)  →  Hidden (64)  →  Output (10 class)
     MNIST image         ReLU + Dropout         ReLU           Softmax
```

### Dropout — chống overfitting

Tắt ngẫu nhiên 20% neuron khi train → model không phụ thuộc 1 neuron cụ thể → generalize tốt hơn.

### Khi nào dùng Deep Learning?

✅ Ảnh, text, audio, data lớn (hàng nghìn+ mẫu)  
❌ Bảng nhỏ 100 dòng → RandomForest/XGBoost thường đủ và nhanh hơn

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

---

## Giải thích chi tiết (Tự học)

### File `examples/01_neural_network_basics.py`

**Perceptron** — neuron đơn giản nhất:
```python
prediction = sigmoid(dot(weights, input) + bias)
error = target - prediction
weights += learning_rate * error * input   # Cập nhật trọng số
```

- Perceptron **không giải được XOR** — cần hidden layer (→ neural network)

**Activation functions:**
- `ReLU(x) = max(0, x)` — phổ biến nhất, tránh vanishing gradient
- `Sigmoid` — output 0-1, dùng classification
- `Softmax` — output tổng = 1, dùng multi-class cuối network

---

### File `examples/02_mnist_classifier.py`

```python
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),   # 28×28 → vector 784
    keras.layers.Dense(128, activation="relu"),    # Fully connected
    keras.layers.Dropout(0.2),                     # Tắt 20% neuron — chống overfit
    keras.layers.Dense(10, activation="softmax"),    # 10 class (số 0-9)
])
```

```python
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(X_train, y_train, epochs=3, batch_size=128, validation_split=0.1)
```

| Tham số | Ý nghĩa |
|---------|---------|
| `epochs=3` | Duyệt toàn bộ training data 3 lần |
| `batch_size=128` | Cập nhật weight sau mỗi 128 mẫu |
| `validation_split=0.1` | 10% train dùng validate trong quá trình fit |
| `sparse_categorical_crossentropy` | Loss khi label là số nguyên (0-9), không one-hot |

```python
predictions = model.predict(X_test[:5])
np.argmax(predictions[i])   # Class có xác suất cao nhất
```

---

## Câu hỏi thường gặp (FAQ)

**Q: TensorFlow quá nặng — có alternative?**  
A: Có thể dùng PyTorch. Module này dùng Keras (API đơn giản hơn).

**Q: Train bao nhiêu epoch?**  
A: Quan sát validation loss — dừng khi không giảm nữa (early stopping).

**Q: GPU có cần không?**  
A: MNIST trên CPU vài phút OK. Dataset lớn (ImageNet) cần GPU.

---

## Bài tập

→ [exercises/bai_tap.md](exercises/bai_tap.md)

## Module tiếp theo

→ [Module 09: FastAPI](../09-fastapi/README.md)
