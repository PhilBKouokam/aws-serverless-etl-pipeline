import json
import boto3

client = boto3.client('glue')

def lambda_handler(event, context):
    client.start_job_run(JobName="csv2json")
    return "Job has started"