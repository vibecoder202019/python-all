# Authorized self-assessment — Tools kiểm thử **site của bạn**

> Chỉ quét / test domain **bạn sở hữu** hoặc có **văn bản ủy quyền**. Ưu tiên môi trường **staging**. Không dùng các lệnh dưới đây lên site người khác.

Mục tiêu kép:

1. **Bảo mật** — tìm lỗ hổng trước khi kẻ xấu tìm thấy  
2. **Tối ưu** — hiệu năng, SEO kỹ thuật, trải nghiệm (Core Web Vitals)

---

## Bản đồ tools (chọn theo mục tiêu)

| Mục tiêu | Tool | Miễn phí? | Ghi chú |
|----------|------|-----------|---------|
| Crawl + XSS/SQLi cơ bản (UI) | **OWASP ZAP** | Có | Chuẩn lab / DevSecOps |
| Scan template CVE / misconfig | **Nuclei** | Có | Nhanh, nhiều template |
| Header / TLS / HTTP basics | **curl** + **testssl.sh** / SSL Labs | Có | Không cần agent nặng |
| Port / service expose | **nmap** | Có | Chỉ IP/host của bạn |
| Perf + a11y + SEO tips | **Lighthouse** (Chrome) | Có | Tối ưu trang |
| Index / phạt / coverage | **Google Search Console** | Có | “Rớt top” thật |
| Crawl SEO kỹ thuật | **Screaming Frog** / **wget**/custom | Freemium | Broken link, redirect |
| Proxy thủ công (học sâu) | **Burp Suite Community** | Có (limit) | Intercept request |
| CMS WordPress | **WPScan** | Có | Chỉ WP của bạn |

Python trong Module 25 (`examples/`) bổ sung heuristics — **không thay** scanner chuyên dụng ở trên.

---

## 0. Chuẩn bị an toàn

```bash
# Ghi rõ scope
export TARGET="https://staging.your-domain.com"   # KHÔNG dùng production nếu chưa sẵn sàng
export OWNED_HOST="staging.your-domain.com"

# Backup DB + code trước khi scan nặng (ZAP active / Nuclei aggressive)
# Rate limit: tránh làm sập site — dùng -rate, delay
```

Checklist trước khi quét:

- [ ] Đây là domain/IP của bạn hoặc có ticket/email ủy quyền  
- [ ] Staging hoặc maintenance window đã thông báo  
- [ ] WAF/CDN (Cloudflare…) — whitelist IP máy scan nếu cần  
- [ ] Không chạy DoS / flood cố ý  

---

## 1. OWASP ZAP — lỗ hổng web (khuyến nghị bắt đầu)

### Cài

```bash
# macOS (Homebrew)
brew install --cask zap

# hoặc Docker
docker pull ghcr.io/zaproxy/zaproxy:stable
```

### Baseline scan (an toàn hơn, passive + light)

```bash
docker run --rm -v "$(pwd):/zap/wrk:rw" ghcr.io/zaproxy/zaproxy:stable \
  zap-baseline.py -t "$TARGET" -r zap-report.html
```

Mở `zap-report.html` → ưu tiên **High/Medium**: XSS, SQLi, missing headers, open redirect.

### UI (học thủ công)

1. Mở ZAP → Automated Scan → dán `$TARGET`  
2. Bật **Traditional Spider** trước; Active Scan chỉ khi đã hiểu rủi ro  
3. Xem Alerts → Evidence → Remediation  

**Cách tối ưu từ kết quả ZAP:** thêm CSP/HSTS, sửa reflected XSS, parameterized query (xem Module 16 + 25 ví dụ 03–04).

---

## 2. Nuclei — misconfiguration & CVE phổ biến

```bash
# Cài (Go) hoặc binary từ GitHub projectdiscovery/nuclei
brew install nuclei

nuclei -update-templates

# Scan nhẹ — tech detect + exposures
nuclei -u "$TARGET" -severity http/misconfiguration,http/exposures \
  -rate-limit 50 -o nuclei-findings.txt

# Chỉ thông tin / low trước
nuclei -u "$TARGET" -severity http/technologies -severity-severity info
```

Đọc `nuclei-findings.txt`: file `.env` lộ, panel admin mở, version cũ → patch.

---

## 3. nmap — bề mặt mạng (host của bạn)

```bash
# Chỉ host/IP bạn sở hữu
nmap -sV -sC -p 80,443,8080,8443 "$OWNED_HOST" -oN nmap-web.txt
```

Nếu thấy port DB (5432, 3306) **public** → đóng firewall / Security Group ngay.

---

## 4. TLS & security headers

