import boto3
import json
import uuid
import os
from datetime import datetime


def v1_tts(event, context):

    
    try:
        identificador = str(uuid.uuid4())
        payload = json.loads(event["body"])
        phrase = payload["phrase"]

        polly = boto3.Session(
            region_name='us-east-1').client('polly')
        
        response = polly.synthesize_speech(
            OutputFormat='mp3',
            Text=phrase,
            VoiceId="Camila"
        )

        nome_arquivo = identificador+".mp3"
        s3 = boto3.client('s3')

        s3.put_object(Key=nome_arquivo,
                      Bucket=['sprint6grupo1'],
                      Body=response['AudioStream'].read())

        url = "https://" \
            + str(['sprint6grupo1']) \
            + ".s3.amazonaws.com/" \
            + str(identificador) \
            + ".mp3"

        return {
            "status": 200,
            "body": {
                "received_phrase": phrase,
                "url_to_audio": url,
                "created_audio": f"{datetime.now()}"
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
