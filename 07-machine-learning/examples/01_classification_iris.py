"""
Module 07 — Ví dụ 1: Classification với Iris dataset
Chạy: python examples/01_classification_iris.py

YÊU CẦU ĐỀ BÀI:
  - Load Iris dataset, chia train/test với stratify
  - Chuẩn hóa feature bằng StandardScaler
  - Train RandomForestClassifier và đánh giá accuracy, classification report
  - In confusion matrix, feature importance và sample predictions

KẾT QUẢ MONG ĐỢI (khi chạy):
  - In accuracy trên test set (~0.97+)
  - In classification report cho 3 loài hoa
  - In confusion matrix và feature importance dạng bar
  - In 3 dự đoán mẫu so sánh predicted vs actual
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import numpy as np

# ── Load dữ liệu ──
iris = load_iris()
X, y = iris.data, iris.target
target_names = iris.target_names

# ── Chia train/test — stratify giữ tỷ lệ class ──
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ── Chuẩn hóa feature — fit trên train, transform cả train và test ──
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ── Train model ──
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# ── Dự đoán và đánh giá ──
y_pred = model.predict(X_test_scaled)

print("=== Iris Classification ===")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=target_names))

print("Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(f"  {cm}")

# ── Feature importance — độ quan trọng từng đặc trưng ──
print("\nFeature Importance:")
for name, importance in zip(iris.feature_names, model.feature_importances_):
    bar = "█" * int(importance * 50)
    print(f"  {name:20s} {importance:.4f} {bar}")

# ── Dự đoán mẫu ──
print("\nSample Predictions:")
sample = X_test_scaled[:3]
preds = model.predict(sample)
for i, (pred, actual) in enumerate(zip(preds, y_test[:3])):
    print(f"  Sample {i+1}: predicted={target_names[pred]}, actual={target_names[actual]}")
