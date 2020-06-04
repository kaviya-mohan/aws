import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('minister')

def lambda_handler(event, context):
    table.put_item(
        Item={
             'department': 'education',
             'name': 'sengottaiyan'
        }
    )
    response = {
        'message': 'Item added'
    }
    return {
        'statusCode': 200,
        'body': response
    }

