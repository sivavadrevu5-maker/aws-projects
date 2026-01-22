# CloudWatch Application Monitoring Project

## Project Objective
The goal of this project is to understand how **AWS CloudWatch monitors an application** by collecting application logs from an EC2 instance and making them available in CloudWatch Logs.  
This project focuses on **log-based monitoring**.
---

## Architecture Overview

User  
→ EC2 Instance (Application)  
→ Application Log File  
→ CloudWatch Agent  
→ CloudWatch Logs  

---

## AWS Services Used
- Amazon EC2
- AWS IAM
- Amazon CloudWatch (Logs)
- CloudWatch Agent

---

## Step-by-Step Implementation

### Step 1: Launch EC2 Instance
- Launched an **Ubuntu EC2 instance**
- Allowed inbound access:
  - SSH (22)
  - HTTP (80)
- Attached an IAM role with the policy:
  - `CloudWatchAgentServerPolicy`

This role allows the EC2 instance to send logs to CloudWatch securely without using access keys.

---

### Step 2: Connect to EC2
Connected to the instance using SSH.

```bash
ssh -i <key.pem> ubuntu@<EC2_PUBLIC_IP>
