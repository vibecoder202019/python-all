# Console checklist — Organizations (in nhanh)

1. [ ] Login AWS Console (admin)
2. [ ] Search "Organizations" → Create organization → All features
3. [ ] AWS accounts → note Management ID
4. [ ] Create OU: Workloads, Security, Sandbox
5. [ ] Add account → Create → dev-workload + unique email
6. [ ] Wait ACTIVE → move to Workloads OU
7. [ ] Settings → copy Organization ID (o-xxx)
8. [ ] CLI: aws organizations list-accounts

# IAM Identity Center

1. [ ] Enable IAM Identity Center
2. [ ] Users → Create dev.engineer
3. [ ] Groups → DevOps
4. [ ] AWS accounts → Assign Dev account + permission set

# Cross-account role (in Dev account)

1. [ ] Switch role → OrganizationAccountAccessRole
2. [ ] IAM → Roles → Create DevOpsCrossAccountRole
3. [ ] Trust management account + external ID
4. [ ] Inline policy devops-scoped.json
