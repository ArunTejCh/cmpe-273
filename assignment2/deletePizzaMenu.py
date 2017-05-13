from __future__ import print_function

import boto3
import json

print('Invoking deletePizzaMenu function')

def lambda_handler(event, context):
    print ('printing event and context')
    print (event)
    print (event['menu_id'])
    table  = boto3.resource('dynamodb').Table('Menus')
    response = table.delete_item(
        Key={
            'menu_id': event['menu_id']
        }
    )
    return 200
