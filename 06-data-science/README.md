# Module 06: Data Science với NumPy & Pandas

## Mục tiêu

- Thao tác mảng với NumPy
- Phân tích dữ liệu với Pandas
- Visualization cơ bản với Matplotlib

---

## 1. NumPy — Mảng số học

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Tạo mảng
np.zeros((3, 4))          # ma trận 0
np.ones((2, 3))           # ma trận 1
np.arange(0, 10, 2)       # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)      # [0, 0.25, 0.5, 0.75, 1]
np.random.randn(3, 3)     # random normal

# Operations — vectorized (nhanh!)
arr * 2                   # nhân từng phần tử
arr + 10
np.sqrt(arr)
matrix.T                  # transpose
matrix @ matrix.T         # matrix multiplication

# Statistics
arr.mean(), arr.std(), arr.min(), arr.max()
matrix.sum(axis=0)        # sum theo cột
matrix.sum(axis=1)        # sum theo hàng

# Indexing
arr[1:4]                  # slice
matrix[0, 1]              # phần tử
matrix[:, 0]              # cột đầu
arr[arr > 3]              # boolean indexing
```

---

## 2. Pandas — DataFrame

```python
import pandas as pd

# Tạo DataFrame
df = pd.DataFrame({
    "name": ["An", "Bình", "Chi"],
    "age": [25, 30, 28],
    "salary": [15_000_000, 20_000_000, 18_000_000],
})

# Đọc file
df = pd.read_csv("data.csv")
df = pd.read_json("data.json")

# Xem dữ liệu
df.head()                 # 5 dòng đầu
df.info()                 # thông tin cột
df.describe()             # thống kê mô tả
df.shape                  # (rows, cols)

# Chọn dữ liệu
df["name"]                # 1 cột → Series
df[["name", "age"]]       # nhiều cột
df.loc[0]                 # theo label
df.iloc[0:2]              # theo index
df[df["age"] > 26]        # filter

# Xử lý missing
df.isnull().sum()
df.dropna()
df.fillna(0)
df["age"].fillna(df["age"].mean())

# Groupby
df.groupby("department")["salary"].mean()
df.groupby("department").agg({"salary": ["mean", "max"], "age": "count"})

# Merge
pd.merge(df1, df2, on="id", how="inner")
```

---

## 3. Matplotlib — Visualization

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].plot(x, y, label="Training")
axes[0].set_title("Loss over epochs")
axes[0].legend()

axes[1].bar(categories, values)
axes[1].set_title("Category counts")

plt.tight_layout()
plt.savefig("chart.png", dpi=150)
plt.show()
```

---

## Pipeline xử lý dữ liệu điển hình

```
Load → Explore → Clean → Transform → Analyze → Visualize
  │       │        │         │          │          │
 CSV   .info()  dropna()  feature    groupby()   plot()
 JSON  .describe() fillna()  engineering  .agg()   savefig()
```

---

## Chạy ví dụ

```bash
python examples/01_numpy_basics.py
python examples/02_pandas_basics.py
python examples/03_visualization.py
```

---

## Giải thích chi tiết (Tự học)

### File `examples/01_numpy_basics.py`

```python
arr = np.array([1, 2, 3])
matrix = np.array([[1, 2], [3, 4]])
```

**Vectorized operations** — tính trên cả mảng không cần vòng lặp:
```python
a + b          # Cộng từng phần tử
a * 2          # Nhân scalar
np.sqrt(a)     # Căn từng phần tử — nhanh hơn loop Python 10-100x
```

```python
matrix.sum(axis=0)   # Tổng theo CỘT
matrix.sum(axis=1)   # Tổng theo HÀNG
scores[scores >= 70] # Boolean indexing — lọc phần tử thỏa điều kiện
```

**Broadcasting:** `matrix + row` — NumPy tự "mở rộng" `row` để khớp kích thước.

---

### File `examples/02_pandas_basics.py`

```python
df = pd.DataFrame({...})
df.head()           # 5 dòng đầu
df.describe()       # mean, std, min, max tự động
df[df["age"] > 26]  # Lọc hàng — boolean mask
```

```python
df.groupby("department").agg(
    count=("name", "count"),
    avg_salary=("salary", "mean"),
)
```

- `groupby` — nhóm theo cột rồi tính toán trên từng nhóm (như SQL GROUP BY)
- `.agg()` — aggregate nhiều metric cùng lúc

```python
df.nlargest(3, "salary")   # Top 3 lương cao nhất
df["salary"].rank(ascending=False)  # Xếp hạng
```

---

### File `examples/03_visualization.py`

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0, 0].plot(x, y)
axes[0, 1].bar(categories, values)
axes[1, 0].hist(data, bins=30)
axes[1, 1].scatter(x, y)
plt.savefig("chart.png", dpi=150)
plt.close()
```

- `subplots(2,2)` — lưới 2×2 biểu đồ
- Luôn `close()` sau `savefig` — giải phóng RAM

---

## Bài tập

→ [exercises/bai_tap.md](exercises/bai_tap.md)

## Module tiếp theo

→ [Module 07: Machine Learning](../07-machine-learning/README.md)
