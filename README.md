# AWS Serverless ETL Pipeline

A production-style serverless Extract, Transform, Load (ETL) pipeline built on AWS that automatically converts CSV datasets into JSON using an event-driven architecture.

---

## Overview

This project demonstrates how multiple managed AWS services can be combined to build a scalable, serverless data processing workflow.

When a CSV file is uploaded to Amazon S3, an event automatically invokes an AWS Lambda function, which starts an AWS Glue ETL job. AWS Glue transforms the dataset into JSON and stores the processed output back in Amazon S3.

The solution eliminates the need to provision or manage servers while showcasing event-driven architecture, cloud automation, and managed ETL services.

---

## Architecture

![Architecture](docs/architecture.png)

---

## Architecture Flow

```text
CSV Upload
     │
     ▼
Amazon S3
     │
     ▼
S3 Event Notification
     │
     ▼
AWS Lambda
     │
     ▼
AWS Glue ETL Job
     │
     ▼
CSV → JSON Transformation
     │
     ▼
Processed JSON stored in Amazon S3
```

---

# Features

- Serverless ETL workflow
- Automatic event-driven processing
- CSV to JSON transformation
- AWS Glue job orchestration
- Lambda-triggered automation
- Scalable cloud-native architecture
- Infrastructure designed using AWS best practices
- Documentation for full deployment

---

# AWS Services Used

| Service | Purpose |
|----------|----------|
| Amazon S3 | Stores raw CSV files and processed JSON output |
| AWS Lambda | Triggers the ETL pipeline automatically |
| AWS Glue | Performs the CSV-to-JSON transformation |
| AWS IAM | Provides secure permissions between AWS services |

---

# Repository Structure

```text
aws-serverless-etl-pipeline/
│
├── lambda/
│   └── lambda_function.py
│
├── docs/
│   ├── architecture.drawio
│   ├── architecture.png
│   ├── deployment-guide.md
│   └── screenshots/
│
├── LICENSE
├── README.md
└── .gitignore
```

---

# How It Works

### 1. Upload Data

A CSV dataset is uploaded into an Amazon S3 bucket.

↓

### 2. Event Notification

Amazon S3 automatically emits an event notification.

↓

### 3. Lambda Execution

AWS Lambda receives the event and starts an AWS Glue ETL job.

↓

### 4. ETL Processing

AWS Glue reads the CSV file, transforms the data into JSON format, and prepares the output.

↓

### 5. Store Results

The processed JSON file is written back into Amazon S3.

---

# Lambda Function

The Lambda function acts as the orchestration layer for the pipeline.

```python
import json
import boto3

client = boto3.client('glue')

def lambda_handler(event, context):
    client.start_job_run(JobName="csv2json")
    return "Job has started"
```

Responsibilities:

- Receive S3 event notifications
- Invoke the AWS Glue ETL job
- Enable fully automated processing

---

# Engineering Decisions

## Why Amazon S3?

Amazon S3 provides durable, scalable object storage for both raw input files and transformed output datasets.

---

## Why AWS Lambda?

Lambda enables event-driven execution without managing servers and automatically scales based on incoming events.

---

## Why AWS Glue?

AWS Glue provides fully managed ETL capabilities that simplify large-scale data transformation while eliminating infrastructure management.

---

## Why Serverless?

Using managed AWS services reduces operational overhead, improves scalability, and allows engineers to focus on application logic instead of infrastructure.

---

# Skills Demonstrated

- AWS Cloud Architecture
- Event-Driven Systems
- Serverless Computing
- AWS Lambda
- AWS Glue
- Amazon S3
- IAM
- Python
- Cloud Automation
- ETL Pipelines
- Data Engineering Fundamentals

---

# Lessons Learned

During this project I gained hands-on experience with:

- Designing serverless architectures
- Building event-driven AWS workflows
- Connecting multiple managed AWS services
- Configuring IAM permissions
- Automating ETL pipelines
- Building reproducible cloud solutions

---

# Deployment Guide

A detailed deployment walkthrough is available here:

**docs/deployment-guide.md**

---

# Project Status

Completed

The AWS infrastructure used for this project has been intentionally removed after completion to avoid ongoing cloud costs.

The repository includes:

- Architecture diagrams
- Deployment documentation
- Lambda source code
- Complete project explanation

allowing the solution to be reproduced from scratch.

---

# Future Improvements

Potential enhancements include:

- Infrastructure as Code using Terraform or AWS CloudFormation
- CloudWatch monitoring and alarms
- Dead Letter Queue (DLQ) support
- Error notifications with Amazon SNS
- Automated deployment using GitHub Actions
- Support for additional file formats such as Parquet or Avro

---

# Author

**Phillip-Bryan Kouokam**

Portfolio: https://philbk.dev

GitHub: https://github.com/PhilBKouokam

LinkedIn: https://www.linkedin.com/in/phillip-bryan-kouokam