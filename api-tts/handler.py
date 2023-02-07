import json


def health(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def v1_description(event, context):
    body = {
        "message": "TTS api version 1."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def v2_description(event, context):
    body = {
        "message": "TTS api version 2."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def v1_tts(event, context):
    body = {
        "message": "Teste rota v1_tts."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def v2_tts(event, context):
    body = {
        "message": "Teste rota v2_tts."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def v3_tts(event, context):
    body = {
        "message": "Teste rota v3_tts."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response