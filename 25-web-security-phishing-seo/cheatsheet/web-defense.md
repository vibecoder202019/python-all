# Module 25 cheatsheet — nhớ nhanh

## Học trước

README → docs/01 phishing → docs/04 OWASP → docs/02 Search

## Red flags phishing

- Hover link → xem **hostname** thật
- Không nhập mật khẩu từ email “khẩn”
- Domain `.xyz/.tk/.click`, IP thay domain, `@` trong URL
- Yêu cầu gift card / crypto / OTP qua điện thoại lạ
- Báo cáo: nhà cung cấp email / IT / Safe Browsing

## Security headers (tối thiểu)

```
Strict-Transport-Security
Content-Security-Policy
X-Frame-Options: DENY|SAMEORIGIN
X-Content-Type-Options: nosniff
Referrer-Policy
Permissions-Policy
```

## Ranking drop triage (site của bạn)

1. GSC **Security Issues**? → cleanup + Request Review  
2. **Manual Actions**? → sửa + reconsideration  
3. Coverage/indexing lỗi? → technical SEO  
4. Sau Core Update? → chất lượng nội dung (không panic)  

## Lệnh lab

```bash
bash scripts/setup.sh
bash scripts/02-run-all-examples.sh
bash scripts/03-run-project.sh
TARGET=https://staging.YOUR_DOMAIN bash scripts/04-self-check-headers.sh
```

## Self-test site của bạn

`docs/03-authorized-self-assessment.md` — ZAP, Nuclei, Lighthouse, GSC.

## Không làm

- Phishing / steal credential người khác  
- Hack / spam / cloaking để đẩy đối thủ rớt Google  
