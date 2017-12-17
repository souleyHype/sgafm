import json

def handler(event, context):
    response = json.dumps({
        "statusCode": 200,
        "body": "Hello World"
    })

    return json.loads(response)