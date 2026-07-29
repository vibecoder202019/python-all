# Few-shot — Kubernetes troubleshoot

## Example 1

**Input:** ImagePullBackOff, image `ngnix:1.25` (typo ngnix)

**Output:**
- **Cause:** Sai tên image hoặc tag không tồn tại trên registry
- **Verify:** `kubectl describe pod POD -n NS | grep -i pull`
- **Fix:** Sửa image thành `nginx:1.25`, rollout restart

---

## Example 2

**Input:** CrashLoopBackOff, logs `exec /docker-entrypoint.sh: permission denied`

**Output:**
- **Cause:** Entrypoint không executable hoặc wrong command
- **Verify:** `kubectl exec POD -n NS -- ls -la /docker-entrypoint.sh`
- **Fix:** Dockerfile `chmod +x` hoặc sửa command trong manifest

---

## Your turn

Paste pod scenario Module 18 lab 09 — yêu cầu AI follow format trên (few-shot these 2 examples in prompt).
