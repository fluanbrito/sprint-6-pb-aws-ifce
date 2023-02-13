import boto3
import os
import uuid
import json
import logging


#criação da tabela
def get_dynamo_table():
    dynamodb = boto3.resource("dynamodb")
    table_name = os.environ['TabelaPolly']
    return dynamodb.Table(table_name)

#Pesquisando Itens
def list(event, context):
    table = get_dynamo_table()
    return table.scan()['Items']

#Modo create
def list(event, context):
    body = event["body"]
    table = get_dynamo_table()
    lista = table.scan()['Items']
    try:
        for e in lista:

            if("id" in body):
                body = {
                    "received_phrase": "converta esse texto para áudio",
                    "url_to_audio": "https://meu-buckect/audio-xyz.mp3",
                    "created_audio": "02-02-2023 17:00:00",
                    "unique_id": "123456"
                    }
                response = {"status": 200,
                    "body": json.dumps(body)}
                return response

                    
            else:
                table = get_dynamo_table()

                table.put_item(
                    Item={
                        "id": str(uuid.uuid4()),
                        "frase":  body["frase"],
                        "url": body["url"],
                    }
                )
            
                body = {
                    
                "received_phrase": "converta esse texto para áudio",
                "url_to_audio": "https://meu-buckect/audio-xyz.mp3",
                "created_audio": "02-02-2023 17:00:00",
                "unique_id": "123456"
            }
                
            response = {"status": 200,
                    "body": json.dumps(body)}

            return response
    except:
            return {"status": 500,
                    "body": "Error"}
        
    