# Hướng dẫn chạy Manual — Module 25: Web Security / Phishing / Search Integrity

> Lệnh từ `setup.sh`, `01-check-prerequisites.sh`, `02-run-all-examples.sh`, `03-run-project.sh`, `06-teardown.sh`.  
> **Phòng thủ only** — không tấn công site / SEO bên thứ ba.

## Phần A — Cài đặt (`scripts/setup.sh`)

```bash
cd learn-python-ai
python3 -m venv .venv
source .venv/bin/activate
python -c "import json, urllib.parse, html; print('stdlib OK')"
mkdir -p 25-web-security-phishing-seo/data
```

**Kiểm tra:**

```bash
test -f 25-web-security-phishing-seo/project/common.py && echo OK
```

---

## Phần B — Prerequisites (`scripts/01-check-prerequisites.sh`)

```bash
python3 --version
test -f learn-python-ai/25-web-security-phishing-seo/data/sample_urls.txt
test -f learn-python-ai/25-web-security-phishing-seo/data/gsc_fixture_compromised.json
```

---

## Phần C — Chạy từng ví dụ

```bash
cd learn-python-ai
source .venv/bin/activate
python3 25-web-security-phishing-seo/examples/01_phishing_url_analyzer.py
python3 25-web-security-phishing-seo/examples/02_email_header_red_flags.py
python3 25-web-security-phishing-seo/examples/03_security_headers_check.py
python3 25-web-security-phishing-seo/examples/04_owasp_input_sanitizer.py
python3 25-web-security-phishing-seo/examples/05_seo_integrity_audit.py
python3 25-web-security-phishing-seo/examples/06_search_penalty_triage.py
```

Hoặc:

```bash
bash 25-web-security-phishing-seo/scripts/02-run-all-examples.sh
```

**Kỳ vọng:** URL/email phishing có `RISK`; fixture compromised → `security_compromise`.

---

## Phần D — Project pipeline (`scripts/03-run-project.sh`)

```bash
bash 25-web-security-phishing-seo/scripts/03-run-project.sh
cat 25-web-security-phishing-seo/data/last_audit_report.json
```

---

## Phần E — Labs

```bash
# Đọc và làm theo
open 25-web-security-phishing-seo/labs/01-phishing-awareness.md
open 25-web-security-phishing-seo/labs/02-owasp-hardening.md
open 25-web-security-phishing-seo/labs/03-search-integrity-recovery.md
```

---

## Phần F — Teardown (`scripts/06-teardown.sh`)

```bash
bash 25-web-security-phishing-seo/scripts/06-teardown.sh
```

---

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `setup.sh` | A |
| `01-check-prerequisites.sh` | B |
| `02-run-all-examples.sh` | C |
| `03-run-project.sh` | D |
| `06-teardown.sh` | F |
