"""
Module 01 — Ví dụ 4: List Comprehension
Chạy: python examples/04_list_comprehension.py

YÊU CẦU ĐỀ BÀI:
  - Tạo list bình phương bằng list comprehension
  - Lọc phần tử có điều kiện (số chẵn)
  - Dùng nested comprehension tạo ma trận và flatten
  - Dùng dict/set comprehension
  - Xử lý dữ liệu thực tế: strip, lower, lọc rỗng
  - So sánh hiệu suất list comp vs vòng lặp for

KẾT QUẢ MONG ĐỢI (khi chạy):
  - Bình phương 1-10: [1, 4, 9, ..., 100]
  - Số chẵn 0-19
  - Ma trận 3x3 và danh sách phẳng (flatten)
  - Dict độ dài từ và set độ dài duy nhất
  - Dữ liệu cleaned sau strip/lower
  - Thời gian chạy: list comp nhanh hơn vòng lặp for
"""

# ── Cơ bản ──
squares = [x ** 2 for x in range(1, 11)]
print(f"Bình phương 1-10: {squares}")

# ── Có điều kiện ──
evens = [x for x in range(20) if x % 2 == 0]  # chỉ lấy số chia hết cho 2
print(f"Số chẵn 0-19: {evens}")

# ── Nested comprehension — ma trận ──
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"\nMa trận 3x3:")
for row in matrix:
    print(f"  {row}")

# ── Flatten ma trận ──
flat = [num for row in matrix for num in row]  # duyệt 2 cấp: hàng rồi phần tử
print(f"Flatten: {flat}")

# ── Dict comprehension ──
words = ["python", "java", "go", "rust"]
word_lengths = {word: len(word) for word in words}
print(f"\nDict comprehension: {word_lengths}")

# ── Set comprehension ──
unique_lengths = {len(word) for word in words}  # set loại bỏ trùng lặp
print(f"Set comprehension: {unique_lengths}")

# ── Thực tế: xử lý dữ liệu ──
raw_data = ["  hello  ", "WORLD", "  Python  ", "", "  AI  "]
cleaned = [s.strip().lower() for s in raw_data if s.strip()]  # bỏ chuỗi rỗng sau strip
print(f"\nDữ liệu gốc:  {raw_data}")
print(f"Sau xử lý:   {cleaned}")

# ── So sánh hiệu suất (list comp vs loop) ──
import time

n = 1_000_000

start = time.perf_counter()
result_loop = []
for x in range(n):
    result_loop.append(x ** 2)
time_loop = time.perf_counter() - start

start = time.perf_counter()
result_comp = [x ** 2 for x in range(n)]
time_comp = time.perf_counter() - start

print(f"\n=== Hiệu suất (n={n:,}) ===")
print(f"  Vòng lặp for:     {time_loop:.4f}s")
print(f"  List comprehension: {time_comp:.4f}s")
