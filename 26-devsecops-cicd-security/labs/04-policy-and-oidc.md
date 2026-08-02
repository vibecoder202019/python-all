# Lab 04 — Policy gate & OIDC

## Policy

Đọc `policy/severity-gate.yaml`. Đề xuất thay đổi cho team “đã sạch CRITICAL 1 tháng”:

- Bật `fail` cho container **HIGH**? Có/Không + lý do.

## OIDC (khái niệm)

Static key trong GitHub Secrets:

```
AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY  → rủi ro leak, khó rotate
```

OIDC:

```
GitHub Actions  --JWT-->  AWS IAM Role  → temporary credentials
```

Trong `devsecops.yml`, job `deploy` đang comment. Việc làm:

1. Viết 5 dòng: role trust policy cần `sub`/`aud` gì (theo GitHub docs).  
2. Nêu vì sao `permissions: id-token: write` bắt buộc.  
3. Nêu 1 lý do dùng GitHub **Environment** `production` + required reviewer.

## DAST

Uncomment khối ZAP khi có URL staging **của bạn**. Liên hệ Module 25 doc self-assessment.
