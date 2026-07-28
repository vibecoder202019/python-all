"""Module 07 — Save & Load Model"""
import joblib
from pathlib import Path
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

MODEL_DIR = Path(__file__).parent / "models"
MODEL_DIR.mkdir(exist_ok=True)

# Train
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Save
joblib.dump(model, MODEL_DIR / "iris_model.joblib")
joblib.dump(scaler, MODEL_DIR / "iris_scaler.joblib")

metadata = {
    "model_type": "RandomForestClassifier",
    "n_estimators": 100,
    "features": iris.feature_names,
    "target_names": list(iris.target_names),
    "accuracy": accuracy_score(y_test, model.predict(X_test_scaled)),
}
joblib.dump(metadata, MODEL_DIR / "metadata.joblib")

print("=== Model Saved ===")
for f in MODEL_DIR.glob("*.joblib"):
    print(f"  {f.name} ({f.stat().st_size:,} bytes)")

# Load & predict
loaded_model = joblib.load(MODEL_DIR / "iris_model.joblib")
loaded_scaler = joblib.load(MODEL_DIR / "iris_scaler.joblib")
loaded_meta = joblib.load(MODEL_DIR / "metadata.joblib")

sample = loaded_scaler.transform([[5.1, 3.5, 1.4, 0.2]])
pred = loaded_model.predict(sample)
print(f"\n=== Loaded Model Prediction ===")
print(f"  Input: [5.1, 3.5, 1.4, 0.2]")
print(f"  Predicted: {loaded_meta['target_names'][pred[0]]}")
print(f"  Model accuracy: {loaded_meta['accuracy']:.4f}")