```bash
# Headers
curl -sI "$TARGET" | grep -iE 'strict-transport|content-security|x-frame|x-content|referrer|permissions'

# Lab Module 25
python3 examples/03_security_headers_check.py
```

Online (site của bạn): [SSL Labs Server Test](https://www.ssllabs.com/ssltest/) — dán hostname.

Mục tiêu tối ưu: grade A, HSTS bật, không TLS 1.0/1.1.

---

## 5. Lighthouse — tốc độ & SEO kỹ thuật

### Chrome DevTools

1. Mở trang (Incognito) → F12 → **Lighthouse**  
2. Categories: Performance, Accessibility, Best Practices, SEO  
3. Device: Mobile + Desktop  

### CLI

```bash
npm install -g lighthouse
lighthouse "$TARGET" --view --output html --output-path ./lighthouse-report.html
```

**Tối ưu thường gặp từ báo cáo:**

| Issue | Hướng xử lý |
|-------|-------------|
| LCP chậm | Nén ảnh WebP, preload hero, CDN |
| CLS | Giữ kích thước ảnh/ads cố định |
| Unused JS | Code-split, bỏ lib thừa |
| SEO: missing description | Meta description, title duy nhất |
| robots / canonical | Kiểm tra không `noindex` nhầm production |

---

## 6. Google Search Console — “rớt top” thật

1. Xác minh quyền sở hữu domain  
2. **Security Issues** → nếu có malware/phishing inject → cleanup (Module 25 lab 03)  
3. **Manual Actions** → sửa + Request review  
4. **Pages** (Indexing) → lỗi 404/soft-404/redirect  
5. **Core Web Vitals** → đối chiếu Lighthouse  
6. **Performance** → query mất impression sau update  

Không cần tool “đánh SEO đối thủ” — GSC + nội dung chất lượng là đủ cho chủ site.

---

## 7. Crawl SEO kỹ thuật (broken link / redirect)

```bash
# Nhanh: liệt kê link hỏng (staging)
wget --spider -r -nd -nv -l 3 "$TARGET" 2>&1 | tee crawl-spider.txt
# hoặc dùng Screaming Frog GUI: Mode → Spider → Start
```

Sửa 404 nội bộ, chuỗi redirect dài, mixed HTTP/HTTPS.

---

## 8. Burp Suite Community (học request thủ công)

1. Cấu hình browser proxy `127.0.0.1:8080`  
2. Bật Intercept → sửa parameter trên **form login staging**  
3. Repeater: thử input `' OR 1=1` **trên staging** để xem app có parameterized query không  
4. Không brute-force production  

Kết hợp Module 25 `sanitize_user_input` / Module 16 SQLi guard để hiểu lớp phòng thủ.

---

## 9. WordPress (nếu site WP của bạn)

```bash
# API token từ wpscan.com (free tier) khuyến nghị
wpscan --url "$TARGET" --enumerate vp,vt,u --plugins-detection mixed
```

Cập nhật core/plugin, xóa plugin bỏ, hạn chế `xmlrpc` nếu không cần.

---

## Quy trình đề xuất (1 buổi)

```
1. Backup + xác nhận TARGET = staging của bạn
2. curl -I + headers + SSL Labs
3. Lighthouse (perf/SEO)
4. ZAP baseline
5. Nuclei misconfig/exposures
6. (Tuỳ) nmap ports
7. GSC: Security / Indexing / CWV
8. Sửa P0 (lộ secret, XSS, port DB) → P1 (headers, LCP) → P2 (SEO meta)
9. Quét lại để xác nhận hết alert quan trọng
```

---

## Kết nối Module 25

```bash
bash scripts/02-run-all-examples.sh   # heuristics phishing/headers/SEO triage
bash scripts/03-run-project.sh
```

Dùng báo cáo ZAP/Nuclei/Lighthouse làm input thật; dùng Python lab để **học phân loại** rủi ro và checklist khôi phục ranking khi site từng bị hack.

---

## Không khuyến nghị (self-test cũng hại)

- Flood / stress test không kiểm soát trên production  
- Active exploit public PoC “vào shell” trên prod có dữ liệu user  
- Tool black-hat SEO (PBNs, cloaking, negative SEO) — vừa rủi ro pháp lý vừa dễ tự hại ranking  

---

## Tài liệu chính thức

- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)  
- [OWASP ZAP Docs](https://www.zaproxy.org/docs/)  
- [ProjectDiscovery Nuclei](https://docs.projectdiscovery.io/tools/nuclei/overview)  
- [web.dev / Lighthouse](https://developer.chrome.com/docs/lighthouse/overview)  
- [Google Search Central](https://developers.google.com/search)
