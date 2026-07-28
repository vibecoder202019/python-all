"""
Module 05 — Ví dụ 2: datetime & regex
Chạy: python examples/02_datetime_regex.py

YÊU CẦU ĐỀ BÀI:
  - Dùng datetime để lấy thời gian hiện tại, tính tuổi, cộng timedelta
  - Dùng regex (re) để trích xuất email, phone, URL từ văn bản
  - Validate định dạng email bằng re.match

KẾT QUẢ MONG ĐỢI (khi chạy):
  - In thời gian hiện tại (format thường và ISO)
  - In tuổi tính từ ngày sinh và deadline 30 ngày
  - In danh sách emails, phones, URLs tìm được
  - In kết quả validate 3 email mẫu
"""

import re
from datetime import datetime, timedelta


def demo_datetime():
    """Demo thao tác với ngày giờ."""
    now = datetime.now()
    print("=== datetime ===")
    print(f"  Now: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  ISO: {now.isoformat()}")

    # strptime: parse chuỗi → datetime object
    birthday = datetime.strptime("1998-05-15", "%Y-%m-%d")
    age_days = (now - birthday).days  # chênh lệch ngày giữa 2 datetime
    print(f"  Tuổi (ngày): {age_days:,} ngày ≈ {age_days // 365} tuổi")

    deadline = now + timedelta(days=30)  # cộng thêm 30 ngày
    print(f"  Deadline 30 ngày: {deadline.strftime('%Y-%m-%d')}")


def demo_regex():
    """Demo trích xuất và validate bằng biểu thức chính quy."""
    text = """
    Liên hệ: minh@example.com, support@company.vn
    Phone: 0901234567, 0912345678
    Website: https://python.org
    """

    print("\n=== regex ===")
    # findall: tìm tất cả chuỗi khớp pattern
    emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)
    print(f"  Emails: {emails}")

    phones = re.findall(r"0\d{9}", text)  # số điện thoại VN: 0 + 9 chữ số
    print(f"  Phones: {phones}")

    urls = re.findall(r"https?://[\w./-]+", text)
    print(f"  URLs: {urls}")

    # ── Validate email ──
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    test_emails = ["valid@email.com", "invalid@", "bad.email"]
    for e in test_emails:
        valid = bool(re.match(email_pattern, e))  # match từ đầu chuỗi
        print(f"  '{e}' valid={valid}")


if __name__ == "__main__":
    demo_datetime()
    demo_regex()
