# ☁️ Introduction to Amazon EC2 - Hands-On Lab
# This project provides a step-by-step guide for launching, monitoring, resizing, and managing an Amazon EC2 instance.
# The lab was completed as part of a cloud fundamentals exercise.

# 🧠 Lab Objectives
# - Launch a web server with termination protection enabled
# - Monitor EC2 instance health and performance
# - Configure security groups to allow HTTP access
# - Resize the instance and EBS volume
# - Test termination protection and safely terminate the instance

# 🕒 Duration
# Approx. 45 minutes

# 🚀 Steps Covered

# 🔐 Accessing AWS Console
# 1. Start the lab and open AWS Console from the lab environment
# 2. Ensure the AWS region is correct and resources are provisioned

# 🛠️ Task 1: Launch an EC2 Instance
# 1. Service: Navigate to EC2 Dashboard → Launch Instance
# 2. Name: Web Server
# 3. AMI: Amazon Linux 2 (default)
# 4. Instance Type: t3.micro
# 5. Key Pair: Proceed without one
# 6. Network Settings:
#    - VPC: Lab VPC
#    - Security Group: Create new named Web Server security group
#    - Remove SSH access (better security)
# 7. Storage: Default 8 GiB EBS
# 8. Advanced Details:
#    - Enable termination protection
#    - Add User Data script:
"""
#!/bin/bash
yum -y install httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>Hello From Your Web Server!</h1></html>' > /var/www/html/index.html
"""
# 9. Launch the instance

# 📈 Task 2: Monitor Your Instance
# - Check EC2 instance status (2/2 checks passed)
# - View metrics under Monitoring (CloudWatch)
# - Use Get Instance Screenshot for diagnostics

# 🔒 Task 3: Modify Security Group for HTTP Access
# - Copy the Public IPv4 of your instance
# - Try accessing it via browser → it fails (port 80 blocked)
# - Modify the security group:
#   - Add rule: HTTP (port 80), source: Anywhere (IPv4)
# - Refresh browser → “Hello From Your Web Server!”

# ⚙️ Task 4: Resize Instance and Disk
# - Stop the instance
# - Change instance type to t3.small
# - Resize EBS volume from 8 GiB to 10 GiB
# - Start the instance again

# 🧪 Task 5: Test Termination Protection
# - Attempt to terminate instance → Error (protection enabled)
# - Disable termination protection
# - Terminate instance successfully

# ✅ Lab Completed
# The EC2 instance was successfully launched, configured, monitored, resized, and terminated.
# This exercise provided a hands-on understanding of AWS EC2 functionality and best practices in cloud security and scalability.