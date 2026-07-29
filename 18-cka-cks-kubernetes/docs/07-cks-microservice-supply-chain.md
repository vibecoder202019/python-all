# CKS — Microservice Vulnerabilities & Supply Chain (20% + 20%)

## Image security

```bash
# Scan image với Trivy (hay gặp CKS)
trivy image nginx:1.25

# Chỉ dùng image từ registry tin cậy
# imagePullPolicy: Always — luôn pull bản mới khi deploy
```

## Immutable container

```yaml
# Không chạy shell, không install package lúc runtime
# Multi-stage Dockerfile — image production tối thiểu
# readOnlyRootFilesystem: true + emptyDir cho /tmp
```

## Admission Control

| Controller | Vai trò |
|------------|---------|
| **PodSecurity** | Enforce PSS |
| **NodeRestriction** | Giới hạn kubelet chỉ sửa pod trên node mình |
| **ImagePolicyWebhook** | Chặn image không whitelisted |

## OPA / Gatekeeper (biết khái niệm)

```yaml
# ConstraintTemplate — policy: bắt buộc label, chặn :latest tag
# Thi CKS có thể yêu cầu đọc/sửa Constraint CRD
```

## Secret management

```bash
# KHÔNG hardcode secret trong Deployment
kubectl create secret generic db-cred \
  --from-literal=password=secret123 -n exam-ns

# Mount secret as env hoặc volume
# Encryption at rest — /etc/kubernetes/encryption-config.yaml
```

## ServiceAccount token

```bash
# Kubernetes 1.24+ không auto-create token Secret
kubectl create token my-sa -n exam-ns --duration=1h
```

→ [08-cks-runtime-monitoring.md](08-cks-runtime-monitoring.md)
