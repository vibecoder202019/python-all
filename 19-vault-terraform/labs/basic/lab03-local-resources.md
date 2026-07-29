# Lab 03 — Local resources, count & for_each (Basic)

**Thời gian:** 45 phút

## Bài tập

1. Apply `terraform/03-local-resources`
2. So sánh file `count-*` vs `fe-*` trong `output/`
3. Sửa list `users` — thêm `dave`, apply lại — quan sát `for_each` chỉ tạo file mới
4. Trả lời: Khi n nào nên dùng `for_each` thay `count`?

## Gợi ý

`for_each` ổn định hơn khi xóa phần tử giữa list — tránh recreate sai resource.
