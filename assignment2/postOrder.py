import boto3
import json
import time

print('Invoking postOrder function')

def lambda_handler(event, context):
    print ('In post lambda handler')
    print (event)
    print (context)
    table  = boto3.resource('dynamodb').Table('Order')
    event['order_status'] = 'processing'
    event['order'] = {}
    event['order']['selection'] = 'NA'
    event['order']['size'] = 'NA'
    event['order']['costs'] = 'NA'
    event['order']['order_time'] = time.strftime("%d-%m-%Y@%H:%M:%S")
    event['processing_state'] = 1
    table.put_item ( Item =  event)
    menu_table  = boto3.resource('dynamodb').Table('Menus')
    response = menu_table.get_item(
        Key={
            'menu_id': event['menu_id']
        }
    )
    menu = response['Item']
    print ('Got menu as')
    print (menu)
    data = {}
    sel = ' '
    i = 0
    while i < len(menu['selection']):
        sel = sel + str(i + 1) +". "+ menu['selection'][i] + " "
        i += 1
    data['Message'] = "Hi "+ event['customer_name']+", please choose one of these selection" + sel
    json_data = json.dumps(data)
    return json_data
