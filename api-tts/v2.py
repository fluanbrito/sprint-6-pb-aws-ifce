import boto3
import os
import hashlib
from datetime import datetime


def v2_tts(event, context):
    try:

        text = event["phrase"]

        polly = boto3.Session(
            region_name='us-east-1').client('polly')
        
        response = polly.synthesize_speech(
            OutputFormat='mp3',
            Text=text,
            VoiceId="Camila"
        )

        hash_ = hashlib.md5(text.encode('utf-8')).hexdigest()
        nome_arquivo = "audio-"+ hash_

        s3 = boto3.client('s3')

        s3.put_object(Key=nome_arquivo,
                      Bucket=os.environ['BUCKET_NAME'],
                      Body=response['AudioStream'].read())

        dynamoDB = boto3.resource('dynamodb')

        tabela = dynamoDB.Table("sprint6grupo1")

        
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
