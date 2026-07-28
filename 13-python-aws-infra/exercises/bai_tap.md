# Bài tập Module 13: Python & AWS

## Bài 1: Liệt kê S3 buckets (Dễ)
Viết script in tên và ngày tạo của tất cả S3 buckets.

## Bài 2: EC2 cost estimator (Dễ)
Viết hàm tính chi phí ước lượng EC2 t3.micro chạy 730 giờ/tháng (~$7.5).

## Bài 3: Tag compliance checker (Trung bình)
Quét EC2 instances không có tag `Environment` → báo cáo.

## Bài 4: S3 upload CLI (Trung bình)
Thêm lệnh `upload` vào step06_final.py: upload file lên bucket.

## Bài 5: Multi-region inventory (Khó)
Liệt kê số EC2 running ở 3 regions: ap-southeast-1, us-east-1, eu-west-1.

## Bài 6: CloudFormation deploy (Khó)
Dùng boto3 cloudformation client deploy stack từ `data/generated/stack_template.json`.

Đáp án: [exercises/solutions/solutions.py](exercises/solutions/solutions.py)
