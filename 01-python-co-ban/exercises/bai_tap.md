# Bài tập Module 01: Python Cơ bản

Làm từng bài theo thứ tự. Tạo file Python riêng cho mỗi bài trong thư mục `exercises/`.

---

## Bài 1: Máy tính BMI (Dễ)

Viết hàm `bmi_calculator(weight_kg, height_m)` trả về:
- BMI (float, làm tròn 1 chữ số thập phân)
- Phân loại: "Thiếu cân" / "Bình thường" / "Thừa cân" / "Béo phì"

**Input mẫu:** `bmi_calculator(70, 1.75)`  
**Output mong đợi:** `(22.9, "Bình thường")`

---

## Bài 2: FizzBuzz (Dễ)

In các số từ 1 đến 100:
- Chia hết cho 3 → in "Fizz"
- Chia hết cho 5 → in "Buzz"
- Chia hết cho cả 3 và 5 → in "FizzBuzz"
- Còn lại → in số đó

---

## Bài 3: Đếm nguyên âm (Trung bình)

Viết hàm `count_vowels(text: str) -> int` đếm số nguyên âm (a, e, i, o, u) trong chuỗi, không phân biệt hoa thường.

**Input:** `"Hello World"`  
**Output:** `3`

---

## Bài 4: Tìm số nguyên tố (Trung bình)

Viết hàm `is_prime(n: int) -> bool` kiểm tra số nguyên tố.

Sau đó dùng list comprehension tìm tất cả số nguyên tố từ 2 đến 100.

---

## Bài 5: Thống kê điểm thi (Trung bình)

Cho list điểm: `scores = [85, 92, 78, 95, 60, 88, 73, 91, 55, 82]`

Viết hàm `score_stats(scores)` trả về dict:
```python
{
    "count": 10,
    "average": 80.9,
    "max": 95,
    "min": 55,
    "passed": 8,      # điểm >= 50
    "excellent": 3    # điểm >= 90
}
```

---

## Bài 6: Mã hóa Caesar (Khó)

Viết hàm `caesar_cipher(text: str, shift: int) -> str` mã hóa Caesar cipher.

**Input:** `caesar_cipher("Hello", 3)`  
**Output:** `"Khoor"`

Viết thêm hàm giải mã `caesar_decipher`.

---

## Bài 7: Xử lý danh sách sinh viên (Khó)

Cho list dict:
```python
students = [
    {"name": "An", "scores": [85, 90, 78]},
    {"name": "Bình", "scores": [92, 88, 95]},
    {"name": "Chi", "scores": [70, 65, 80]},
]
```

Viết hàm trả về list sinh viên có điểm trung bình >= 80, sắp xếp giảm dần theo điểm TB.

**Output mong đợi:**
```
[
    {"name": "Bình", "average": 91.67},
    {"name": "An", "average": 84.33},
]
```

---

## Tiêu chí hoàn thành

- [ ] Làm được bài 1-3 không cần xem đáp án
- [ ] Làm được bài 4-5
- [ ] Thử bài 6-7 (không bắt buộc)

Đáp án: [solutions/](solutions/)
