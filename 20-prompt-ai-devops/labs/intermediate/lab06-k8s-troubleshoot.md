# Lab 06 — Troubleshoot K8s Pod (Intermediate)

**60 phút**

## Chuẩn bị

Deploy broken manifest Module 18:
```bash
kubectl apply -f 18-cka-cks-kubernetes/manifests/cka/troubleshoot-broken.yaml
```

Hoặc mô tả pod lỗi giả lập nếu không có cluster.

## Bài tập

1. Thu thập describe + logs + events
2. Dùng [prompts/kubernetes/troubleshoot-pod.md](../../prompts/kubernetes/troubleshoot-pod.md) + few-shot từ [examples/k8s-few-shot.md](../../examples/k8s-few-shot.md)
3. Verify từng đề xuất AI bằng kubectl tay
4. Chỉ apply fix **sau** khi hiểu

## Pass

Sửa ≥ 1 broken pod với AI hỗ trợ — bạn document 3 lệnh verify.
