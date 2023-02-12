import boto3
import json
import inspect
from datetime import datetime

def dados(event, db):

    payload = json.loads(event["body"])
    phrase = payload["phrase"]
    hash_frase = str(hash(phrase))[1:len(phrase)]
    filename = f"{hash_frase}.mp3"
    bucket = "bucket-sprint6-edi"
    table = db.Table("table-sprint6-edi")
    
    return payload, phrase, table, hash_frase, filename, bucket

def bibliotecas():

    s3 = boto3.client('s3')
    polly = boto3.client('polly', region_name='us-east-1')
    db = boto3.resource('dynamodb')

    return s3, polly, db

def gerar_audio(phrase, filename, bucket, s3, polly):

    response = polly.synthesize_speech(
        OutputFormat='mp3',
        Text=phrase,
        VoiceId='Camila'
    )
    audio = response['AudioStream'].read()

    s3.put_object(
        Bucket=bucket,
        Key=filename,
        Body=audio,
    )

def audio_dynamo(phrase, table, hash_frase, filename, bucket):

    table.put_item(
        Item={
        'hash': hash_frase,
        'frase': phrase,
        'url':f"https://{bucket}.s3.amazonaws.com/{filename}"
        }
    )

def retorno(phrase, hash_frase, filename, bucket):

    stack = inspect.stack()
    caller = stack[1]
    
    if (caller.function == 'v1_tts'):
        return {
            "received_phrase": phrase,
            "url_to_audio": f"https://{bucket}.s3.amazonaws.com/{filename}",
            "created_audio": str(datetime.now())
        }

    else:
        return {
            "received_phrase": phrase,
            "url_to_audio": f"https://{bucket}.s3.amazonaws.com/{filename}",
            "created_audio": str(datetime.now()),
            "unique_id": hash_frase
        }

def busca_dynamo(table, hash_frase):

    response = table.get_item(Key={'hash': hash_frase})
    item = response.get("Item")

    return item