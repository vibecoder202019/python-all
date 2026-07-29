# Lab 11 — Pod Security Standards (Advanced | CKS)

**Namespace:** `cks-lab` | **Thời gian:** 45 phút

## Bài tập 1 — Enforce PSS trên namespace

```bash
kubectl create namespace cks-lab
kubectl label namespace cks-lab \
  pod-security.kubernetes.io/enforce=baseline \
  pod-security.kubernetes.io/warn=restricted \
  pod-security.kubernetes.io/audit=restricted
```

## Bài tập 2 — Pod bị từ chối (privileged)

```bash
kubectl apply -f manifests/cks/pod-privileged.yaml -n cks-lab
# Phải bị Forbidden
```

## Bài tập 3 — Pod compliant (restricted)

Apply `manifests/cks/pod-restricted.yaml` — phải Running.

## Bài tập 4 — SecurityContext

Thêm vào deployment:
- `runAsNonRoot: true`
- `capabilities.drop: [ALL]`
- `readOnlyRootFilesystem: true`

## Verify

```bash
bash scripts/03-verify-lab.sh 11
```
