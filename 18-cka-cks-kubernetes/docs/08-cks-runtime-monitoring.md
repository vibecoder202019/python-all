# CKS — Monitoring, Logging, Runtime Security (20%)

## Audit Policy

File `/etc/kubernetes/audit-policy.yaml`:

```yaml
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
  # Log mọi thay đổi resource ở mức RequestResponse
  - level: RequestResponse
    verbs: ["create", "update", "patch", "delete"]
    resources:
      - group: ""
        resources: ["pods", "secrets", "configmaps"]
  # Metadata cho request đọc
  - level: Metadata
    verbs: ["get", "list", "watch"]
  - level: Metadata
    omitStages: ["RequestReceived"]
```

Gắn vào kube-apiserver manifest:
```yaml
- --audit-policy-file=/etc/kubernetes/audit-policy.yaml
- --audit-log-path=/var/log/kubernetes/audit.log
```

## Falco — Runtime detection

```bash
# Cài Falco (helm)
helm repo add falcosecurity https://falcosecurity.github.io/charts
helm install falco falcosecurity/falco -n falco --create-namespace

# Xem alert
kubectl logs -l app.kubernetes.io/name=falco -n falco
```

Rule mẫu phát hiện shell trong container:
```yaml
- rule: Terminal shell in container
  condition: spawned_process and container and shell_procs
  output: "Shell in container (user=%user.name %container.info)"
  priority: WARNING
```

## Log aggregation (biết khái niệm)

- **Node level:** `/var/log/pods/`, `journalctl -u kubelet`
- **Cluster:** EFK (Elasticsearch, Fluentd, Kibana) hoặc Loki

```bash
# Log pod
kubectl logs <pod> -n exam-ns -f

# Log tất cả container trong pod multi-container
kubectl logs <pod> -c <container> -n exam-ns
```

## Lab

- [Lab 13 Audit & Falco](../labs/advanced/lab13-audit-falco.md)

→ [09-mock-exam-chien-luoc.md](09-mock-exam-chien-luoc.md)
