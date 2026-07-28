"""
Module 08 — Ví dụ 2: MNIST Classifier với Keras
Chạy: python examples/02_mnist_classifier.py

YÊU CẦU ĐỀ BÀI:
  - Load MNIST dataset, chuẩn hóa pixel về [0, 1]
  - Xây dựng MLP: Flatten → Dense(128) → Dropout → Dense(64) → Dense(10)
  - Train 3 epochs, đánh giá trên test set
  - Dự đoán 5 mẫu đầu tiên

KẾT QUẢ MONG ĐỢI (khi chạy):
  - In phiên bản TensorFlow
  - In shape train/test và model summary
  - In test accuracy (~0.97+ sau 3 epochs)
  - In predicted vs actual cho 5 mẫu
"""

import numpy as np

try:
    import tensorflow as tf
    from tensorflow import keras
except ImportError:
    print("Cần cài TensorFlow: pip install tensorflow")
    raise

print(f"TensorFlow version: {tf.__version__}")

# ── Load MNIST — 60k train, 10k test, ảnh 28x28 grayscale ──
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

# Chuẩn hóa pixel từ [0, 255] → [0, 1]
X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0

print(f"Training: {X_train.shape}, Test: {X_test.shape}")

# ── Xây dựng model MLP ──
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # 28x28 → vector 784
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dropout(0.2),  # bỏ ngẫu nhiên 20% neuron — chống overfit
    keras.layers.Dense(64, activation="relu"),
    keras.layers.Dense(10, activation="softmax"),  # 10 class → xác suất
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",  # nhãn dạng số nguyên (0-9)
    metrics=["accuracy"],
)

model.summary()

# ── Train (3 epochs cho demo nhanh) ──
print("\n=== Training (3 epochs) ===")
history = model.fit(
    X_train, y_train,
    epochs=3,
    batch_size=128,
    validation_split=0.1,  # 10% train dùng làm validation
    verbose=1,
)

# ── Đánh giá trên test set ──
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f"\nTest accuracy: {test_acc:.4f}")

# ── Dự đoán 5 mẫu đầu ──
predictions = model.predict(X_test[:5], verbose=0)
for i in range(5):
    pred = np.argmax(predictions[i])  # class có xác suất cao nhất
    print(f"  Sample {i}: predicted={pred}, actual={y_test[i]}")
