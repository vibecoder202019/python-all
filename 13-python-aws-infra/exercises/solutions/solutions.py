"""
Module 13 — Đáp án bài tập AWS (boto3)
Chạy: python exercises/solutions/solutions.py
      (cần AWS credentials: aws configure hoặc env vars)

YÊU CẦU ĐỀ BÀI:
  - list_s3_buckets(): liệt kê bucket S3 (tên + ngày tạo)
  - ec2_cost_estimate(): ước lượng chi phí EC2 theo giờ × số giờ/tháng
  - check_tag_compliance(): tìm EC2 instance thiếu tag bắt buộc

KẾT QUẢ MONG ĐỢI (khi chạy):
  - Có credentials: in số bucket, ước lượng t3.micro/month (~$7.59)
  - Không có credentials: in "Chưa cấu hình AWS credentials"
"""
import boto3
from botocore.exceptions import NoCredentialsError


def list_s3_buckets() -> list[dict]:
    """Gọi S3 API list_buckets — trả list dict name + created."""
    s3 = boto3.client("s3")
    return [
        {"name": b["Name"], "created": b["CreationDate"].strftime("%Y-%m-%d")}
        for b in s3.list_buckets().get("Buckets", [])
    ]


def ec2_cost_estimate(instance_type: str = "t3.micro", hours: int = 730) -> float:
    """Ước lượng đơn giản — t3.micro ~$0.0104/giờ, 730h ≈ 1 tháng."""
    hourly_rates = {"t3.micro": 0.0104, "t3.small": 0.0208, "t3.medium": 0.0416}
    rate = hourly_rates.get(instance_type, 0.05)
    return round(rate * hours, 2)


def check_tag_compliance(tag_key: str = "Environment") -> list[str]:
    """Trả instance_id của EC2 đang chạy nhưng thiếu tag tag_key."""
    ec2 = boto3.client("ec2")
    non_compliant = []
    for r in ec2.describe_instances()["Reservations"]:
        for inst in r["Instances"]:
            if inst["State"]["Name"] == "terminated":
                continue
            tags = {t["Key"]: t["Value"] for t in inst.get("Tags", [])}
            if tag_key not in tags:
                non_compliant.append(inst["InstanceId"])
    return non_compliant


if __name__ == "__main__":
    try:
        buckets = list_s3_buckets()
        print(f"S3 buckets: {len(buckets)}")
        print(f"t3.micro/month: ${ec2_cost_estimate()}")
    except NoCredentialsError:
        print("Chưa cấu hình AWS credentials")
