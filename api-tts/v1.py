import boto3
import json
import uuid
import os
from datetime import datetime


def v1_tts(event, context):
    try:
        identificador = str(uuid.uuid4())
        text = event["phrase"]

        with open("../.config/credentials.json", "r") as file:
            credentials = json.load(file)

        polly = boto3.Session(
            aws_access_key_id=credentials["aws_access_key_id"],
            aws_secret_access_key=credentials["aws_secret_access_key"],
            region_name='us-east-1').client('polly')

        response = polly.synthesize_speech(
            OutputFormat='mp3',
            Text=text,
            VoiceId="Camila"
        )

        nome_arquivo = identificador+".mp3"
        s3 = boto3.client('s3')

        s3.put_object(Key=nome_arquivo,
                      Bucket=os.environ['BUCKET_NAME'],
                      Body=response['AudioStream'].read())

        url = "https://" \
            + str(os.environ['BUCKET_NAME']) \
            + ".s3.amazonaws.com/" \
            + str(identificador) \
            + ".mp3"

        return {
            "status": 200,
            "body": {
                "received_phrase": text,
                "url_to_audio": url,
                "created_audio": f"{datetime.now()}"
            }
        }
    except Exception as err:
        return {
            "status": 500,
            "error" : err
        }
