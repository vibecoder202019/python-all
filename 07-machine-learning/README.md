# Module 07: Machine Learning với Scikit-learn

## Mục tiêu

- Hiểu pipeline ML: data → train → evaluate → deploy
- Sử dụng Scikit-learn cho classification & regression
- Cross-validation, hyperparameter tuning

---

## Lý thuyết nền tảng — Machine Learning là gì?

**ML = máy tính học từ dữ liệu** thay vì lập trình viên viết rule cứng.

```
Rule-based (cũ):     if petal_length > 4.5 → virginica
ML (mới):            Học từ 150 mẫu hoa → tự tìm pattern
```

### Hai loại bài toán chính

| Loại | Output | Ví dụ | Metric |
|------|--------|-------|--------|
| **Classification** | Nhãn rời rạc (class) | Phân loại email spam | Accuracy, F1 |
| **Regression** | Số liên tục | Dự đoán giá nhà | RMSE, R² |

### Train / Test split — tại sao?

Nếu test trên data đã học → model "học thuộc" → **overfitting**:
- Train accuracy 99%, test accuracy 60% → model không generalize

**Quy tắc vàng:** Test set **không bao giờ** được dùng khi train hoặc tune.

### Feature vs Label

```
Features (X)              Label (y)
─────────────────         ─────────
[5.1, 3.5, 1.4, 0.2]  →   setosa
[6.2, 2.8, 4.8, 1.8]  →   versicolor
```

- **X** = input model nhìn thấy
- **y** = đáp án model cần dự đoán

### Overfitting vs Underfitting

| | Overfitting | Underfitting |
|---|-------------|--------------|
| Biểu hiện | Train tốt, test kém | Train và test đều kém |
| Nguyên nhân | Model quá phức tạp | Model quá đơn giản |
| Cách xử lý | Regularization, more data | Thêm features, model phức tạp hơn |

### Cross-validation — kiểm tra ổn định

Chia data 5 phần, rotate train/test 5 lần → trung bình score **đáng tin hơn** 1 lần split.

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

## Câu hỏi thường gặp (FAQ)

**Q: Accuracy 95% có tốt không?**  
A: Tùy dataset — nếu 95% data là class A, model đoán hết A cũng được 95% nhưng vô dụng. Xem precision/recall/F1.

**Q: Train accuracy cao, test thấp?**  
A: **Overfitting** — giảm complexity, thêm data, hoặc regularization.

**Q: Có cần scale data cho RandomForest?**  
A: RF không bắt buộc. SVM, KNN, Neural Net **cần** scale.

**Q: `random_state=42` nghĩa là gì?**  
A: Seed cố định → kết quả reproducible (chạy lại cho cùng kết quả).

---

## Bài tập

→ [exercises/bai_tap.md](exercises/bai_tap.md)

## Module tiếp theo

→ [Module 08: Deep Learning](../08-deep-learning/README.md)
