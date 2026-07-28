"""Đáp án Module 07"""
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib


def train_iris_classifier():
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return accuracy_score(y_test, y_pred), confusion_matrix(y_test, y_pred)


def compare_models():
    X, y = load_iris(return_X_y=True)
    models = {
        "LogisticRegression": LogisticRegression(max_iter=200),
        "SVM": SVC(),
        "RandomForest": RandomForestClassifier(random_state=42),
    }
    results = {}
    for name, model in models.items():
        scores = cross_val_score(model, X, y, cv=5)
        results[name] = scores.mean()
    return results


if __name__ == "__main__":
    acc, cm = train_iris_classifier()
    print(f"Accuracy: {acc:.4f}\nCM:\n{cm}")
    print(f"\nModel comparison: {compare_models()}")
