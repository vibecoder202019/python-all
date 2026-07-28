"""
Module 13 — Ví dụ 5: CloudWatch — metrics, alarms, log groups

Chạy: python examples/05_cloudwatch.py

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Liệt kê 5 log groups đầu tiên (tên và stored bytes).
  2. Lấy metric CPUUtilization của EC2 running (nếu có).
  3. Liệt kê alarms và dashboard count.

KẾT QUẢ MONG ĐỢI (in ra terminal):
  - "Log Groups (N shown):" kèm tên và KB.
  - CPU metric hoặc "(no running instances)".
  - Alarms count và "✓ Done".
═══════════════════════════════════════════════════════════════════════════
"""
import sys
from datetime import datetime, timedelta, timezone

try:
    import boto3
    from botocore.exceptions import ClientError, NoCredentialsError
except ImportError:
    print("pip install boto3")
    sys.exit(1)


def main():
    print("=== CloudWatch ===\n")

    try:
        cw = boto3.client("cloudwatch")
        logs = boto3.client("logs")
    except NoCredentialsError:
        print("❌ Chưa cấu hình AWS credentials")
        return

    # Log groups
    log_groups = logs.describe_log_groups(limit=5)["logGroups"]
    print(f"1. Log Groups ({len(log_groups)} shown):")
    for lg in log_groups:
        print(f"   {lg['logGroupName']:50s} {lg.get('storedBytes', 0) // 1024} KB")

    # EC2 CPU metric (if instances exist)
    ec2 = boto3.client("ec2")
    instances = [
        i["InstanceId"]
        for r in ec2.describe_instances()["Reservations"]
        for i in r["Instances"]
        if i["State"]["Name"] == "running"
    ][:1]

    if instances:
        iid = instances[0]
        print(f"\n2. CPU Utilization — {iid} (last 1 hour):")
        end = datetime.now(timezone.utc)
        start = end - timedelta(hours=1)
        metrics = cw.get_metric_statistics(
            Namespace="AWS/EC2",
            MetricName="CPUUtilization",
            Dimensions=[{"Name": "InstanceId", "Value": iid}],
            StartTime=start,
            EndTime=end,
            Period=3600,
            Statistics=["Average"],
        )
        for dp in metrics["Datapoints"]:
            print(f"   Average CPU: {dp['Average']:.1f}%")
    else:
        print("\n2. Không có EC2 running — bỏ qua CPU metric")

    # Alarms
    alarms = cw.describe_alarms(MaxRecords=5)["MetricAlarms"]
    print(f"\n3. CloudWatch Alarms ({len(alarms)} shown):")
    for alarm in alarms:
        state = alarm["StateValue"]
        icon = "🔴" if state == "ALARM" else "🟢"
        print(f"   {icon} {alarm['AlarmName']:40s} {state}")

    print(f"\n4. CloudWatch use cases:")
    print("   • Monitor EC2 CPU, memory, disk")
    print("   • Set alarms → SNS notification")
    print("   • Centralize logs từ app/EC2")
    print("   • Dashboard cho team")

    print("\n✓ Done")


if __name__ == "__main__":
    main()
