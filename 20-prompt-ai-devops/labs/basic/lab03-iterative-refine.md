# Lab 03 — Iterative refine (Basic)

**45 phút**

1. Prompt AI: *"Viết Deployment nginx 3 replicas namespace cka-lab"*
2. Output thiếu probes/resources → prompt refine:
   ```
   Giữ image và replicas. Thêm liveness probe + requests 64Mi/50m.
   Output: full YAML only.
   ```
3. Lặp đến khi `kubectl apply --dry-run=client` pass (nếu có cluster)

Ghi lại **3 vòng** prompt → what improved.
