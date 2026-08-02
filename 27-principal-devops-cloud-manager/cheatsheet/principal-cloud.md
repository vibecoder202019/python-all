# Principal DevOps / Cloud Manager — cheatsheet

## Bốn trụ

Platform · Reliability (SLO) · Security/Gov · FinOps

## Artifact bắt buộc

ADR · Golden path catalog · SLO · Runbook · Postmortem · Scorecard · 1-pager

## Lệnh

```bash
bash scripts/setup.sh
bash scripts/02-init-portfolio.sh
bash scripts/03-run-governance-scorecard.sh
bash scripts/04-run-finops-summary.sh
bash scripts/05-validate-portfolio.sh
```

## Error budget (nhớ)

99.9% / 30 ngày ≈ **43 phút** downtime

## Cloud Manager weekly

- Cost anomaly  
- IAM / break-glass review  
- SEV trend  
- Platform adoption %  

## Map module

12/26 CI · 13/22 AWS Org · 15–18 K8s · 19 Vault/TF · 27 portfolio
