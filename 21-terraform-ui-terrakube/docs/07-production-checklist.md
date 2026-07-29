# Production checklist — Terrakube

## Security

- [ ] Đổi password admin mặc định
- [ ] HTTPS TLS certificate thật (Let's Encrypt / corp CA)
- [ ] SSO (Dex → OIDC Azure AD / Google / Keycloak)
- [ ] RBAC least privilege — không mọi user Apply prod
- [ ] Secrets trong Vault (Module 19) — không plain trong UI variables
- [ ] Backup PostgreSQL định kỳ

## State & DR

- [ ] Backup state backend (DB snapshot)
- [ ] Document restore procedure
- [ ] Separate org: `prod` vs `nonprod`

## Executor

- [ ] Executor agent isolated network
- [ ] Dynamic credentials (AWS IRSA / OIDC) thay static keys

## Observability

- [ ] Log aggregation cho API + executor
- [ ] Metrics Prometheus (Terrakube hỗ trợ telemetry compose — tham khảo upstream)
- [ ] Alert run failure → Slack/PagerDuty

## Git workflow

- [ ] Prod apply: manual approval mandatory
- [ ] Plan on PR, apply from protected branch only
- [ ] Drift detection schedule (plan định kỳ)

## So sánh với AWX production

| AWX | Terrakube |
|-----|-----------|
| Backup AWX postgres | Backup Terrakube postgres |
| Credential in Vault | Variable sets + Vault integration |
| Job isolation | Executor isolation |

---

## Khi không dùng Terrakube full platform

Team nhỏ có thể dùng **Atlantis** (PR-only) + S3 state — nhẹ hơn. Module 21 vẫn hữu ích vì học mô hình TACOS; ghi chú tham khảo trong [cheatsheet/alternatives.md](../cheatsheet/alternatives.md).
