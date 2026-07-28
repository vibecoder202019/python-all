"""
Module 01 — Ví dụ 1: Biến và Kiểu dữ liệu
Chạy: python examples/01_bien_va_kieu_du_lieu.py

YÊU CẦU ĐỀ BÀI:
  - Khai báo biến với các kiểu cơ bản: str, int, float, bool
  - Ép kiểu giữa str và int
  - Dùng các toán tử số học (+, -, *, /, //, %, **)
  - Thao tác chuỗi: strip, upper, split, slice
  - Kiểm tra kiểu dữ liệu bằng type()

KẾT QUẢ MONG ĐỢI (khi chạy):
  - In thông tin cá nhân (tên, tuổi, lương, trạng thái)
  - Hiển thị kết quả ép kiểu "42" → 42 và 3.14159 → "3.14159"
  - In kết quả toán tử với a=17, b=5
  - Demo các phương thức chuỗi và slice
  - Liệt kê kiểu của [42, 3.14, "hello", True, None]
"""

# ── Biến cơ bản ──
name = "Nguyễn Văn A"
age = 28
salary = 15_000_000.50  # dùng _ để dễ đọc số lớn
is_employed = True

print("=== Thông tin cá nhân ===")
print(f"Tên: {name}")
print(f"Tuổi: {age} (kiểu: {type(age).__name__})")
print(f"Lương: {salary:,.0f} VND")
print(f"Đang làm việc: {is_employed}")

# ── Ép kiểu ──
text_number = "42"
number = int(text_number)  # chuyển chuỗi số → int
print(f"\nÉp kiểu '{text_number}' → {number} (int)")

pi_str = str(3.14159)  # chuyển float → chuỗi
print(f"Ép kiểu 3.14159 → '{pi_str}' (str)")

# ── Toán tử ──
a, b = 17, 5
print(f"\n=== Toán tử: a={a}, b={b} ===")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b:.2f}")
print(f"a // b = {a // b}  (chia nguyên)")
print(f"a % b = {a % b}   (modulo)")
print(f"a ** 2 = {a ** 2}")

# ── Chuỗi ──
message = "  Python là ngôn ngữ mạnh mẽ  "
print(f"\n=== Chuỗi ===")
print(f"Gốc: '{message}'")
print(f"strip(): '{message.strip()}'")
print(f"upper(): '{message.strip().upper()}'")
print(f"split(): {message.strip().split()}")
print(f"Ký tự đầu: '{message.strip()[0]}'")
print(f"Slice [0:6]: '{message.strip()[0:6]}'")  # lấy 6 ký tự đầu

# ── Kiểm tra kiểu ──
values = [42, 3.14, "hello", True, None]
print(f"\n=== Kiểm tra kiểu ===")
for v in values:
    print(f"  {repr(v):15} → {type(v).__name__}")
