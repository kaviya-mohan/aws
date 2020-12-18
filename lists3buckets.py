import json
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    list_of_bucket = []
    for buck in s3.buckets.all():
        print(buck.name)
        list_of_bucket.append(buck.name)
    return {
        'statusCode': 200,
        'body': list_of_bucket
    }

