# CKS — System Hardening (15%)

## Seccomp, AppArmor (Pod securityContext)

```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  seccompProfile:
    type: RuntimeDefault    # dùng profile mặc định container runtime
  capabilities:
    drop: ["ALL"]
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
```

## Restricted Pod example (PSS restricted)

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: app
      image: nginx:1.25
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: ["ALL"]
        runAsUser: 101   # nginx user
      volumeMounts:
        - name: tmp
          mountPath: /tmp
        - name: cache
          mountPath: /var/cache/nginx
  volumes:
    - name: tmp
      emptyDir: {}
    - name: cache
      emptyDir: {}
```

## kubelet hardening

File `/var/lib/kubelet/config.yaml`:

```yaml
authentication:
  anonymous:
    enabled: false
authorization:
  mode: Webhook
readOnlyPort: 0          # tắt kubelet read-only port 10255
```

## SSH / OS hardening (biết khái niệm)

- Tắt root login SSH
- Chỉ cho phép key-based auth
- Cập nhật patch OS thường xuyên

→ [07-cks-microservice-supply-chain.md](07-cks-microservice-supply-chain.md)
