# Framework R-C-T-O (quick)

**R**ole — senior DevOps / Python / SRE  
**C**ontext — version, NS, log, file, metric (redact secrets)  
**T**ask — ONE job per prompt  
**O**utput — format: YAML only / diff / table / commands

# Always include
- Exact resource names (pod, NS, file path)
- Error message / traceback full
- Constraints (no :latest, no hardcode secret)
- Verify steps

# Refine loop
"Output thiếu X. Giữ Y. Chỉ sửa X."

# Before run
kubectl apply --dry-run=client
terraform plan
pytest
grep -i password (no secrets in diff)

# Cursor
@file @folder — attach context
Agent: Goal + Constraints + Done when

# Never
- Paste production tokens
- Apply AI YAML blind
- "fix my code" one-liner
