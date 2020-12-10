import json
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    client=boto3.resource('dynamodb')
    table=client.Table('B_data')
    
    response = table.query(
        KeyConditionExpression = Key('Date').eq('2020-12-3') & Key('Time').gt('19:49:09')
    )
    items = response['Items']
    for data in items:
        print(data)
