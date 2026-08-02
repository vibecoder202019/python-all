# Module 25: Web Security — Phishing Defense, OWASP & Google Search Integrity

Học **phòng thủ** web: nhận diện phishing, hardening chống tấn công phổ biến, và **bảo vệ / khôi phục xếp hạng Google** khi site của bạn bị hack hoặc bị phạt.

> **Đạo đức & pháp lý (bắt buộc đọc)**  
> Module này chỉ phục vụ **bảo vệ hệ thống của bạn**, lab local, và nhận thức người dùng.  
> **Không** hướng dẫn phishing thật, credential theft, tấn công site người khác, hay black-hat SEO để đẩy đối thủ rớt hạng.  
> Lạm dụng kỹ thuật để hại bên thứ ba là **vi phạm pháp luật**.

**Dành cho ai?** Người mới tự học — biết Python cơ bản (Module 01–05) là đủ để chạy lab.  
**Liên quan:** [Module 16](../16-k8s-security/README.md) · [Module 12](../12-python-devops-devsecops/README.md) · [Module 26](../26-devsecops-cicd-security/README.md)

---

## Mục tiêu

Sau module này bạn sẽ:

1. Giải thích được phishing hoạt động thế nào (không cần “làm phishing”)
2. Nhìn URL/email và chỉ ra **red flags**
3. Hiểu vài lỗ hổng web phổ biến (OWASP) và cách **harden**
4. Biết vì sao site **của bạn** có thể rớt hạng Google và quy trình triage/khôi phục
5. Chạy được bộ ví dụ Python + checklist tự kiểm tra site mình sở hữu

| Chủ đề | Bạn học được |
|--------|----------------|
| **Phishing** | Phân tích URL/email giả mạo, red flags, báo cáo |
| **Tấn công web (OWASP)** | Hiểu vector phổ biến → harden input, headers, auth |
| **Google Search Integrity** | Vì sao site rớt hạng; Security Issues; khôi phục |

---

## Cách tự học module này

1. Đọc hết **Lý thuyết nền tảng** bên dưới (đừng skip)
2. Đọc docs ngắn: [01](docs/01-phishing-defense.md) → [04](docs/04-owasp-hardening-theory.md) → [02](docs/02-google-search-integrity.md)
3. Chạy examples theo thứ tự 01 → 06 — mỗi file in kết quả, đối chiếu với lý thuyết
4. Làm labs 01 → 04
5. Chỉ khi đã hiểu defense mới xem [self-assessment tools](docs/03-authorized-self-assessment.md) trên **site của bạn**

```bash
cd learn-python-ai
bash 25-web-security-phishing-seo/scripts/setup.sh
bash 25-web-security-phishing-seo/scripts/02-run-all-examples.sh
bash 25-web-security-phishing-seo/scripts/03-run-project.sh
```

Chi tiết lệnh: [readme_manual.md](readme_manual.md)

---

## Lý thuyết nền tảng (đọc kỹ)

### 1. Web “không an toàn mặc định” nghĩa là gì?

Khi bạn mở trình duyệt vào một website:

```
Bạn (browser)  ──HTTPS──►  Server (HTML/JS/API/DB)
```

Ba bên có thể “đi lạc”:

| Bên | Rủi ro nếu bị lợi dụng |
|-----|-------------------------|
| **Người dùng** | Bị lừa nhập mật khẩu vào trang giả (phishing) |
| **Ứng dụng** | Input độc hại → XSS, SQL Injection… |
| **Server / CMS** | Bị hack → gắn spam/malware → Google cảnh báo, traffic giảm |

Module này dạy bạn **nhìn nhận và phòng**, không dạy tấn công.

**Ví von:** Khóa cửa nhà + biết nhận diện người giả danh shipper (phishing) + không để cửa sổ tầng trệt mở (lỗ hổng web) + nếu nhà bị đột nhập thì dọn và báo công an / bảo hiểm (khôi phục Search Console).

---

### 2. Phishing — lừa đảo bằng giả mạo

#### Phishing là gì?

**Phishing** = kẻ xấu **giả danh** tổ chức/người tin cậy (ngân hàng, Google, sếp, đồng nghiệp) để bạn:

- Gõ mật khẩu / OTP trên trang giả, hoặc
- Cài malware, hoặc
- Chuyển tiền / mua gift card

Họ **không cần phá mật khẩu mạnh** — họ khiến bạn **tự đưa** thông tin.

#### Chuỗi tấn công điển hình (để bạn nhận ra)

```
1. Bạn nhận email/SMS: “Tài khoản sẽ khóa trong 24h — bấm vào đây”
2. Link trông giống ngân hàng nhưng domain thật là paypal-secure.xyz
3. Trang login giả copy giao diện
4. Bạn nhập user/pass → dữ liệu gửi về server kẻ tấn công
5. Chúng đăng nhập tài khoản thật của bạn
```

#### Red flags (dấu hiệu đỏ) — học thuộc

