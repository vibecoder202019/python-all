"""
Module 01 — Đáp án Bài 4-7: Số nguyên tố, Thống kê, Caesar, Top SV
Chạy: python exercises/solutions/bai_4_7.py

YÊU CẦU ĐỀ BÀI:
  - Kiểm tra số nguyên tố (tối ưu đến √n)
  - Tính thống kê điểm: count, average, max, min, passed, excellent
  - Mã hóa/giải mã Caesar cipher (dịch chuyển chữ cái)
  - Lọc sinh viên có điểm TB ≥ ngưỡng, sắp xếp giảm dần

KẾT QUẢ MONG ĐỢI (khi chạy):
  - Danh sách số nguyên tố 2-100 (25 số)
  - Dict thống kê điểm 10 môn
  - Mã hóa Hello → Khoor, giải mã ngược lại
  - Top students: Bình (91.67), An (84.33)
"""
import math


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # chỉ kiểm tra ước lẻ từ 3 đến √n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def score_stats(scores: list[float]) -> dict:
    return {
        "count": len(scores),
        "average": round(sum(scores) / len(scores), 1),
        "max": max(scores),
        "min": min(scores),
        "passed": sum(1 for s in scores if s >= 50),
        "excellent": sum(1 for s in scores if s >= 90),
    }


def caesar_cipher(text: str, shift: int) -> str:
    result = []
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")  # mốc bảng chữ cái
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)  # giữ nguyên ký tự không phải chữ
    return "".join(result)


def caesar_decipher(text: str, shift: int) -> str:
    return caesar_cipher(text, -shift)  # giải mã = dịch ngược


def top_students(students: list[dict], min_avg: float = 80) -> list[dict]:
    result = []
    for s in students:
        avg = sum(s["scores"]) / len(s["scores"])
        if avg >= min_avg:
            result.append({"name": s["name"], "average": round(avg, 2)})
    return sorted(result, key=lambda x: x["average"], reverse=True)


# ── Demo ──
if __name__ == "__main__":
    primes = [n for n in range(2, 101) if is_prime(n)]
    print(f"Số nguyên tố 2-100: {primes[:10]}... ({len(primes)} số)")

    scores = [85, 92, 78, 95, 60, 88, 73, 91, 55, 82]
    print(f"Thống kê: {score_stats(scores)}")

    encrypted = caesar_cipher("Hello", 3)
    print(f"Mã hóa: Hello → {encrypted}")
    print(f"Giải mã: {encrypted} → {caesar_decipher(encrypted, 3)}")

    students = [
        {"name": "An", "scores": [85, 90, 78]},
        {"name": "Bình", "scores": [92, 88, 95]},
        {"name": "Chi", "scores": [70, 65, 80]},
    ]
    print(f"Top students: {top_students(students)}")
