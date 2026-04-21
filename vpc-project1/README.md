# AWS Production Grade Application Deployment using Public and Private Subnets

Real-time AWS project demonstrating secure application deployment inside private subnets using Bastion Host, Application Load Balancer, and Multi-AZ architecture.

---
<img width="611" height="481" alt="vpc-example-private-subnets" src="https://github.com/user-attachments/assets/cbbe0415-20e8-48c3-b30f-e0eda0b35714" />



# Project Overview

This project demonstrates how to deploy an application securely in AWS using a production-style network architecture.

The application servers are hosted inside private subnets, while users access the application through an Application Load Balancer deployed in public subnets.

Administrative access to private servers is provided through a Bastion Host.

This architecture is commonly used in production environments for security, high availability, and traffic management.

---

# Architecture

```text id="u83kwe"
                         Internet Users
                               │
                               ▼
                      Internet Gateway
                               │
                               ▼
                Application Load Balancer
                     (Public Subnets)
                               │
                  ┌────────────┴────────────┐
                  ▼                         ▼
          EC2 Instance 1             EC2 Instance 2
         Private Subnet              Private Subnet
        ap-southeast-2a             ap-southeast-2b

Outbound Internet Access:
Private EC2 → NAT Gateway → Internet

Administrative Access:
Laptop → Bastion Host → Private EC2
```

---

# AWS Services Used

| Service                   | Purpose                                |
| ------------------------- | -------------------------------------- |
| Amazon Web Services VPC   | Isolated network                       |
| Public Subnets            | ALB and Bastion Host                   |
| Private Subnets           | Application servers                    |
| Internet Gateway          | Public internet access                 |
| NAT Gateway               | Outbound internet from private servers |
| Amazon EC2                | Application hosting                    |
| Application Load Balancer | Traffic distribution                   |
| Auto Scaling Group        | Multi-instance deployment              |
| Launch Template           | EC2 template configuration             |
| Security Groups           | Firewall rules                         |

---

# Availability Zones

* `ap-southeast-2a`
* `ap-southeast-2b`

Using two Availability Zones increases availability and fault tolerance.

---

# Application Deployed

File: `myapp/app.js`

```javascript id="dj27pe"
const http = require('http');

http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.end('<h1>Hello from EC2 Server!</h1><p>Application deployed successfully.</p>');
}).listen(3000, '0.0.0.0');

console.log("Running on port 3000");
```

---

# Implementation Steps

## 1. Created VPC using AWS VPC Wizard

Created:

* 2 Public Subnets
* 2 Private Subnets
* Route Tables
* Internet Gateway
* NAT Gateway

## 2. Created Auto Scaling Group

Configured:

* Launch Template
* 2 EC2 Instances
* Instances distributed across:

  * `ap-southeast-2a`
  * `ap-southeast-2b`

## 3. Created Bastion Host

* Bastion Host launched in Public Subnet
* Used for SSH access to private EC2 instances

```text id="gr5x8f"
Local Machine → Bastion Host → Private EC2
```

## 4. Deployed Node.js Application

* Connected to Bastion Host
* Connected to private servers
* Created `myapp/app.js`
* Started application on port `3000`

Run command:

```bash id="u3v2fr"
cd myapp
node app.js
```

## 5. Created Application Load Balancer

Configured:

* Internet-facing ALB
* Public subnets attached
* Listener enabled
* Security Group updated

## 6. Added EC2 Instances as Targets

* Registered both EC2 instances
* Health checks enabled
* ALB routed traffic to healthy targets

---

# Traffic Flow

```text id="c1r7ma"
User Request
   ↓
Internet Gateway
   ↓
Application Load Balancer
   ↓
Private EC2 Instances
```

---

# Security Design

* Backend servers do not have public IP addresses
* Only ALB is publicly accessible
* SSH access allowed only through Bastion Host
* Security Groups restrict inbound traffic
* Private servers use NAT Gateway for outbound internet access

---

# Validation

Accessed application using ALB DNS URL:

project-vpc-load-balancer-609031527.ap-southeast-2.elb.amazonaws.com


# Result:

<img width="1920" height="1080" alt="Screenshot (14)" src="https://github.com/user-attachments/assets/7c00876c-568e-4ea1-8c46-84bc73a2f41f" />



# Key Learning Outcome

This project helped in understanding how real-world production applications are securely deployed inside private subnets while exposing only the Load Balancer to users.

---



Successfully implemented a production-grade AWS deployment architecture using VPC, private subnets, NAT Gateway, Bastion Host, Auto Scaling Group, and Application Load Balancer across two Availability Zones.
