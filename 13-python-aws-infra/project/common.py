"""
Module 13 — Tiện ích dùng chung cho dự án AWS Infra

Quản lý session boto3, tag dự án, xử lý lỗi AWS và đọc config YAML —
dùng lại ở step01→step06 và scripts/destroy_resources.py.

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Tạo boto3 Session và lấy thông tin caller identity (STS).
  2. Định nghĩa tag mặc định Project=python-all-learn cho mọi tài nguyên.
  3. Cung cấp helper dry_run_message, handle_aws_error, load_infra_config.

KẾT QUẢ MONG ĐỢI:
  - get_context() trả AWSContext(session, region, account_id, arn).
  - default_tags() trả list tag chuẩn cho EC2/S3/SG.
  - handle_aws_error() in thông báo tiếng Việt khi thiếu credentials.
═══════════════════════════════════════════════════════════════════════════
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

try:
    import boto3
    from botocore.exceptions import ClientError, NoCredentialsError, ProfileNotFound
except ImportError:
    boto3 = None

# ── Tag dùng để nhận diện tài nguyên do module này tạo ──
PROJECT_TAG_KEY = "Project"
PROJECT_TAG_VALUE = "python-all-learn"

# ── Region mặc định — ưu tiên biến môi trường AWS_DEFAULT_REGION ──
DEFAULT_REGION = os.environ.get("AWS_DEFAULT_REGION", "ap-southeast-1")


@dataclass
class AWSContext:
    """Thông tin phiên làm việc AWS sau khi xác thực STS."""
    session: Any
    region: str
    account_id: str
    arn: str


def get_session(region: str | None = None) -> Any:
    """Tạo boto3 Session — raise ImportError nếu chưa cài boto3."""
    if boto3 is None:
        raise ImportError("pip install boto3")
    return boto3.Session(region_name=region or DEFAULT_REGION)


def get_context(region: str | None = None) -> AWSContext:
    """Kết nối STS, lấy Account ID và ARN của caller hiện tại."""
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
    """Tag chuẩn gắn lên EC2, S3, Security Group khi tạo tài nguyên."""
    return [
        {"Key": PROJECT_TAG_KEY, "Value": PROJECT_TAG_VALUE},
        {"Key": "ManagedBy", "Value": "python-all-learn"},
        {"Key": "Environment", "Value": "learning"},
    ]


def tag_dict() -> dict[str, str]:
    """Chuyển default_tags sang dict {Key: Value} cho API cần dict."""
    return {t["Key"]: t["Value"] for t in default_tags()}


def dry_run_message(action: str, details: str, apply: bool) -> None:
    """In log DRY-RUN hoặc APPLY trước khi thực thi thao tác AWS."""
    prefix = "🔧 APPLY" if apply else "🔍 DRY-RUN"
    print(f"{prefix} | {action}")
    print(f"         {details}")


def handle_aws_error(exc: Exception) -> str:
    """Chuyển exception AWS sang thông báo tiếng Việt dễ hiểu."""
    if isinstance(exc, NoCredentialsError):
        return "❌ Chưa cấu hình AWS credentials. Chạy: aws configure"
    if isinstance(exc, ProfileNotFound):
        return f"❌ AWS profile không tồn tại: {exc}"
    if isinstance(exc, ClientError):
        return f"❌ AWS Error: {exc.response['Error']['Code']} — {exc.response['Error']['Message']}"
    return f"❌ {exc}"


def load_infra_config(path: str) -> dict:
    """Đọc file YAML cấu hình infra (instance type, bucket name, ...)."""
    import yaml
    from pathlib import Path
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))
