"""
Đáp án tham khảo — Module 15 Bài tập
Chỉ xem sau khi đã tự làm!
"""
from __future__ import annotations


def get_job_count(client) -> int:
    """Bài 1: Đếm số job trong AWX."""
    result = client.get("/jobs/", params={"page_size": 1})
    return result.get("count", 0)


def launch_with_vars_file(client, template_id: int, vars_path: str) -> int:
    """Bài 2: Launch job với file JSON extra vars."""
    import json
    from pathlib import Path
    extra = json.loads(Path(vars_path).read_text(encoding="utf-8"))
    result = client.launch_job(template_id, extra_vars=extra)
    return result.get("job")


def list_minio_objects(endpoint: str, bucket: str, prefix: str = "") -> list[str]:
    """Bài 3: Liệt kê object trong MinIO bucket."""
    import boto3
    from botocore.client import Config
    s3 = boto3.client(
        "s3",
        endpoint_url=endpoint,
        aws_access_key_id="minioadmin",
        aws_secret_access_key="minioadmin123",
        config=Config(signature_version="s3v4"),
        region_name="us-east-1",
    )
    resp = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
    return [obj["Key"] for obj in resp.get("Contents", [])]
