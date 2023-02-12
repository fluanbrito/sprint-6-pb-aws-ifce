import json
from datetime import datetime
from utils import functions

def health(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body)
    }
    return response

def v1_description(event, context):
    body = {
        "message": "TTS api version 1."
    }
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body)
    }
    return response

def v2_description(event, context):
    body = {
        "message": "TTS api version 2."
    }

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body)
    }

    return response

def tts_get(event, context):

    with open('templates/index.html', 'r') as f:
        html_content = f.read()
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
        },
        'body': html_content,
    }

def v1_tts(event, context):
    
    bibliotecas = functions.bibliotecas()
    dados = functions.dados(event, bibliotecas[2])
    functions.gerar_audio(dados[1], dados[4], dados[5], bibliotecas[0], bibliotecas[1])

    return functions.retorno(dados[1], '', dados[4], dados[5])

def v2_tts(event, context):
    
    bibliotecas = functions.bibliotecas()
    dados = functions.dados(event, bibliotecas[2])
    functions.gerar_audio(dados[1], dados[4], dados[5], bibliotecas[0], bibliotecas[1])
    functions.audio_dynamo(dados[1], dados[2], dados[3], dados[4], dados[5])

    return functions.retorno(dados[1], dados[3], dados[4], dados[5])
    

def v3_tts(event, context):
    
    bibliotecas = functions.bibliotecas()
    dados = functions.dados(event, bibliotecas[2])
    busca_dynamo = functions.busca_dynamo(dados[2], dados[3])

    if busca_dynamo is None:
        functions.gerar_audio(dados[1], dados[4], dados[5], bibliotecas[0], bibliotecas[1])
        functions.audio_dynamo(dados[1], dados[2], dados[3], dados[4], dados[5])

        return functions.retorno(dados[1], dados[3], dados[4], dados[5])
        
    else:
        return functions.retorno(dados[1], dados[3], dados[4], dados[5])