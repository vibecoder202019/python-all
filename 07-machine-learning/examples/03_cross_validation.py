"""Module 07 — Cross Validation & Grid Search"""
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, GridSearchCV, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

X, y = load_iris(return_X_y=True)

models = {
    "Random Forest": RandomForestClassifier(random_state=42),
    "SVM": SVC(random_state=42),
    "KNN": KNeighborsClassifier(),
}

print("=== 5-Fold Cross Validation ===")
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=cv, scoring="accuracy")
    print(f"  {name:20s} {scores.round(4)} → mean={scores.mean():.4f} (±{scores.std():.4f})")

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
    n_jobs=-1,
)
grid.fit(X, y)

print(f"  Best params: {grid.best_params_}")
print(f"  Best CV score: {grid.best_score_:.4f}")
