# DevSecOps pipeline — lý thuyết mở rộng (tự học)

File này bổ sung README Module 26: đi sâu hơn từng khái niệm để bạn giảng lại được.

## 1. Vòng đời một thay đổi code có bảo mật

```
Viết code
   → pre-commit (gitleaks/bandit trên laptop)
   → git push / mở Pull Request
   → CI: secrets, SCA, SAST, tests (song song)
   → CI: build image, Trivy, SBOM
   → Policy: đủ sạch? 
        Không → comment báo cáo, chặn merge
        Có → merge
   → Deploy staging (OIDC)
   → DAST nhẹ (ZAP)
   → Promote production
   → Monitor / response sự cố
```

Mỗi mũi tên là chỗ **tự động hóa** có thể bắt lỗi mà không cần chờ pentest cuối năm.

## 2. Secret scan — vì sao phải full history?

Người mới hay nghĩ: “Tôi đã xóa key khỏi file rồi”.  
Nhưng **git vẫn nhớ** commit cũ. Bot internet quét GitHub public liên tục.

Gitleaks trên CI nên `fetch-depth: 0` để thấy lịch sử.  
Nếu đã lộ: **rotate key ngay** (xóa key cũ trên cloud), không chỉ xóa file.

## 3. SCA — CVE là gì?

**CVE** = mã định danh lỗ hổng công bố công khai (ví dụ CVE-2024-…).  
`pip-audit` hỏi: “Phiên bản thư viện bạn đang pin có nằm trong danh sách bị ảnh hưởng không?”

**False sense of security:** hết CVE hôm nay không nghĩa mãi mãi — vì thế cần CI chạy **mỗi PR** và Dependabot/renovate.

## 4. SAST — “đọc code tìm pattern xấu”

Bandit (Python) ví dụ bắt:

- `hashlib.md5` dùng cho mục đích bảo mật (B324)  
- `subprocess` với `shell=True` + input user  
- Bind `0.0.0.0` kèm debug…

Semgrep dùng rule pack (OWASP) đa ngôn ngữ.

**Giới hạn SAST:** không chạy app → có thể miss lỗi logic nghiệp vụ, race, config chỉ lộ khi runtime → cần DAST/test.

## 5. Container scan — base image quan trọng

Dockerfile:

```dockerfile
FROM python:3.11-slim
```

CVE có thể nằm ở:

- Package OS trong image nền  
- Package Python bạn `pip install`  
- Binary bạn COPY vào

Trivy scan **image đã build**, không chỉ `requirements.txt`.

Mẹo: dùng distroless/slim, update base định kỳ, `USER` không root (lab sample dùng `nobody`).

## 6. SBOM vs vulnerability report

| | SBOM | Vulnerability scan |
|---|------|-------------------|
| Trả lời | “Có gì bên trong?” | “Cái bên trong có lỗ hổng biết trước không?” |
| Format | CycloneDX, SPDX | JSON/table/SARIF |
| Dùng khi | Audit, recall, compliance | Gate CI, patch |

Cần cả hai: không có SBOM thì khó trả lời nhanh CVE mới tuần sau.

## 7. Policy as code (ý tưởng)

`policy/severity-gate.yaml` là phiên bản “đọc được bởi người”.  
Production có thể dùng OPA/Conftest: “nếu Trivy CRITICAL > 0 thì deny”.

Branch protection của GitHub = policy ở tầng merge.

## 8. Supply chain tấn công (khái niệm)

Kẻ xấu có thể:

- Đẩy version độc vào thư viện phụ thuộc  
- Đổi tag GitHub Action `v1` trỏ sang commit độc  
- Thay image trên registry  

Giảm rủi ro: pin version/digest, verify signature (Cosign), SBOM, least privilege OIDC.

## 9. Lộ trình chín dần cho team nhỏ

| Tuần | Việc |
|------|------|
| 1 | Gitleaks + pytest bắt buộc |
| 2 | Bandit + pip-audit (warn) |
| 3 | Docker + Trivy CRITICAL fail |
| 4 | SBOM artifact + branch protection |
| 5+ | OIDC deploy, ZAP staging, fail HIGH |

Đừng bật “fail mọi thứ” ngày đầu khiến team tắt CI — escalate dần có số liệu.
