# Module 07: Machine Learning với Scikit-learn

## Mục tiêu

- Hiểu pipeline ML: data → train → evaluate → deploy
- Sử dụng Scikit-learn cho classification & regression
- Cross-validation, hyperparameter tuning

---

## 1. Quy trình ML

```
┌─────────┐   ┌─────────┐   ┌──────────┐   ┌─────────┐   ┌──────────┐
│  Data   │ → │  Clean  │ → │ Features │ → │  Train  │ → │ Evaluate │
│  Load   │   │  & EDA  │   │ Engineer │   │  Model  │   │  & Tune  │
└─────────┘   └─────────┘   └──────────┘   └─────────┘   └──────────┘
```

---

## 2. Classification — Iris Dataset

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load data
X, y = load_iris(return_X_y=True)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate
y_pred = model.predict(X_test_scaled)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(classification_report(y_test, y_pred))
```

---

## 3. Regression

```python
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X, y = fetch_california_housing(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"RMSE: {mean_squared_error(y_test, y_pred, squared=False):.4f}")
print(f"R²: {r2_score(y_test, y_pred):.4f}")
```

---

## 4. Cross-Validation

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
print(f"CV scores: {scores}")
print(f"Mean: {scores.mean():.4f} (+/- {scores.std():.4f})")
```

---

## 5. Hyperparameter Tuning

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [3, 5, 10, None],
}
grid = GridSearchCV(RandomForestClassifier(), param_grid, cv=5)
grid.fit(X_train, y_train)
print(f"Best params: {grid.best_params_}")
print(f"Best score: {grid.best_score_:.4f}")
```

---

## 6. Save & Load Model

```python
import joblib

joblib.dump(model, "model.joblib")
joblib.dump(scaler, "scaler.joblib")

loaded_model = joblib.load("model.joblib")
loaded_scaler = joblib.load("scaler.joblib")
```

---

## Metrics quan trọng

| Task | Metrics |
|------|---------|
| Classification | Accuracy, Precision, Recall, F1, Confusion Matrix |
| Regression | MSE, RMSE, MAE, R² |
| Clustering | Silhouette Score, Inertia |

---

## Chạy ví dụ

```bash
python examples/01_classification_iris.py
python examples/02_regression.py
python examples/03_cross_validation.py
python examples/04_save_load_model.py
```

---

## Giải thích chi tiết (Tự học)

### Pipeline ML trong ví dụ

```
Load data → train_test_split → StandardScaler → fit model → predict → evaluate
```

**Tại sao split?** Train trên tập A, test trên tập B — đo khả năng **generalize** (dự đoán data chưa thấy).

**Tại sao scale?** RandomForest ít cần, nhưng SVM/Neural Net cần features cùng thang đo:
```python
scaler.fit_transform(X_train)   # Học mean/std từ train
scaler.transform(X_test)        # Áp cùng mean/std — KHÔNG fit lại test
```

---

### File `examples/01_classification_iris.py`

```python
train_test_split(X, y, test_size=0.2, stratify=y)
```

- `stratify=y` — giữ tỷ lệ class trong train và test (quan trọng khi data mất cân bằng)
- `classification_report` — precision, recall, f1 từng class
- `confusion_matrix` — ma trận dự đoán vs thực tế
- `feature_importances_` — feature nào model coi là quan trọng nhất

---

### File `examples/03_cross_validation.py`

```python
cross_val_score(model, X, y, cv=5, scoring="accuracy")
```

- Chia data 5 fold — train/evaluate 5 lần, lấy trung bình → ước lượng ổn định hơn 1 lần split

```python
GridSearchCV(model, param_grid, cv=5)
grid.fit(X_train, y_train)
grid.best_params_
```

- Thử mọi tổ hợp hyperparameter trong `param_grid` — chọn bộ tốt nhất

---

### File `examples/04_save_load_model.py`

```python
joblib.dump(model, "iris_model.joblib")
model = joblib.load("iris_model.joblib")
```

- Lưu model đã train + scaler + metadata → deploy sau không cần train lại
- **Luôn lưu scaler cùng model** — predict phải scale input giống lúc train

---

## Bài tập

→ [exercises/bai_tap.md](exercises/bai_tap.md)

## Module tiếp theo

→ [Module 08: Deep Learning](../08-deep-learning/README.md)
