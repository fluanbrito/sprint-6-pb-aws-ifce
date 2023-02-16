import boto3
import hashlib
import os
import json
from datetime import datetime

def v3_tts(event, context):
    try:
        # Obtém o texto do corpo da solicitação
        text = event["phrase"]

        # Calcula o hash do texto para verificar se já foi convertido antes
        hash_ = hashlib.md5(text.encode('utf-8')).hexdigest()

        dynamoDB = boto3.resource('dynamodb')
        tabela = dynamoDB.Table("sprint6grupo1")

        # Verifica se o hash já existe na tabela DynamoDB
        response = tabela.get_item(
                Key = {
                    "unique_id": hash_
                }
        )
        response = json.loads(json.dumps(response))
        if len(response.keys()) > 1:
            return {
            "status": 200,
            "body": {
                "received_phrase": text,
                "url_to_audio": response["Item"]["url"],
                "created_audio": f"{datetime.now()}",
                "unique_id": response["Item"]["unique_id"]
            }
        }
    
        else:
                # Se o hash não existir, converte o texto em áudio
            text = event["phrase"]

            polly = boto3.Session(
                region_name='us-east-1').client('polly')

            response = polly.synthesize_speech(
                OutputFormat='mp3',
                Text=text,
                VoiceId="Camila"
            )

            nome_arquivo = "audio-"+ hash_

            s3 = boto3.client('s3')

            s3.put_object(Key=nome_arquivo,
                          Bucket=os.environ['BUCKET_NAME'],
                          Body=response['AudioStream'].read())

            dynamoDB = boto3.resource('dynamodb')

            tabela = dynamoDB.Table("sprint6grupo1")

            hash_ = hashlib.md5(text.encode('utf-8')).hexdigest()

            url = "https://" \
                + str(os.environ['BUCKET_NAME']) \
                + ".s3.amazonaws.com/" \
                + nome_arquivo \
                + ".mp3"


            tabela.put_item(
                Item= {
                    "unique_id": hash_,
                    "phrase": text,
                    "url": url
                }
            )

        return {
            "status": 200,
            "body": {
                "received_phrase": text,
                "url_to_audio": url,
                "created_audio": f"{datetime.now()}",
                "unique_id": hash_
            }
        }

    except Exception as err:
        return {
        "status": 500,
        "error": {
            "type": type(err).__name__,
            "message": str(err),
            }
        }