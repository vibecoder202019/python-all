"""
Module 06 — Ví dụ 3: Trực quan hóa dữ liệu (Matplotlib)
Chạy: python examples/03_visualization.py

YÊU CẦU ĐỀ BÀI:
  - Vẽ 4 biểu đồ trong subplot 2x2: line, bar, histogram, scatter
  - Cấu hình title, label, legend, grid cho từng biểu đồ
  - Lưu figure ra file PNG

KẾT QUẢ MONG ĐỢI (khi chạy):
  - Tạo file output_chart.png trong thư mục examples/
  - In đường dẫn file đã lưu
  - 4 biểu đồ: Training Loss, Language Popularity, Score Distribution, Feature Correlation
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(42)

# ── Tạo figure với 4 subplot ──
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Data Science Visualization Demo", fontsize=14, fontweight="bold")

# ── 1. Line plot — training loss theo epoch ──
epochs = np.arange(1, 51)
train_loss = 2.0 * np.exp(-0.1 * epochs) + 0.05 * np.random.randn(50)
val_loss = 2.2 * np.exp(-0.08 * epochs) + 0.1 * np.random.randn(50)
axes[0, 0].plot(epochs, train_loss, label="Train", color="blue")
axes[0, 0].plot(epochs, val_loss, label="Validation", color="orange")
axes[0, 0].set_xlabel("Epoch")
axes[0, 0].set_ylabel("Loss")
axes[0, 0].set_title("Training Loss")
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# ── 2. Bar chart — số lượng theo danh mục ──
categories = ["Python", "Java", "Go", "Rust", "TypeScript"]
counts = [45, 30, 15, 8, 22]
colors = ["#3776ab", "#f89820", "#00add8", "#dea584", "#3178c6"]
axes[0, 1].bar(categories, counts, color=colors)
axes[0, 1].set_title("Language Popularity")
axes[0, 1].set_ylabel("Count")

# ── 3. Histogram — phân phối điểm số ──
data = np.random.normal(75, 12, 500)  # phân phối chuẩn μ=75, σ=12
axes[1, 0].hist(data, bins=30, color="steelblue", edgecolor="white", alpha=0.8)
axes[1, 0].axvline(data.mean(), color="red", linestyle="--", label=f"Mean={data.mean():.1f}")
axes[1, 0].set_title("Score Distribution")
axes[1, 0].set_xlabel("Score")
axes[1, 0].legend()

# ── 4. Scatter — tương quan giữa 2 feature ──
x = np.random.randn(100)
y = 2 * x + np.random.randn(100) * 0.5  # y tương quan tuyến tính với x
axes[1, 1].scatter(x, y, alpha=0.6, c="green", edgecolors="white")
axes[1, 1].set_title("Feature Correlation")
axes[1, 1].set_xlabel("Feature X")
axes[1, 1].set_ylabel("Feature Y")

# ── Lưu figure ──
plt.tight_layout()
output = __import__("pathlib").Path(__file__).parent / "output_chart.png"
plt.savefig(output, dpi=150, bbox_inches="tight")
print(f"Chart saved to: {output}")
plt.close()
