# OWASP & harden web — lý thuyết cho người mới

> Đọc trước khi chạy `examples/03` và `04`. Mục tiêu: hiểu *vì sao* cần escape/header, không chỉ chạy tool.

## 1. Request–response trong đầu người mới

```
Browser gửi:  GET /search?q=hello
Server trả:   200 OK + HTML + Headers
```

- **Input** nguy hiểm nằm ở query, form, JSON body, header…  
- **Output** nguy hiểm khi server **in lại** input thiếu escape  
- **Headers** là chỉ thị kèm theo cho browser

Hacker / bug = lợi dụng chỗ app tin input quá mức.

## 2. SQL Injection — câu chuyện ngắn

Giả sử login viết (sai):

```sql
SELECT id FROM users WHERE user='" + user + "' AND pass='" + pass + "'
```

Nếu `user` = `admin'--` phần mật khẩu có thể bị comment hóa tùy DB.

**Cách đúng:** truyền tham số riêng (`?` / `%s`), thư viện driver bind giá trị — SQL và dữ liệu tách nhau.

Lab chỉ **nhận diện chuỗi giống tấn công** để bạn quen mặt payload — production vẫn dựa parameterized query là chính.

## 3. XSS — câu chuyện ngắn

Comment:

```html
<script>/* đánh cắp cookie */</script>
```

Nếu trang hiện comment bằng `innerHTML` / template không escape → nạn nhân khác mở trang là chạy script.

**Escape** biến `<script>` thành text vô hại.  
**CSP** thêm lớp: browser từ chối script inline/lạ dù XSS lọt.

## 4. Clickjacking & phishing UI

Trang ác nhúng site ngân hàng trong iframe trong suốt, lừa bạn click “Có”.  
`X-Frame-Options: DENY` hoặc CSP `frame-ancestors` giúp site **không chịu** bị nhúng bừa.

## 5. Thứ tự ưu tiên harden (thực tế)

1. HTTPS mọi nơi + HSTS  
2. Parameterized query / ORM  
3. Escape output + CSP  
4. Cookie: `Secure`, `HttpOnly`, `SameSite`  
5. Rate limit login (chống brute-force)  
6. Cập nhật CMS/plugin  
7. Headers còn lại + WAF  

## 6. Liên hệ lab Module 25

| Ví dụ | Khái niệm |
|-------|-----------|
| 03 security headers | Checklist header |
| 04 sanitizer | Phát hiện pattern + `html.escape` |

Sang Module 16 để harden trên Ingress/K8s; Module 26 để **bắt** MD5/SQLi pattern trên CI trước khi merge.
