import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('minister')

def lambda_handler(event, context):
    response = table.get_item(
        Key={
            'department':'health'
        }    
    )
    print(response)
    return {
        'statusCode': 200,
        'body': response
    }

