# Phishing — lý thuyết phòng thủ chi tiết (người mới)

> Đọc xong file này bạn phải giải thích được cho người khác: phishing là gì, red flags, và 4 việc cần làm khi nghi ngờ.

## 1. Định nghĩa

**Phishing** là hình thức lừa đảo kỹ thuật số: kẻ tấn công **giả danh** bên đáng tin (ngân hàng, công ty, đồng nghiệp, cơ quan) để bạn:

- Tự cung cấp mật khẩu, OTP, thẻ tín dụng, hoặc
- Mở file/link độc, hoặc
- Thực hiện hành động có lợi cho chúng (chuyển tiền)

Khác brute-force (đoán mật khẩu): phishing thắng khi **con người tin nhầm**.

## 2. Các biến thể thường gặp (chỉ để nhận diện)

| Loại | Đặc điểm | Ví dụ nhận biết |
|------|----------|-----------------|
| Email phishing | Gửi hàng loạt | Domain From lạ, lỗi chính tả, đe dọa khóa tài khoản |
| Spear phishing | Nhắm cá nhân/công ty | Biết tên bạn, dự án, sếp |
| Smishing | Qua SMS | Link rút gọn + “phạt nguội”, “hoàn thuế” |
| Vishing | Qua điện thoại | Giả bank call center hỏi OTP |
| Quishing | QR code giả | QR trên poster/email dẫn domain lạ |

Bạn **không** cần dựng trang giả để học — chỉ cần nhận ra.

## 3. Giải phẫu một URL giả

Ví dụ nguy hiểm (lab):

```text
https://google.com@evil-phish.tk/steal
```

- Phần trước `@` dễ khiến mắt đọc “google.com”
- Trình duyệt thực tế có thể điều hướng tới host **sau** `@` → `evil-phish.tk`

Ví dụ khác:

```text
https://paypal-secure-update.xyz/confirm-password
```

- Có chữ “paypal” nhưng đuôi `.xyz` + “secure-update” là cụm hay dùng để tạo cảm giác khẩn

**Thói quen vàng:** nhìn **hostname thật** (phần giữa scheme và path), không nhìn chữ trên nút bấm.

## 4. Giải phẫu email giả

Các tín hiệu trong lab `data/sample_emails.txt`:

1. `From:` dùng TLD đáng ngờ  
2. Subject chữ HOA + URGENT  
3. Body đe dọa thời hạn  
4. Link `http://` (không mã hóa) tới domain lạ  
5. Yêu cầu gift card  

Email GitHub giả lập “an toàn” hơn: không đe dọa, trỏ về `github.com`, khuyên tự vào Settings.

## 5. Heuristics trong code lab nghĩa là gì?

Hàm `analyze_phishing_url` cộng điểm khi thấy:

- IP thay domain  
- TLD trong danh sách đáng ngờ  
- Keyword (`verify-account`, `confirm-password`…)  
- `@` trong URL  
- Subdomain quá sâu / giống brand  

**Điểm cao ≠ chắc chắn phishing 100%**, điểm thấp ≠ chắc chắn an toàn.  
Đó là **bài tập nhận thức**. Hệ thống thật dùng threat intel, sandbox, DMARC/DKIM/SPF, ML…

## 6. Lớp phòng thủ (người + kỹ thuật)

```
Con người: nghi ngờ → verify kênh chính thức → MFA
     +
Email: SPF/DKIM/DMARC, filter phishing, báo cáo nút "Report"
     +
Trình duyệt: Safe Browsing, cảnh báo certificate
     +
Ứng dụng: không để bị nhúng iframe lạ (X-Frame-Options/CSP)
     +
Tổ chức: training định kỳ, simulated phishing nội bộ (có quy trình HR/Legal)
```

## 7. Checklist 60 giây khi nhận link lạ

- [ ] Tôi có đang được **dọa** làm gấp không?  
- [ ] Domain có đúng thương hiệu chính thức không?  
- [ ] Tôi có mở bằng bookmark thay vì click không?  
- [ ] Có yêu cầu OTP / gift card / cài app lạ không?  
- [ ] Nếu đã nhập pass → đổi pass + MFA + báo IT  

## 8. Bài tự kiểm tra (không cần máy)

Giải thích miệng (hoặc viết):

1. Vì sao “giống logo ngân hàng” vẫn có thể là giả?  
2. MFA giúp gì khi đã bị phishing mật khẩu? (và MFA còn bị bypass kiểu nào — OTP fatigue / session — ở mức khái niệm)  
3. Khác nhau giữa training nhân viên và security headers trên web app?
