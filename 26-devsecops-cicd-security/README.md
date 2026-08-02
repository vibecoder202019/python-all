# Module 26: DevSecOps CI/CD — Security in the Pipeline

Xây **pipeline CI/CD có bảo mật xuyên suốt** (shift-left): secrets → SCA → SAST → build → container/SBOM → policy gate → deploy an toàn.

**Dành cho ai?** Người mới đã biết git cơ bản + chạy được terminal. Không cần từng là Security Engineer.  
**Liên quan:** [Module 12](../12-python-devops-devsecops/README.md) · [Module 16](../16-k8s-security/README.md) · [Module 25](../25-web-security-phishing-seo/README.md) · [Module 19 Vault](../19-vault-terraform/README.md)

---

## Mục tiêu

Sau module này bạn sẽ:

1. Giải thích được **CI/CD** và **DevSecOps** bằng lời đơn giản
2. Nói rõ từng lớp scan: secret, SCA, SAST, container, SBOM, DAST
3. Chạy pipeline **local** giống CI và đọc báo cáo (Bandit, pip-audit…)
4. Hiểu **policy gate** (khi nào fail PR)
5. Biết vì sao production dùng **OIDC** thay vì nhét AWS key dài hạn vào GitHub Secrets
6. Copy được workflow mẫu vào repo của bạn

---

## Cách tự học module này

1. Đọc **Lý thuyết nền tảng** hết một lượt
2. Đọc [docs/01](docs/01-devsecops-pipeline.md) + [docs/02](docs/02-tools-matrix.md) + [docs/03-glossary](docs/03-glossary-for-beginners.md)
3. Chạy local pipeline — xem stage nào OK / SKIP / WARN
4. Mở `reports/bandit.json` — đối chiếu MD5 trong `sample-app` với lý thuyết SAST
5. Làm labs 01 → 04; sau đó mới sửa YAML cho repo thật

```bash
cd learn-python-ai
bash 26-devsecops-cicd-security/scripts/setup.sh
bash 26-devsecops-cicd-security/scripts/01-check-prerequisites.sh
bash 26-devsecops-cicd-security/scripts/02-run-local-pipeline.sh
```

Chi tiết lệnh: [readme_manual.md](readme_manual.md)

---

## Lý thuyết nền tảng (đọc kỹ)

### 1. CI/CD là gì? (cho người chưa làm DevOps)

| Thuật ngữ | Nghĩa đơn giản |
|-----------|----------------|
| **CI** (Continuous Integration) | Mỗi lần push/PR, máy chủ **tự** chạy test/build để bắt lỗi sớm |
| **CD** (Continuous Delivery/Deployment) | Sau khi CI xanh, **tự** (hoặc bán tự động) đưa bản build lên staging/production |
| **Pipeline** | Chuỗi bước tuần tự/song song: checkout → test → scan → build → deploy |
| **GitHub Actions** | CI/CD của GitHub; file YAML trong `.github/workflows/` |

**Ví von:** Mỗi lần bạn nộp bài (push), có “cô giám thị tự động” chấm: có mang đáp án cấm (secret) không? thư viện có lỗi không? code có pattern nguy hiểm không? bài test có đậu không? rồi mới cho vào “kho chứa hành” (registry) và giao hàng (deploy).

```
Trước (thủ công):
  Dev code → quên test → copy lên server → user gặp lỗi/bảo mật

Sau (CI/CD):
  Dev push → Pipeline chạy → Đỏ thì chặn merge → Xanh mới deploy
```

---

### 2. DevOps vs DevSecOps

```
DevOps                         DevSecOps
──────                         ─────────
Tự động build/test/deploy  +   Quét bảo mật trong cùng pipeline
Nhanh giao tính năng       +   Không giao kèm lỗ hổng/secret đã biết
IaC, monitor               +   Policy gate, SBOM, sign image
```

**DevSecOps không phải team Security thay Dev làm hết.**  
Mà là: **mọi PR đều đi qua cửa kiểm tra bảo mật tối thiểu**, giống mọi PR đều phải qua unit test.

#### Shift-left nghĩa là gì?

“**Shift-left**” = đưa kiểm tra bảo mật **sang trái** trên timeline (sớm hơn):

```
Cũ:  Code ──────────────────────── Deploy ──► Mới pentest (đắt, muộn)
Mới: Code → scan ngay trên PR → Build đã sạch → Deploy → Vẫn monitor
         ↑
      shift-left
```

Sửa secret lộ trên PR rẻ hơn sửa sau khi key đã lên internet vài tuần.

---

### 3. Các lớp bảo mật trong pipeline (học thuộc sơ đồ)

