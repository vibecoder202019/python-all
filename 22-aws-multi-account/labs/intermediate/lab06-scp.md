# Lab 06 — SCP Deny Region (Console)

1. Enable SCP trong Organizations
2. Create policy `DenyOutsideSingapore` — JSON từ `policies/scp-deny-regions.json`
3. Attach vào OU **Sandbox** (không Root lần đầu)
4. Test: assume role sandbox → EC2 us-east-1 denied

## Terraform mirror (sau)

`terraform/environments/management` — module scp_deny_regions_sandbox
