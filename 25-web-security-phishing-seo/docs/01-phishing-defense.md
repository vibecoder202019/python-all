# Phishing — phòng thủ & nhận diện

## Phishing là gì?

Kẻ tấn công **giả mạo** thương hiệu / đồng nghiệp để lừa bạn tiết lộ mật khẩu, OTP, hoặc chuyển tiền.

## Red flags thường gặp

- Domain gần giống (`paypa1`, `secure-update.xyz`)
- IP thay vì tên miền
- Ngôn ngữ gấp: “trong 24h tài khoản bị khóa”
- Link display text khác domain thật
- Yêu cầu gift card / crypto / wire

## Việc nên làm

1. Mở trang login bằng bookmark / gõ domain chính thức  
2. Bật MFA  
3. Báo cáo email phishing cho IT / nhà cung cấp mail  
4. Nếu đã nhập mật khẩu → đổi ngay + revoke session  

## Trong lab

`analyze_phishing_url` / `analyze_email_text` chỉ là **heuristics giáo dục** — không thay Safe Browsing / email gateway doanh nghiệp.