```
┌─────────────┐
│  git push   │
└──────┬──────┘
       ▼
┌──────────────────────────────────────────────────────────┐
│ 1. Secret scan     Gitleaks — tìm API key/password trong git │
│ 2. SCA             pip-audit — CVE trong thư viện          │
│ 3. SAST            Bandit/Semgrep — pattern code nguy hiểm │
│ 4. IaC (nếu có)    Checkov/Trivy config — K8s/TF sai cấu hình │
│ 5. Unit tests      pytest — logic vẫn đúng                 │
│ 6. Build image     Docker — đóng gói app                   │
│ 7. Container CVE   Trivy — lỗ hổng trong image/OS packages │
│ 8. SBOM            Syft — “hóa đơn” thành phần phần mềm    │
│ 9. Sign (prod)     Cosign — chứng minh image chưa bị sửa   │
│10. Policy gate     Fail PR nếu CRITICAL                    │
│11. Deploy          OIDC — quyền tạm, không key dài hạn     │
│12. DAST (staging)  ZAP — thử tấn công HTTP trên site chạy  │
└──────────────────────────────────────────────────────────┘
```

#### Giải thích từng lớp bằng ví dụ đời thường

| # | Lớp | Câu hỏi nó trả lời | Ví dụ tool |
|---|-----|--------------------|------------|
| 1 | **Secret scan** | Có ai commit nhầm mật khẩu/AWS key không? | Gitleaks |
| 2 | **SCA** (Software Composition Analysis) | Thư viện `requests==x.y` có CVE nặng không? | pip-audit, OSV |
| 3 | **SAST** (Static Application Security Testing) | Code có dùng MD5 cho bảo mật, `eval`, SQL nối chuỗi không? | Bandit, Semgrep |
| 4 | **IaC scan** | Manifest K8s có `privileged: true` bừa không? | Checkov, Trivy |
| 5 | **Tests** | App còn chạy đúng không sau khi sửa? | pytest |
| 6 | **Build** | Đóng gói thành container để chạy everywhere | Docker |
| 7 | **Container scan** | Image (kể cả OS) có CVE CRITICAL không? | Trivy, Grype |
| 8 | **SBOM** | Image gồm package nào? (để recall khi CVE mới) | Syft → CycloneDX |
| 9 | **Sign** | Image trên registry có bị thay thế độc hại không? | Cosign |
|10 | **Policy gate** | Đủ sạch để merge/deploy chưa? | Branch protection |
|11 | **OIDC deploy** | Lấy quyền cloud tạm thời, không lưu secret vĩnh viễn | GitHub OIDC → AWS |
|12 | **DAST** | Site **đang chạy** có XSS/header yếu không? | OWASP ZAP |

**SAST vs DAST (dễ lẫn):**

- **SAST** = đọc **source code** (chưa cần chạy app) — nhanh, sớm  
- **DAST** = tấn công **URL đang chạy** (staging) — bắt lỗi runtime/config  

Cần cả hai theo thời điểm khác nhau.

**SCA vs Container scan:**

- **SCA** nhìn `requirements.txt` / `package-lock`  
- **Trivy image** nhìn cả **OS packages** trong Dockerfile base (`apt`/`apk`)  

---

### 4. Nguyên tắc thiết kế pipeline tốt

| Nguyên tắc | Nghĩa | Trong module |
|------------|-------|--------------|
| **Shift-left** | Scan sớm | Secret + SAST trước build image |
| **Fail closed** | Không chắc thì **chặn** | CRITICAL → fail job |
| **Least privilege** | Ít quyền nhất đủ việc | OIDC, không AWS key dài hạn |
| **Defense in depth** | Nhiều lớp | Secret + SAST + Trivy… |
| **Supply chain security** | Tin được thứ mình build/kéo | SBOM, pin action SHA, scan base image |
| **Fast feedback** | Dev không chờ 1 giờ | Job song song, cache pip/Docker |

#### Fail-closed vs “cảnh báo rồi cho qua”

| Giai đoạn team | Secrets | CRITICAL CVE | HIGH | Bandit HIGH |
|----------------|---------|--------------|------|-------------|
| Lab / tuần đầu | fail | fail hoặc warn có chủ đích | warn | warn (học) |
| Production chín | fail | fail | fail dần | fail |

Lab `sample-app` **cố ý** dùng MD5 để bạn thấy Bandit báo HIGH — production phải sửa hoặc có ticket + `# nosec` có hạn.

File quy tắc: [`policy/severity-gate.yaml`](policy/severity-gate.yaml)

---

### 5. GitHub Actions — đọc YAML như người mới

Workflow = file YAML khai báo:

- **Khi nào chạy:** `on: push` / `pull_request`
- **Chạy trên máy nào:** `runs-on: ubuntu-latest`
- **Các việc:** `jobs` → `steps` (checkout code, cài Python, chạy bandit…)

Trong repo học:

- Bản mẫu: [`pipelines/github-actions/devsecops.yml`](pipelines/github-actions/devsecops.yml)
- Bản đã copy sẵn để CI repo: [`.github/workflows/devsecops.yml`](../.github/workflows/devsecops.yml)