| Red flag | Ví dụ | Vì sao nguy hiểm |
|----------|--------|------------------|
| Domain lạ / TLD rẻ | `.xyz`, `.tk`, `.click` | Dễ đăng ký hàng loạt để lừa |
| IP thay tên miền | `http://192.168.x.x/login` | Che tên thương hiệu thật |
| Ký tự `@` trong URL | `https://google.com@evil.tk/` | Trình duyệt có thể đưa bạn tới `evil.tk` |
| Brand trong subdomain giả | `microsoft-login-verify.click` | Trông quen mắt nhưng không phải Microsoft |
| Ngôn ngữ gấp / đe dọa | “khóa trong 24h” | Ép bạn không kịp suy nghĩ |
| Yêu cầu gift card / crypto | “mua thẻ gửi code” | Không công ty uy tín nào làm vậy |
| Link chữ khác domain | Chữ “Đăng nhập ngân hàng” → URL lạ | Phải hover xem URL thật |

#### Việc đúng khi nghi ngờ

1. **Không click** link trong email — mở bookmark / gõ tay `https://nganhang.com`
2. Bật **MFA** (xác thực 2 lớp)
3. Báo cáo cho IT / nhà cung cấp email
4. Nếu đã nhập mật khẩu → **đổi ngay**, revoke session, kiểm tra chuyển tiền

Trong lab, Python chỉ **chấm điểm heuristics** (quy tắc đơn giản). Nó giúp bạn học — **không thay** Google Safe Browsing hay anti-phishing doanh nghiệp.

Chi tiết thêm: [docs/01-phishing-defense.md](docs/01-phishing-defense.md)

---

### 3. OWASP & lỗ hổng web phổ biến (góc phòng thủ)

#### OWASP là gì?

**OWASP** (Open Worldwide Application Security Project) là cộng đồng xuất bản danh sách lỗ hổng web phổ biến (OWASP Top 10). Dev/Sec dùng danh sách này để biết **cần harden chỗ nào**.

Bạn chưa cần thuộc cả Top 10. Module này tập trung vài khái niệm gặp mọi ngày:

#### A) SQL Injection (SQLi) — hiểu ý tưởng

Ứng dụng ghép chuỗi SQL từ input người dùng:

```text
SELECT * FROM users WHERE name = ' + input + '
```

Nếu `input` = `' OR 1=1--` thì điều kiện luôn đúng → lộ dữ liệu.

**Chống (bắt buộc nhớ):**

- Dùng **parameterized query** / ORM (không nối chuỗi SQL)
- Validate / reject pattern nguy hiểm ở edge (WAF) — lớp phụ, không thay parameterized query

Lab: `examples/04_owasp_input_sanitizer.py` phát hiện pattern kiểu lab.

#### B) XSS (Cross-Site Scripting) — hiểu ý tưởng

Kẻ gửi HTML/JS độc vào ô comment. Nếu server **in lại nguyên** cho người khác xem, trình duyệt chạy JS → đánh cắp cookie phiên đăng nhập.

**Chống:**

- **Escape** output HTML (`<` → `&lt;` …)
- **CSP** (Content-Security-Policy) hạn chế script lạ
- HttpOnly cookie

#### C) Security headers — “lá chắn trình duyệt”

Server gửi kèm response một số header bảo mật. Trình duyệt **tuân thủ** chúng:

| Header | Việc nó làm (nói đơn giản) |
|--------|----------------------------|
| `Strict-Transport-Security` (HSTS) | Ép chỉ dùng HTTPS lần sau |
| `Content-Security-Policy` (CSP) | Chỉ cho phép script/ảnh từ nguồn tin cậy |
| `X-Frame-Options` | Chống nhúng site bạn vào iframe giả (clickjacking / phishing UI) |
| `X-Content-Type-Options: nosniff` | Không đoán nhầm loại file |
| `Referrer-Policy` | Giảm lộ URL khi click ra ngoài |
| `Permissions-Policy` | Tắt camera/mic nếu không cần |

Lab: `examples/03_security_headers_check.py` so sánh site “yếu” vs “đã harden”.

#### D) Defense in depth (nhiều lớp)

```
Người dùng được training (không click bừa)
        +
HTTPS + HSTS
        +
CSP + X-Frame-Options
        +
Validate + parameterized query + escape HTML
        +
WAF / rate limit (Module 16)
        +
CI scan (Module 26)
```

Một lớp hỏng vẫn còn lớp khác.

---

### 4. Google Search Integrity — vì sao site “rớt top”?

#### Hiểu đúng trước

Google **không** có nút “đánh SEO đối thủ” mà bạn học trong module này.  
Hạng thay đổi vì tín hiệu **chất lượng / an toàn / kỹ thuật** của **chính site bạn** (và cạnh tranh nội dung).

Khi traffic organic giảm, **đừng đoán bừa** — triage theo nhánh:

```
Traffic giảm?
    │
    ├─ Search Console có Security Issues? ──► Site có thể bị HACK / malware
    ├─ Có Manual Actions? ──────────────────► Vi phạm chính sách (spam, cloaking…)
    ├─ Indexing lỗi hàng loạt? ─────────────► Technical SEO (robots, 404…)
    ├─ Vừa có Core/Spam Update? ────────────► Chất lượng nội dung (E-E-A-T)
    └─ Không rõ ────────────────────────────► Kiểm tra Analytics, mùa vụ, tracking
```

