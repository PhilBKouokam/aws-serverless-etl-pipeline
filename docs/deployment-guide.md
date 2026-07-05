# Deployment Guide

This guide explains how to recreate the Serverless ETL Pipeline on AWS.

---

# Prerequisites

- AWS Account
- IAM User with Administrator permissions
- Python knowledge (basic)
- AWS Management Console

---

# AWS Services Used

- Amazon S3
- AWS Lambda
- AWS Glue
- IAM

---

# Deployment Steps

## 1. Create S3 Buckets

Create two buckets.

Example:

```
etl-input-bucket
etl-output-bucket
```

The first stores CSV files.

The second stores transformed JSON output.

---

## 2. Configure IAM Role

Create an IAM Role for AWS Glue with permissions for:

- Amazon S3
- AWS Glue
- CloudWatch Logs

Create another IAM Role for Lambda with permission to start Glue jobs.

---

## 3. Create AWS Glue Job

Configure:

- Source: CSV in S3
- Target: JSON in S3
- Output format: JSON

Give the job a name.

Example:

```
csv2json
```

---

## 4. Create Lambda Function

Upload the provided Python code:

```python
import json
import boto3

client = boto3.client("glue")

def lambda_handler(event, context):
    client.start_job_run(JobName="csv2json")
    return "Job has started"
```

Attach the Lambda IAM role.

---

## 5. Configure S3 Event Notification

Create an ObjectCreated trigger.

Target:

AWS Lambda Function

This automatically starts the ETL pipeline whenever a CSV file is uploaded.

---

## 6. Test the Pipeline

Upload a CSV file.

Expected sequence:

```
CSV Upload

↓

Amazon S3

↓

Lambda Trigger

↓

AWS Glue Job

↓

JSON Output

↓

Amazon S3
```

---

# Validation Checklist

- CSV upload succeeds
- Lambda executes
- Glue job starts
- JSON file generated
- Output stored in S3

---

# Security

Least-privilege IAM permissions were used.

Only required AWS services were granted access.

---

# Notes

The original AWS infrastructure has been deleted to prevent ongoing cloud costs.

The repository contains:

- Architecture diagrams
- Lambda source code
- Documentation

allowing the entire solution to be recreated.

---

# Future Improvements

Potential enhancements include:

- CloudFormation
- Terraform
- CloudWatch monitoring
- SNS alerts
- Step Functions orchestration
- GitHub Actions deployment
- Support for additional data formats

---

# Estimated Cost

AWS Free Tier eligible for most usage.

Running Glue jobs outside the Free Tier incurs additional charges.

---

# Author

Phillip-Bryan Kouokam

GitHub: https://github.com/PhilBKouokam