# CloudWatch Application Monitoring Project

## Project Objective
The goal of this project is to understand how **AWS CloudWatch monitors an application** by collecting application logs from an EC2 instance and making them available in CloudWatch Logs.  
This project focuses on **log-based monitoring**, not alerting or autoscaling.

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
Step 3: Create a Simple Application
Created a basic Python HTTP server

The application:

Writes normal requests as INFO logs

Writes error requests as ERROR logs

Logs are written to:

lua
Copy code
/var/log/app.log
This simulates a real application generating logs.

Step 4: Verify Application Logs
Verified that the application was generating logs correctly.

bash
Copy code
sudo cat /var/log/app.log
Confirmed that both INFO and ERROR messages were being written.

Step 5: Install CloudWatch Agent (Ubuntu)
Downloaded and installed the CloudWatch Agent on Ubuntu using a .deb package.

bash
Copy code
wget https://s3.amazonaws.com/amazoncloudwatch-agent/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb
sudo dpkg -i amazon-cloudwatch-agent.deb
Step 6: Configure CloudWatch Agent
Created a CloudWatch Agent configuration file to collect application logs.

Log file path:

lua
Copy code
/var/log/app.log
Log group name:

pgsql
Copy code
app-log-group
This configuration instructs the agent to push application logs to CloudWatch Logs.

Step 7: Start CloudWatch Agent
Started the CloudWatch Agent with the custom configuration.

bash
Copy code
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
-a fetch-config \
-m ec2 \
-c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json \
-s
Step 8: Verify Logs in CloudWatch
Navigated to CloudWatch → Logs → Log groups

Confirmed that:

app-log-group was created

Application logs were visible in CloudWatch Logs

At this point, application log monitoring using CloudWatch was successfully implemented.

