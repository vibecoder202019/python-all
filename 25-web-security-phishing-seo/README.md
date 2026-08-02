# Module 25: Web Security — Phishing Defense, OWASP & Google Search Integrity

Học **phòng thủ** web: nhận diện phishing, hardening chống tấn công phổ biến, và **bảo vệ / khôi phục xếp hạng Google** khi site của bạn bị hack hoặc bị phạt.

> **Đạo đức & pháp lý (bắt buộc đọc)**  
> Module này chỉ phục vụ **bảo vệ hệ thống của bạn**, lab local, và nhận thức người dùng.  
> **Không** hướng dẫn phishing thật, credential theft, tấn công site người khác, hay black-hat SEO để đẩy đối thủ rớt hạng.  
> Lạm dụng kỹ thuật để hại bên thứ ba là **vi phạm pháp luật**.

**Liên quan:** [Module 16 K8s Security](../16-k8s-security/README.md) (WAF/phishing trên cluster) · [Module 12 DevSecOps](../12-python-devops-devsecops/README.md)

---

## Mục tiêu

| Chủ đề | Bạn học được |
|--------|----------------|
| **Phishing** | Phân tích URL/email giả mạo, red flags, báo cáo |
| **Tấn công web (OWASP)** | Hiểu vector phổ biến → harden input, headers, auth |
| **Google Search Integrity** | Vì sao **site của bạn** rớt hạng; triage Security Issues; khôi phục |

---

## Vì sao site “rớt top Google”? (góc nhìn chủ site)

Google **không** “bị đánh SEO” theo kiểu bạn gõ lệnh — ranking thay đổi vì tín hiệu chất lượng / an toàn. Với site **của bạn**, các nguyên nhân phổ biến:

| Nguyên nhân | Dấu hiệu | Hướng xử lý (phòng thủ) |
|-------------|----------|-------------------------|
| Site bị hack → spam / malware / phishing page | Search Console **Security Issues**, URL lạ, redirect | Quét malware, xóa backdoor, đổi credential, Request Review |
| Manual Action (spam, cloaking, scraped content) | Manual Actions trong GSC | Gỡ nội dung spam, sửa cloaking, submit reconsideration |
| Core / spam update | Traffic giảm sau update, không có Security Issue | Cải thiện E-E-A-T, bỏ thin/spam content |
| Technical SEO xấu | Indexing errors, robots chặn nhầm | Sửa robots/sitemap, crawl budget, Core Web Vitals |
| Brand / reputation | Review xấu, phishing mạo danh brand | DMCA/abuse report, domain monitoring |

Lab trong module mô phỏng **audit / triage** trên dữ liệu giả — không tấn công Google hay site ngoài.

---

## Kiến trúc lab

```
URL / Email mẫu (data/)
        │
        ▼
┌─────────────────────────┐
│ Phishing analyzer       │  heuristics URL + header email
├─────────────────────────┤
│ Security headers check  │  CSP, HSTS, X-Frame-Options…
├─────────────────────────┤
│ Input sanitizer (OWASP) │  SQLi / XSS pattern (defense)
├─────────────────────────┤
│ SEO integrity audit     │  robots, sitemap, spam signals
└─────────────────────────┘
        │
        ▼
  Báo cáo triage (JSON / console)
```

---

## Chạy nhanh

```bash
cd learn-python-ai
bash 25-web-security-phishing-seo/scripts/setup.sh
bash 25-web-security-phishing-seo/scripts/01-check-prerequisites.sh
bash 25-web-security-phishing-seo/scripts/02-run-all-examples.sh
bash 25-web-security-phishing-seo/scripts/03-run-project.sh
```

Manual từng lệnh: [readme_manual.md](readme_manual.md)

---

## Lộ trình lab

| Lab | Nội dung |
|-----|----------|
| [01](labs/01-phishing-awareness.md) | Nhận diện phishing URL/email |
| [02](labs/02-owasp-hardening.md) | Hardening input + security headers |
| [03](labs/03-search-integrity-recovery.md) | Triage ranking drop & recovery checklist |
| [04](labs/04-self-assessment-toolkit.md) | Tự quét **site của bạn** (ZAP/Nuclei/Lighthouse…) |

Docs: [docs/01-phishing-defense.md](docs/01-phishing-defense.md) · [docs/02-google-search-integrity.md](docs/02-google-search-integrity.md) · [docs/03-authorized-self-assessment.md](docs/03-authorized-self-assessment.md)

---

## Cấu trúc

```
25-web-security-phishing-seo/
├── data/                 # URL/email mẫu (lab only)
├── examples/             # 6 ví dụ Python
├── project/              # Pipeline audit end-to-end
├── labs/
├── docs/
├── scripts/
├── cheatsheet/
├── README.md
└── readme_manual.md
```

---

## FAQ

**Khác Module 16 thế nào?**  
16 = WAF + NetworkPolicy trên **K8s**. 25 = phishing awareness sâu hơn + OWASP hardening + **Search Console / ranking recovery** cho chủ site.

**Có cần Google Search Console API?**  
Không bắt buộc. Lab dùng fixture JSON mô phỏng Security Issues / Manual Actions.

**Teardown**

```bash
bash scripts/06-teardown.sh
```

---

[readme_manual.md](readme_manual.md) | [cheatsheet/web-defense.md](cheatsheet/web-defense.md)
