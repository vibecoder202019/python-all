"""
Module 07 — Ví dụ 2: Regression (California Housing)
Chạy: python examples/02_regression.py

YÊU CẦU ĐỀ BÀI:
  - Load California Housing dataset
  - Chia train/test, chuẩn hóa feature
  - So sánh 3 model: LinearRegression, Ridge, RandomForestRegressor
  - Đánh giá bằng RMSE, MAE, R² trên test set

KẾT QUẢ MONG ĐỢI (khi chạy):
  - In số samples và features của dataset
  - In bảng metrics RMSE/MAE/R² cho từng model
  - Random Forest thường cho R² cao nhất
"""

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler
import numpy as np

# ── Load dữ liệu ──
housing = fetch_california_housing()
X, y = housing.data, housing.target

# ── Chia train/test ──
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ── Chuẩn hóa feature ──
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ── Danh sách model cần so sánh ──
models = {
    "Linear Regression": LinearRegression(),
    "Ridge (alpha=1)": Ridge(alpha=1.0),  # L2 regularization
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
}

print("=== California Housing Regression ===")
print(f"Dataset: {X.shape[0]} samples, {X.shape[1]} features")
print(f"Target: Median house value ($100k)\n")

# ── Train và đánh giá từng model ──
for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    rmse = mean_squared_error(y_test, y_pred) ** 0.5  # căn MSE → RMSE
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)  # hệ số xác định, càng gần 1 càng tốt
    print(f"  {name:25s} RMSE={rmse:.4f}  MAE={mae:.4f}  R²={r2:.4f}")
