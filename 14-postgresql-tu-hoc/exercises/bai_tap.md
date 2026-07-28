# Bài tập — Module 14: PostgreSQL

Làm sau khi chạy xong `scripts/setup.sh` và các ví dụ. Mở `scripts/psql_shell.sh` hoặc dùng `python scripts/run_sql.py`.

---

## Cơ bản (SQL)

### Bài 1 — CRUD
Tạo bảng `genres` (id, name) và bảng `book_genres` (book_id, genre_id). Thêm 3 thể loại, gán thể loại cho ít nhất 2 sách trong schema `demo`.

### Bài 2 — JOIN
Viết query trả về: tên sách, tác giả, thể loại (nếu có), sắp xếp theo thể loại rồi tên sách.

### Bài 3 — Aggregation
Viết query: mỗi quốc gia có bao nhiêu tác giả, bao nhiêu sách, giá trung bình.

---

## Trung bình (Functions)

### Bài 4 — Function đếm
Viết function `fn_genre_count(p_genre_name VARCHAR)` trả về số sách thuộc thể loại đó.

### Bài 5 — Function mượn/trả (library)
Trong schema `library`, viết function `fn_member_can_borrow(p_member_id INTEGER)` trả về `TRUE` nếu thành viên active và đang mượn < 3 sách.

### Bài 6 — Function trả TABLE
Viết function `fn_overdue_loans()` trả về danh sách loan quá hạn: book title, member name, số ngày quá hạn.

---

## Nâng cao (Triggers & Views)

### Bài 7 — Trigger validate
Tạo trigger trên `library.members`: không cho `UPDATE email` thành email đã tồn tại ở member khác.

### Bài 8 — Trigger audit books
Tạo trigger ghi vào `library.audit_log` khi `INSERT` hoặc `DELETE` trên bảng `books`.

### Bài 9 — Materialized View
Tạo materialized view `mv_monthly_loans` thống kê số lượt mượn theo tháng (year-month). Viết lệnh `REFRESH`.

### Bài 10 — Python
Viết script Python gọi `fn_borrow_book`, in kết quả, và xử lý exception khi hết sách (dùng try/except).

---

## Gợi ý chấm tự học

| Bài | Kiểm tra nhanh |
|-----|----------------|
| 1–3 | `SELECT * FROM demo.genres;` |
| 4 | `SELECT fn_genre_count('Tiểu thuyết');` |
| 5 | `SELECT fn_member_can_borrow(1);` |
| 6 | `SELECT * FROM fn_overdue_loans();` |
| 7 | Thử update email trùng → phải raise exception |
| 8 | Insert/delete book → có dòng audit |
| 9 | `REFRESH MATERIALIZED VIEW mv_monthly_loans;` |
| 10 | Chạy script, test case hết sách |

Đáp án tham khảo: thư mục `solutions/`.
