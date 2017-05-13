from __future__ import print_function

import boto3
import json

print('Invoking postPizzaMenu function')

def lambda_handler(event, context):
    print ('In post lambda handler')
    print (event)
    print (context)
    table  = boto3.resource('dynamodb').Table('Menus')
    table.put_item ( Item =  event)
    return 200

