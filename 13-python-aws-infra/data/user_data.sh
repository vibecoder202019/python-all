#!/bin/bash
# EC2 User Data — chạy khi instance khởi động lần đầu
yum update -y
yum install -y python3 python3-pip httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Python All Learn — AWS EC2 Ready!</h1>" > /var/www/html/index.html
echo "Setup completed at $(date)" >> /var/log/user-data.log
