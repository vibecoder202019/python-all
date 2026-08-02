# Cloud operating model — cho Principal / Cloud Manager

## 1. Tách account theo blast radius

```
Management
├── Security (log archive, GuardDuty admin, break-glass)
├── Shared (CI runners, Harbor/ECR, DNS)
└── Workloads
     ├── Sandbox
     ├── NonProd (dev/stage)
     └── Prod
```

**Vì sao:** credential leak ở sandbox không = toàn bộ prod; bill tách được; SCP khác nhau từng OU.

Liên hệ Module 22.

## 2. Ai own cái gì? (RACI rút gọn)

| Khả năng | Platform | Product team | Security | Cloud Manager |
|----------|----------|--------------|----------|---------------|
| Landing zone / Org | A/R | C | C | A |
| App deploy | C | R | C | I |
| Secret policy | A | R (dùng đúng) | A | I |
| Prod IAM human | A | C | A | A |
| Budget account | C | R (tag) | I | A |

R = Responsible, A = Accountable, C = Consulted, I = Informed

## 3. Control tower tối thiểu

1. SSO / Identity Center — không IAM user dài hạn  
2. CloudTrail / audit → log archive  
3. SCP: deny leave org, deny disable Trail, restrict regions  
4. Backup policy prod  
5. CI OIDC — không static cloud key (Module 26)  

## 4. Multi-cloud?

Chỉ khi business bắt buộc (latency, data residency, acquisition).  
Principal ưu tiên: **abstraction đúng chỗ** (Terraform modules, OCI images) — không nhân đôi mọi dịch vụ managed.

## 5. Metric operating model

- % workload trên account chuẩn  
- Mean time to provision env  
- % PR fail vì thiếu security gate (rồi giảm dần bằng education, không tắt gate)  
- Cost / team / env  
