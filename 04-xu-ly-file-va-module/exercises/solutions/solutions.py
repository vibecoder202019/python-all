"""
Module 04 — Đáp án bài tập: Phân tích text, CSV→JSON, Log parser
Chạy: python exercises/solutions/solutions.py

YÊU CẦU ĐỀ BÀI:
  - analyze_text: đếm dòng, từ, từ phổ biến nhất
  - csv_to_json: chuyển CSV sinh viên sang JSON, thêm cột average
  - analyze_logs: parse log theo regex, đếm theo level (INFO, ERROR, ...)

KẾT QUẢ MONG ĐỢI (khi chạy):
  - In "Module 04 solutions ready — import and use functions above."
  - Các hàm sẵn sàng import để dùng trong bài tập
"""
import csv
import json
import re
from collections import Counter
from pathlib import Path


def analyze_text(filepath: str) -> dict:
    text = Path(filepath).read_text(encoding="utf-8")
    words = text.lower().split()
    return {
        "lines": len(text.splitlines()),
        "words": len(words),
        "most_common": Counter(words).most_common(1)[0] if words else None,
    }


def csv_to_json(csv_path: str, json_path: str):
    with open(csv_path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    for row in rows:
        scores = [int(row[k]) for k in row if k not in ("id", "name")]  # lấy cột điểm số
        row["average"] = round(sum(scores) / len(scores), 2)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)


def analyze_logs(log_path: str) -> dict:
    pattern = r"\[([\d-]+ [\d:]+)\] (\w+): (.+)"  # [timestamp] LEVEL: message
    levels = Counter()
    with open(log_path, encoding="utf-8") as f:
        for line in f:
            match = re.match(pattern, line.strip())
            if match:
                levels[match.group(2)] += 1  # group(2) = level (INFO, ERROR, ...)
    return dict(levels)


# ── Demo ──
if __name__ == "__main__":
    print("Module 04 solutions ready — import and use functions above.")
