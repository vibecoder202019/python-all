# Example ADR-001 (tham khảo — tự viết trước khi đọc)

**Status:** Accepted  
**Date:** 2026-08-01  
**Tags:** platform / reliability  

## Context

Acme cần chạy 30 service JVM/Python. Team 12 eng. Muốn giảm snowflake cluster.

## Options

### A — EKS
Pros: portable, ecosystem. Cons: control plane cost + skills.

### B — ECS Fargate
Pros: ít node mgmt. Cons: lock-in hơn, networking patterns khác.

### C — VM + Ansible only
Pros: đơn giản ngắn hạn. Cons: không scale self-service.

## Decision

**ECS Fargate** năm 1 cho 80% service; EKS pilot 2 service mesh-heavy. Review sau 2 quý.

## Consequences

+ Onboarding nhanh hơn qua golden path Task Def  
− Cần ADR riêng cho data-plane egress/NAT cost  
Follow-up: FinOps review NAT (lab cost fixture)
