# Lộ trình tự học CKA → CKS

## Giai đoạn 0 — Chuẩn bị (1 tuần)

**Mục tiêu:** Cài cluster lab, thuần `kubectl` cơ bản.

```bash
# Kiểm tra cluster
kubectl get nodes
kubectl get ns
kubectl run test --image=nginx --dry-run=client -o yaml
```

**Đọc:** Module 15 docs K8s cơ bản hoặc kubernetes.io/tutorials  
**Đọc thêm:** [JSONPath với kubectl](10-jsonpath-kubectl.md) — kỹ năng dùng nhiều khi thi

**Lab:** 01, 02

---

## Giai đoạn 1 — CKA Core (3–4 tuần)

| Tuần | Docs | Labs | Kỹ năng |
|------|------|------|---------|
| 1 | 02 Workloads | 01–02 | Pod, Deployment, scale |
| 2 | 03 Networking | 03–05 | Service, Ingress, NetPol |
| 3 | 04 Storage | 06 | PVC, PV, mount volume |
| 4 | 02 Scheduling | 07–08 | Affinity, taint, RBAC |

**Checkpoint:** Làm lab 09 troubleshoot trong ≤ 45 phút.

---

## Giai đoạn 2 — CKA Advanced (2 tuần)

| Tuần | Docs | Labs |
|------|------|------|
| 5 | 01 Cluster Arch | 10 etcd backup |
| 6 | 04 Troubleshooting | 09, 14 (CKA part) |

**Checkpoint:** Mock 17 task CKA trong 2 giờ, điểm ≥ 70%.

---

## Giai đoạn 3 — CKS (3–4 tuần)

**Yêu cầu:** Đã có CKA hoặc nắm vững CKA domains.

| Tuần | Docs | Labs |
|------|------|------|
| 7 | 05 Cluster Hardening | 11 Pod Security |
| 8 | 06 System Hardening | 12 NetPol Zero Trust |
| 9 | 07–08 Supply Chain/Runtime | 13 Audit/Falco |
| 10 | 09 Mock strategy | 14 full mock |

---

## Thời gian học mỗi ngày (gợi ý)

| Buổi | Thời gian | Hoạt động |
|------|-----------|-----------|
| Sáng | 30 phút | Đọc docs lý thuyết |
| Chiều | 60 phút | Làm 1 lab hands-on |
| Tối | 15 phút | Ôn cheatsheet, ghi chú lỗi |

---

## Checklist trước khi đăng ký thi

### CKA
- [ ] Tạo Pod/Deployment/Service trong namespace bất kỳ ≤ 3 phút
- [ ] Debug Pod `CrashLoopBackOff` không cần Google
- [ ] Tạo PVC + mount vào Pod
- [ ] Cấu hình RBAC Role + RoleBinding
- [ ] Backup/restore etcd (hoặc hiểu quy trình)
- [ ] Dùng thành thạo `kubectl explain`, `--dry-run`

### CKS
- [ ] Áp dụng Pod Security Standards (restricted/baseline)
- [ ] Viết NetworkPolicy deny-all + allow cụ thể
- [ ] Đọc hiểu Audit Policy YAML
- [ ] Scan image với Trivy / policy
- [ ] Biết seccomp, AppArmor cơ bản trên Pod spec
