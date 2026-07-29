# Lab 02 — OU & Account Member (Console)

## Checklist

- [ ] OU `Workloads`, `Security`, `Sandbox`
- [ ] Account `dev-workload` — email unique, status ACTIVE
- [ ] Kéo dev account vào OU Workloads
- [ ] Ghi Dev Account ID + `OrganizationAccountAccessRole` ARN

## Verify

```bash
aws organizations list-organizational-units-for-parent --parent-id r-xxxx
aws organizations list-accounts
```
