# Lab 09 — Troubleshooting (Advanced | CKA 30%)

**Thời gian:** 60 phút — **Không xem đáp án trước khi thử 30 phút**

## Tình huống

Namespace `cka-trouble` có 4 pod broken — sửa tất cả cho Running.

```bash
kubectl apply -f manifests/cka/troubleshoot-broken.yaml
kubectl get pods -n cka-trouble
```

| Pod | Triệu chứng gợi ý |
|-----|-------------------|
| `broken-image` | ImagePullBackOff |
| `broken-config` | CreateContainerConfigError |
| `broken-crash` | CrashLoopBackOff |
| `broken-mount` | Pending / mount error |

## Quy trình (ghi chú từng bước)

```
1. kubectl describe pod <name> -n cka-trouble
2. kubectl logs <name> -n cka-trouble [--previous]
3. Sửa deployment/yaml hoặc tạo resource thiếu
4. Verify: kubectl get pods -n cka-trouble
```

<details>
<summary>Đáp án (chỉ mở sau khi thử)</summary>

1. **broken-image** — sửa image tag sai → `nginx:1.25`
2. **broken-config** — tạo ConfigMap `missing-cm` hoặc sửa env ref
3. **broken-crash** — sửa command (exit 1 → sleep infinity hoặc nginx)
4. **broken-mount** — tạo PVC hoặc sửa claimName

File fixed: `manifests/cka/troubleshoot-fixed.yaml`
</details>

## Verify

```bash
bash scripts/03-verify-lab.sh 09
```
