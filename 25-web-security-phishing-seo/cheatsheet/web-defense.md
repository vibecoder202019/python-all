# Phishing defense

- Hover link → xem domain thật trước khi click
- Không nhập mật khẩu từ email “khẩn”
- Báo cáo: Google Safe Browsing / nhà cung cấp email / CERT

# Security headers (tối thiểu)

```
Strict-Transport-Security
Content-Security-Policy
X-Frame-Options: DENY|SAMEORIGIN
X-Content-Type-Options: nosniff
Referrer-Policy
Permissions-Policy
```

# Ranking drop triage (site của bạn)

1. Search Console → **Security Issues**? → cleanup + Request Review  
2. **Manual Actions**? → sửa + reconsideration  
3. Coverage/indexing lỗi hàng loạt? → technical SEO  
4. Sau Core Update? → chất lượng nội dung (không panics)  

# Lệnh lab

```bash
bash scripts/setup.sh
bash scripts/02-run-all-examples.sh
bash scripts/03-run-project.sh
TARGET=https://staging.YOUR_DOMAIN bash scripts/04-self-check-headers.sh
```

# Self-test site của bạn

Chi tiết: `docs/03-authorized-self-assessment.md` — ZAP, Nuclei, Lighthouse, GSC, nmap.

# Không làm

- Phishing / steal credential người khác  
- Hack / spam / cloaking để đẩy đối thủ rớt Google  
