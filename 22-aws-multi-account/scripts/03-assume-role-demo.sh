#!/usr/bin/env bash
# Demo assume role cross-account
set -euo pipefail

DEV_ACCOUNT_ID="${DEV_ACCOUNT_ID:?Set DEV_ACCOUNT_ID}"
ROLE_NAME="${ROLE_NAME:-DevOpsCrossAccountRole}"
EXTERNAL_ID="${EXTERNAL_ID:-lab-module-22-dev}"
ROLE_ARN="arn:aws:iam::${DEV_ACCOUNT_ID}:role/${ROLE_NAME}"

echo "Assume role: $ROLE_ARN"
CREDS=$(aws sts assume-role \
  --role-arn "$ROLE_ARN" \
  --role-session-name module22-lab \
  --external-id "$EXTERNAL_ID" \
  --output json)

export AWS_ACCESS_KEY_ID=$(echo "$CREDS" | jq -r .Credentials.AccessKeyId)
export AWS_SECRET_ACCESS_KEY=$(echo "$CREDS" | jq -r .Credentials.SecretAccessKey)
export AWS_SESSION_TOKEN=$(echo "$CREDS" | jq -r .Credentials.SessionToken)

echo "Caller identity in dev account:"
aws sts get-caller-identity

echo ""
echo "Thu list S3 (scoped policy):"
aws s3 ls 2>&1 | head -5 || true

unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN
