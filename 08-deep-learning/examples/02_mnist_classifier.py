"""Module 08 — MNIST Classifier với Keras"""
import numpy as np

try:
    import tensorflow as tf
    from tensorflow import keras
except ImportError:
    print("Cần cài TensorFlow: pip install tensorflow")
    raise

print(f"TensorFlow version: {tf.__version__}")

# Load MNIST
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0

print(f"Training: {X_train.shape}, Test: {X_test.shape}")

# Build model
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

model.summary()

# Train (3 epochs cho demo nhanh)
print("\n=== Training (3 epochs) ===")
history = model.fit(
    X_train, y_train,
    epochs=3,
    batch_size=128,
    validation_split=0.1,
    verbose=1,
)

# Evaluate
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f"\nTest accuracy: {test_acc:.4f}")

# Predict samples
predictions = model.predict(X_test[:5], verbose=0)
for i in range(5):
    pred = np.argmax(predictions[i])
    print(f"  Sample {i}: predicted={pred}, actual={y_test[i]}")
