"""Shared utilities for AWS Infra module."""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

try:
    import boto3
    from botocore.exceptions import ClientError, NoCredentialsError, ProfileNotFound
except ImportError:
    boto3 = None

PROJECT_TAG_KEY = "Project"
PROJECT_TAG_VALUE = "python-all-learn"
DEFAULT_REGION = os.environ.get("AWS_DEFAULT_REGION", "ap-southeast-1")


@dataclass
class AWSContext:
    session: Any
    region: str
    account_id: str
    arn: str


def get_session(region: str | None = None) -> Any:
    if boto3 is None:
        raise ImportError("pip install boto3")
    return boto3.Session(region_name=region or DEFAULT_REGION)


def get_context(region: str | None = None) -> AWSContext:
    session = get_session(region)
    sts = session.client("sts")
    identity = sts.get_caller_identity()
    return AWSContext(
        session=session,
        region=session.region_name or DEFAULT_REGION,
        account_id=identity["Account"],
        arn=identity["Arn"],
    )


def default_tags() -> list[dict[str, str]]:
    return [
        {"Key": PROJECT_TAG_KEY, "Value": PROJECT_TAG_VALUE},
        {"Key": "ManagedBy", "Value": "python-all-learn"},
        {"Key": "Environment", "Value": "learning"},
    ]


def tag_dict() -> dict[str, str]:
    return {t["Key"]: t["Value"] for t in default_tags()}


def dry_run_message(action: str, details: str, apply: bool) -> None:
    prefix = "🔧 APPLY" if apply else "🔍 DRY-RUN"
    print(f"{prefix} | {action}")
    print(f"         {details}")


def handle_aws_error(exc: Exception) -> str:
    if isinstance(exc, NoCredentialsError):
        return "❌ Chưa cấu hình AWS credentials. Chạy: aws configure"
    if isinstance(exc, ProfileNotFound):
        return f"❌ AWS profile không tồn tại: {exc}"
    if isinstance(exc, ClientError):
        return f"❌ AWS Error: {exc.response['Error']['Code']} — {exc.response['Error']['Message']}"
    return f"❌ {exc}"


def load_infra_config(path: str) -> dict:
    import yaml
    from pathlib import Path
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))
