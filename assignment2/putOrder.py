import boto3
import json

print('Invoking getOrder function')

def lambda_handler(event, context):
    print ('printing event and context')
    print (event)
    print (event['order_id'])
    table  = boto3.resource('dynamodb').Table('Order')
    table_menu = boto3.resource('dynamodb').Table('Menus')
    response = table.get_item(
        Key={
            'order_id': event['order_id']
        }
    )
    item = response['Item']
    menu_response = table_menu.get_item(
        Key={
            'menu_id': item['menu_id']
        }
    )
    menu = menu_response['Item']
    if(item['processing_state'] == 1):
        item['order']['selection'] = menu['selection'][int(event['input'])]
        item['processing_state'] = 2
        table.put_item(Item =  item)
        print(item)
        item.pop('processing_state', None)
        data = {}
        sel = ' '
        i = 0
        while i < len(menu['size']):
            sel = sel + str(i + 1) + ". " + menu['size'][i] + " "
            i += 1
        data['Message'] = "Hi, Which size do you want?" + sel
        json_data = json.dumps(data)
        return json_data
    elif(item['processing_state'] == 2):
        item['order']['size'] = menu['size'][int(event['input'])]
        item['order']['costs'] = menu['price'][int(event['input'])]
        item['processing_state'] = 3
        table.put_item(Item=item)
        print(item)
        item.pop('processing_state', None)
        data = {}
        data['Message'] = "Your order costs $"+menu['price'][int(event['input'])]+". We will email you when the order is ready. Thank you!"
        json_data = json.dumps(data)
        return json_data


    return "Order completed!! please wait for email"