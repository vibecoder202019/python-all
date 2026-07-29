# Prompt AI cho Kubernetes

## Troubleshoot Pod — checklist context

Luôn đính kèm (hoặc @file):

```bash
kubectl get pod POD -n NS -o wide
kubectl describe pod POD -n NS
kubectl logs POD -n NS --previous   # nếu restart
kubectl get events -n NS --sort-by='.lastTimestamp' | tail -20
```

Template: [prompts/kubernetes/troubleshoot-pod.md](../prompts/kubernetes/troubleshoot-pod.md)

---

## Prompt troubleshoot mẫu

```markdown
## Role
CKA-level K8s troubleshooter.

## Context
Namespace: cka-lab
Pod: api-pod — Status CrashLoopBackOff, Restarts: 5
Describe excerpt:
  Warning FailedMount: configmap "app-config" not found
  Container exit code 1

Logs:
  Error: CONFIG_PATH not set

## Task
Root cause + fix tối thiểu.
Output: YAML patch hoặc lệnh kubectl tạo ConfigMap thiếu.
Mọi lệnh có `-n cka-lab`.
```

---

## Viết manifest YAML

```markdown
## Task
Deployment `web`:
- image nginx:1.25 (không latest)
- replicas 3
- labels app=web
- resource requests 64Mi/50m, limits 128Mi/100m
- liveness GET / on port 80, initialDelaySeconds 10
- namespace cka-lab

## Output
Single YAML multi-doc: Deployment + Service ClusterIP port 80.
Valid apiVersion. Không field alpha không cần thiết.
```

Template: [prompts/kubernetes/write-deployment.md](../prompts/kubernetes/write-deployment.md)

---

## NetworkPolicy

```markdown
Context: namespace cks-lab, labels frontend/app, backend/app, db/app.
Task: default deny all ingress+egress.
Allow: frontend → backend TCP 8080 only.
Allow: backend → db TCP 5432 only.
Allow: DNS egress UDP 53 to kube-system.

Output: 1 NetworkPolicy hoặc tách rõ nếu cần — giải thích selector.
```

---

## CKA-style exam prompt

```markdown
Exam task style:
"Tạo Role cho SA `deployer` trong NS `exam` — verbs get,list,watch trên pods và deployments."

Output:
1. Lệnh kubectl imperativ nhanh nhất (dry-run yaml)
2. Hoặc YAML apply
3. Lệnh verify: kubectl auth can-i ...
```

Module 18 lab broken YAML — dùng prompt **từng pod một**, đính kèm manifest lỗi.

---

## JSONPath (Module 18)

```markdown
Task: Lệnh kubectl jsonpath in tất cả pod NS production: NAME, PHASE, NODE — mỗi dòng.

Context: không dùng custom-columns, phải dùng jsonpath {range}.
```

---

## Verify AI output

Sau mọi YAML từ AI:

```bash
kubectl apply --dry-run=client -f manifest.yaml
kubeconform -summary manifest.yaml   # nếu có
kubectl diff -f manifest.yaml        # cluster có sẵn
```

**Không** apply production trực tiếp từ AI.

---

## Lab

- [Lab 06 — Troubleshoot Pod](../labs/intermediate/lab06-k8s-troubleshoot.md)
- [Lab 07 — Manifest](../labs/intermediate/lab07-k8s-manifests.md)

**Tiếp:** [05-prompt-vault-terraform.md](05-prompt-vault-terraform.md)
