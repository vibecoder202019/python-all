# Lab 07 — S3 Cross-Account (Console)

1. Management/Audit: bucket `org-audit-logs-ACCOUNT_ID-lab`
2. Bucket policy từ `policies/s3-cross-account-bucket.json`
3. Assume DevOps role → `aws s3 cp` vào prefix `dev/`

## Pass

Object visible từ audit account console.

Doc: [docs/05-console-resource-access.md](../../docs/05-console-resource-access.md)