**Branch protection:** Settings → Branches → require các status check DevSecOps xanh mới merge `main`.  
Đó chính là **policy gate** ở tầng GitHub.

---

### 6. OIDC deploy — vì sao không lưu AWS key trong Secrets?

**Cách cũ (rủi ro):**

```
GitHub Secret: AWS_ACCESS_KEY_ID + AWS_SECRET_ACCESS_KEY
→ Key sống lâu, leak = kẻ có quyền cloud của bạn
```

**Cách tốt hơn (OIDC):**

```
GitHub Actions ──JWT ngắn hạn──► AWS IAM Role
→ Chỉ job đúng repo/branch mới assume role được
→ Hết job là hết quyền
```

Trong workflow mẫu, job `deploy` đang **comment** — lab tập trung scan; khi làm cloud thật hãy bật và cấu hình IAM trust (lab 04).

---

### 7. SBOM là gì? (hiểu trong 1 phút)

**SBOM** (Software Bill of Materials) = danh sách nguyên liệu: thư viện nào, phiên bản nào nằm trong image/artifact.

Khi CVE mới công bố, bạn hỏi: “Ta có package đó không?” → mở SBOM thay vì đoán.

Lab tạo SBOM bằng Syft (nếu cài được) hoặc trên GitHub Actions job build.

---

## Chạy nhanh (local)

```bash
cd learn-python-ai
bash 26-devsecops-cicd-security/scripts/setup.sh
bash 26-devsecops-cicd-security/scripts/02-run-local-pipeline.sh
```

Thiếu `gitleaks`/`trivy`/`docker` → stage **SKIP** (vẫn học được flow).  
Bật Docker Desktop để đủ build + Trivy + SBOM.

Copy workflow vào repo app:

```bash
mkdir -p .github/workflows
cp 26-devsecops-cicd-security/pipelines/github-actions/devsecops.yml \
   .github/workflows/devsecops.yml
# Đổi APP_DIR="." nếu là repo app riêng
```

---

## Sample app — vì sao có “lỗ hổng” cố ý?

`sample-app/app.py` dùng **MD5** ở endpoint `/hash` để Bandit báo **B324**.  
Mục đích: bạn thấy SAST hoạt động. **Không** copy pattern này sang production.

```bash
# Sau khi hiểu finding, bài tập: đổi sang sha256 và chạy lại Bandit
bandit -r 26-devsecops-cicd-security/sample-app -ll
```

---

## Lộ trình lab

| Lab | Nội dung | Kết quả kỳ vọng |
|-----|----------|-----------------|
| [01](labs/01-pipeline-stages.md) | Map stage → tool | Bảng tự điền đủ 8+ lớp |
| [02](labs/02-run-local-gates.md) | Chạy local + đọc report | Giải thích finding MD5 |
| [03](labs/03-github-actions.md) | Bật Actions | PR bị chặn nếu check đỏ (khi bật protection) |
| [04](labs/04-policy-and-oidc.md) | Policy + OIDC | Viết được lý do không dùng static key |

Docs: [01 pipeline](docs/01-devsecops-pipeline.md) · [02 tools](docs/02-tools-matrix.md) · [03 glossary](docs/03-glossary-for-beginners.md)

---

## Cấu trúc thư mục

```
26-devsecops-cicd-security/
├── sample-app/              # FastAPI lab (+ MD5 cố ý)
├── pipelines/
│   ├── github-actions/      # Workflow mẫu
│   └── pre-commit-config.yaml
├── policy/                  # severity-gate.yaml
├── scripts/                 # Local pipeline
├── reports/                 # Output (gitignore)
├── labs/ docs/ cheatsheet/
├── README.md
└── readme_manual.md
```

---

## FAQ — người mới hay hỏi

**Khác Module 12?**  
12 = học **viết script** Python DevOps. 26 = **lắp ráp pipeline CI/CD** đầy đủ (YAML + gate + image scan).

**Phải cài hết Gitleaks/Trivy/Syft ngay?**  
Không. Script skip tool thiếu. Cài dần khi muốn stage đó chạy thật: `brew install gitleaks trivy syft`.

**Pipeline lab fail vì Bandit MD5 có sao không?**  
Lab **cố ý** để bạn thấy finding. Local script warn; trên CI mẫu cũng warn trước. Production: sửa code hoặc fail-closed.

**Semgrep cần token?**  
Bản cloud có thể cần; lab để `continue-on-error`. Bandit vẫn chạy offline.

**Production còn thiếu gì?**  
Pin action SHA, branch protection, Cosign, OIDC, Vault (Module 19), ZAP staging (Module 25 doc), monitoring runtime.

---

## Bài tập

[exercises/bai_tap.md](exercises/bai_tap.md)

[readme_manual.md](readme_manual.md) | [cheatsheet/devsecops-pipeline.md](cheatsheet/devsecops-pipeline.md)
