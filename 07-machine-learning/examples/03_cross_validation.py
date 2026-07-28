"""
Module 07 — Ví dụ 3: Cross Validation & Grid Search
Chạy: python examples/03_cross_validation.py

YÊU CẦU ĐỀ BÀI:
  - So sánh 3 classifier bằng 5-fold cross validation
  - Dùng StratifiedKFold để giữ tỷ lệ class mỗi fold
  - Dùng GridSearchCV tìm hyperparameter tốt nhất cho Random Forest

KẾT QUẢ MONG ĐỢI (khi chạy):
  - In accuracy từng fold và mean ± std cho mỗi model
  - In best_params_ và best_score_ sau Grid Search
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, GridSearchCV, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# ── Load dữ liệu ──
X, y = load_iris(return_X_y=True)

models = {
    "Random Forest": RandomForestClassifier(random_state=42),
    "SVM": SVC(random_state=42),
    "KNN": KNeighborsClassifier(),
}

# ── 5-Fold Cross Validation ──
print("=== 5-Fold Cross Validation ===")
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=cv, scoring="accuracy")
    print(f"  {name:20s} {scores.round(4)} → mean={scores.mean():.4f} (±{scores.std():.4f})")

# ── Grid Search — thử mọi tổ hợp hyperparameter ──
print("\n=== Grid Search — Random Forest ===")
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [3, 5, 10, None],
    "min_samples_split": [2, 5],
}
grid = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1,  # dùng tất cả CPU cores
)
grid.fit(X, y)

print(f"  Best params: {grid.best_params_}")
print(f"  Best CV score: {grid.best_score_:.4f}")
