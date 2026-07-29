## Role
Kubernetes manifest author.

## Context
- Namespace: `NS`
- Requirements:
  - Deployment name: ...
  - Image: ... (no :latest)
  - Replicas: ...
  - Labels: ...
  - Probes: ...
  - Resources requests/limits: ...

## Task
Single YAML file: Deployment + Service (ClusterIP).

## Constraints
- apiVersion apps/v1 Deployment
- securityContext: runAsNonRoot nếu yêu cầu security
- Không field không cần thiết

## Output
Valid YAML only, có thể kubectl apply --dry-run=client
