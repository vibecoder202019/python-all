# CKS — Cluster Setup & Hardening (10% + 15%)

## CIS Benchmark — Hardening kube-apiserver

Các flag thường gặp thi CKS (file `/etc/kubernetes/manifests/kube-apiserver.yaml` — static pod):

```yaml
# Bật audit log
- --audit-policy-file=/etc/kubernetes/audit-policy.yaml
- --audit-log-path=/var/log/kubernetes/audit.log

# Tắt anonymous auth
- --anonymous-auth=false

# RBAC bắt buộc
- --authorization-mode=Node,RBAC

# Không dùng basic auth
- --basic-auth-file=   # phải KHÔNG set hoặc xóa
```

> **Thi CKS:** Sửa manifest static pod → kubelet tự restart pod sau ~30s.

## Pod Security Standards (PSS)

| Level | Mô tả |
|-------|-------|
| **Privileged** | Không hạn chế |
| **Baseline** | Chặn privileged, hostNetwork... |
| **Restricted** | Rất chặt — non-root, drop caps |

```bash
# Gắn label namespace
kubectl label namespace exam-ns \
  pod-security.kubernetes.io/enforce=restricted \
  pod-security.kubernetes.io/warn=restricted \
  pod-security.kubernetes.io/audit=restricted
```

## RBAC — Principle of least privilege

```bash
# Tạo Role + RoleBinding
kubectl create role pod-reader --verb=get,list,watch --resource=pods -n exam-ns
kubectl create rolebinding read-pods --role=pod-reader \
  --serviceaccount=exam-ns:default -n exam-ns

# Kiểm tra quyền
kubectl auth can-i create pods --as=system:serviceaccount:exam-ns:default -n exam-ns
```

## NetworkPolicy default deny

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: exam-ns
spec:
  podSelector: {}
  policyTypes: [Ingress, Egress]
  # Không có ingress/egress rules = deny all
```

## Lab

- [Lab 08 RBAC](../labs/intermediate/lab08-rbac.md), [Lab 11 Pod Security](../labs/advanced/lab11-pod-security.md), [Lab 12 NetPol](../labs/advanced/lab12-netpol-zero-trust.md)

→ [06-cks-system-hardening.md](06-cks-system-hardening.md)
