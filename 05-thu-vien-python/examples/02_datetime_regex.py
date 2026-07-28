"""Module 05 — datetime & regex"""
import re
from datetime import datetime, timedelta


def demo_datetime():
    now = datetime.now()
    print("=== datetime ===")
    print(f"  Now: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  ISO: {now.isoformat()}")

    birthday = datetime.strptime("1998-05-15", "%Y-%m-%d")
    age_days = (now - birthday).days
    print(f"  Tuổi (ngày): {age_days:,} ngày ≈ {age_days // 365} tuổi")

    deadline = now + timedelta(days=30)
    print(f"  Deadline 30 ngày: {deadline.strftime('%Y-%m-%d')}")


def demo_regex():
    text = """
    Liên hệ: minh@example.com, support@company.vn
    Phone: 0901234567, 0912345678
    Website: https://python.org
    """

    print("\n=== regex ===")
    emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)
    print(f"  Emails: {emails}")

    phones = re.findall(r"0\d{9}", text)
    print(f"  Phones: {phones}")

    urls = re.findall(r"https?://[\w./-]+", text)
    print(f"  URLs: {urls}")

    # Validate email
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    test_emails = ["valid@email.com", "invalid@", "bad.email"]
    for e in test_emails:
        valid = bool(re.match(email_pattern, e))
        print(f"  '{e}' valid={valid}")


if __name__ == "__main__":
    demo_datetime()
    demo_regex()
