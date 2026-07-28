"""
Module 04 — Ví dụ 2: JSON và CSV
Chạy: python examples/02_json_csv.py

YÊU CẦU ĐỀ BÀI:
  - Ghi/đọc JSON với json.dump/load, ensure_ascii=False cho tiếng Việt
  - Ghi CSV với csv.DictWriter
  - Đọc CSV với csv.DictReader và tính điểm trung bình

KẾT QUẢ MONG ĐỢI (khi chạy):
  - Profile JSON: tên, skills, 2 projects kèm accuracy
  - CSV 3 sinh viên với điểm TB: An≈84.3, Bình≈91.7, Chi≈71.7
"""
import csv
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)


def demo_json():
    profile = {
        "name": "Nguyễn Văn A",
        "age": 28,
        "skills": ["Python", "Machine Learning", "FastAPI"],
        "projects": [
            {"name": "Iris Classifier", "accuracy": 0.97},
            {"name": "Sentiment API", "accuracy": 0.89},
        ],
    }

    json_path = DATA_DIR / "profile.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=2, ensure_ascii=False)  # giữ ký tự Unicode

    with open(json_path, encoding="utf-8") as f:
        loaded = json.load(f)

    print("=== JSON Profile ===")
    print(f"  Tên: {loaded['name']}")
    print(f"  Skills: {', '.join(loaded['skills'])}")
    for p in loaded["projects"]:
        print(f"  Project: {p['name']} (acc={p['accuracy']})")


def demo_csv():
    students = [
        {"id": "SV001", "name": "An", "math": 85, "english": 90, "physics": 78},
        {"id": "SV002", "name": "Bình", "math": 92, "english": 88, "physics": 95},
        {"id": "SV003", "name": "Chi", "math": 70, "english": 65, "physics": 80},
    ]

    csv_path = DATA_DIR / "students.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=students[0].keys())
        writer.writeheader()
        writer.writerows(students)

    print("\n=== CSV Students ===")
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            avg = (int(row["math"]) + int(row["english"]) + int(row["physics"])) / 3
            print(f"  {row['name']}: avg={avg:.1f}")


# ── Demo ──
if __name__ == "__main__":
    demo_json()
    demo_csv()