#### Các nguyên nhân phổ biến (chủ site)

| Nguyên nhân | Dấu hiệu | Việc làm (phòng thủ) |
|-------------|----------|----------------------|
| Bị hack → spam / malware / trang phishing | Security Issues, URL lạ | Cleanup, đổi mật khẩu, Removals, Request Review |
| Manual Action | Báo cáo Manual Actions | Gỡ spam → reconsideration |
| Core / spam update | Giảm sau update, không Security Issue | Cải thiện nội dung, bỏ thin/AI-spam |
| Technical SEO | Coverage errors | Sửa robots/sitemap/canonical |
| Giả mạo thương hiệu | Domain/email giả brand bạn | Báo cáo abuse, giám sát domain |

#### E-E-A-T (hiểu nhanh)

Google đánh giá nội dung theo hướng: **Experience, Expertise, Authoritativeness, Trust**.  
Site spam / copy / không nguồn gốc tác giả dễ yếu hơn site uy tín — đặc biệt chủ đề sức khỏe, tài chính.

Chi tiết triage: [docs/02-google-search-integrity.md](docs/02-google-search-integrity.md)

---

### 5. Lab trong module làm gì?

```
URL / Email mẫu (data/)
        │
        ▼
┌─────────────────────────┐
│ Phishing analyzer       │  heuristics URL + email
├─────────────────────────┤
│ Security headers check  │  thiếu header → điểm rủi ro
├─────────────────────────┤
│ Input sanitizer         │  phát hiện XSS/SQLi mẫu + escape
├─────────────────────────┤
│ SEO integrity + triage  │  fixture GSC → nhánh khôi phục
└─────────────────────────┘
```

Đây là **mô phỏng giáo dục**. Trên site thật bạn còn dùng ZAP, Lighthouse, Search Console — xem lab 04 + [docs/03](docs/03-authorized-self-assessment.md).

---

## Nội dung chính — map file ↔ lý thuyết

| File | Ý lý thuyết |
|------|-------------|
| `examples/01_phishing_url_analyzer.py` | Red flags URL |
| `examples/02_email_header_red_flags.py` | Red flags email |
| `examples/03_security_headers_check.py` | Headers phòng thủ |
| `examples/04_owasp_input_sanitizer.py` | XSS/SQLi defense cơ bản |
| `examples/05_seo_integrity_audit.py` | Site bị inject/spam |
| `examples/06_search_penalty_triage.py` | Nhánh khôi phục ranking |
| `project/run_audit.py` | Ghép cả pipeline |

---

## Lộ trình lab

| Lab | Nội dung | Sau lab bạn làm được |
|-----|----------|----------------------|
| [01](labs/01-phishing-awareness.md) | URL/email | Chỉ ra vì sao RISK |
| [02](labs/02-owasp-hardening.md) | Headers + sanitize | Viết CSP tối thiểu |
| [03](labs/03-search-integrity-recovery.md) | Triage GSC fixture | Checklist cleanup hack |
| [04](labs/04-self-assessment-toolkit.md) | Tool trên site bạn | Headers + Lighthouse |

Docs lý thuyết: [01 phishing](docs/01-phishing-defense.md) · [04 OWASP](docs/04-owasp-hardening-theory.md) · [02 Search](docs/02-google-search-integrity.md) · [03 self-test](docs/03-authorized-self-assessment.md)

---

## Cấu trúc thư mục

```
25-web-security-phishing-seo/
├── data/                 # Fixture lab (URL, email, GSC giả)
├── examples/             # 6 ví dụ — chạy tuần tự
├── project/              # common.py + run_audit.py
├── labs/
├── docs/                 # Lý thuyết mở rộng
├── scripts/
├── cheatsheet/
├── README.md             # File này
└── readme_manual.md      # Copy-paste lệnh
```

---

## FAQ — câu hỏi người mới hay hỏi

**Tôi có phải “tấn công” gì không?**  
Không. Chỉ phân tích mẫu và harden. Self-test chỉ trên domain **bạn sở hữu**.

**Heuristics Python có đủ bảo vệ công ty không?**  
Không. Đó là bài học. Production cần email gateway, WAF, MFA, patch CMS, CI (Module 26).

**Khác Module 16?**  
16 = WAF/NetworkPolicy trên **Kubernetes**. 25 = nhận thức phishing + OWASP cơ bản + **Search Console recovery**.

**Rớt top Google có phải bị “đánh SEO” không?**  
Thường là: bị hack, Manual Action, update chất lượng, hoặc lỗi kỹ thuật — triage bằng GSC trước khi đổ thừa đối thủ.

**Teardown**

```bash
bash scripts/06-teardown.sh
```

---

## Bài tập & ghi chú tự học

- [exercises/bai_tap.md](exercises/bai_tap.md)
- Ghi sổ: 5 red flags phishing + 3 header bắt buộc + 4 nhánh triage ranking

[readme_manual.md](readme_manual.md) | [cheatsheet/web-defense.md](cheatsheet/web-defense.md)
