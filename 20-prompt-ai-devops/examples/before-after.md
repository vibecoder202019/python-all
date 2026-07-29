# Before / After — Prompt examples

## 1. Python debug

### ❌ Before
```
my script error fix it
```

### ✅ After
See [prompts/python/debug-error.md](../prompts/python/debug-error.md)

---

## 2. Kubernetes

### ❌ Before
```
deployment not working
```

### ✅ After
```
Namespace prod. Deployment web replicas 0/3.
Events: FailedScheduling — 0/3 nodes insufficient cpu.
Describe node: allocatable cpu 100m, requests total 9800m.
Task: suggest 2 fixes — scale cluster vs reduce requests.
Output: table Option | Change | Trade-off |
```

---

## 3. Vault

### ❌ Before
```
write vault policy for my app
```

### ✅ After
```
App reads only secret/data/payment/api-key (KV v2).
Deny write, delete, list other paths.
Auth: K8s SA payment-sa in ns payment.
Output: HCL + vault policy write command
```

---

## 4. Monitoring

### ❌ Before
```
prometheus query for errors
```

### ✅ After
```
Metric http_requests_total{job="api",status=~"5.."}.
Task: 5m error rate / total RPS, ratio 0-1.
Output: PromQL + Grafana stat panel threshold 0.01
```
