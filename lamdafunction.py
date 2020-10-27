import boto3
import json
from boto3.dynamodb.conditions import Key
dynamo = boto3.resource("dynamodb")
table = dynamo.Table("Water_level_table")
def lambda_handler(event,context):
    response = table.query(KeyConditionExpression=Key('Row').eq(str(event['Row'])))
    for i in response['Items']:
        pay = (i['payload'])
    return pay