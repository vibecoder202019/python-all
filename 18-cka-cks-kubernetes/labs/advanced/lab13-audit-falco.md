# Lab 13 — Audit Policy & Falco (Advanced | CKS)

**Thời gian:** 60 phút

## Phần A — Audit Policy (lý thuyết + YAML)

Đọc `manifests/cks/audit-policy.yaml` — giải thích từng rule.

Câu hỏi:
1. Level `RequestResponse` khác `Metadata`?
2. Tại sa log delete Secret?

## Phần B — Falco (lab local tuỳ chọn)

```bash
helm repo add falcosecurity https://falcosecurity.github.io/charts
helm install falco falcosecurity/falco -n falco --create-namespace
```

Trigger alert:
```bash
kubectl exec -it <any-pod> -n cks-lab -- sh
# Falco alert: shell in container
```

## Phần C — Đọc audit log (simulation)

File mẫu log: `manifests/cks/sample-audit-log.json`

Tìm: ai delete pod? user nào?

## Verify

Checklist bài 13 trong exercises.
