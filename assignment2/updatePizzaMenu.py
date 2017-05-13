from __future__ import print_function

import boto3
import json

print('Invoking updatePizzaMenu function')

def lambda_handler(event, context):
    print ('printing event and context')
    print (event)
    print (event['menu_id'])
    table  = boto3.resource('dynamodb').Table('Menus')
    table.update_item(
        Key={
            'menu_id': event['menu_id']
        },
        UpdateExpression='SET selection = :val1',
        ExpressionAttributeValues={
            ':val1': event['selection']
        }
    )
    return 200