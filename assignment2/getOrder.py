import boto3
import json

print('Invoking getPizzaMenu function')

def lambda_handler(event, context):
    print ('printing event and context')
    print (event)
    print (event['order_id'])
    table  = boto3.resource('dynamodb').Table('Order')
    response = table.get_item(
        Key={
            'order_id': event['order_id']
        }
    )
    item = response['Item']
    print(item)
    item.pop('processing_state', None)
    return item
