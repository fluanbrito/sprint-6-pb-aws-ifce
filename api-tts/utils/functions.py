import boto3
import json
import inspect
from datetime import datetime

def dados(event, db):
    # Carrega o body da requisição processada pelo script, extraindo a frase
    payload = json.loads(event["body"])
    phrase = payload["phrase"]

    # Gera um hash aleatório para a frase
    hash_frase = str(hash(phrase))[1:len(phrase)]
    filename = f"{hash_frase}.mp3"
    bucket = "bucket-sprint6"
    table = db.Table("audio-data-sprint6")
    
    return payload, phrase, table, hash_frase, filename, bucket

def bibliotecas():
    # Inicializa o client do s3, polly e dynamodb
    s3 = boto3.client('s3')
    polly = boto3.client('polly', region_name='us-east-1')
    db = boto3.resource('dynamodb')

    return s3, polly, db

def gerar_audio(phrase, filename, bucket, s3, polly):

    # Gera o áudio mp3 baseado na frase digitada pelo usuário, com a voz de "Camila"
    response = polly.synthesize_speech(
        OutputFormat='mp3',
        Text=phrase,
        VoiceId='Camila'
    )
    audio = response['AudioStream'].read()

    # Insere o áudio no bucket do S3
    s3.put_object(
        Bucket=bucket,
        Key=filename,
        Body=audio,
    )

def audio_dynamo(phrase, table, hash_frase, filename, bucket):

    # Insere ID, frase e url do áudio na tabela do DynamoDB
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
    
    # Se a rota socilitada for /v1/tts, retorna a frase, url e data da criação do áudio em JSON.
    if (caller.function == 'v1_tts'):
        return {
            "received_phrase": phrase,
            "url_to_audio": f"https://{bucket}.s3.amazonaws.com/{filename}",
            "created_audio": str(datetime.now())
        }
    # Caso for /v2/tts ou /v3/tts, retorna também a hash da frase
    else:
        return {
            "received_phrase": phrase,
            "url_to_audio": f"https://{bucket}.s3.amazonaws.com/{filename}",
            "created_audio": str(datetime.now()),
            "unique_id": hash_frase
        }

def busca_dynamo(table, hash_frase):

    # Busca no DynamoDB por uma hash idêntica à gerada pela frase e, caso encontre, retorna o item que já existe na tabela
    response = table.get_item(Key={'hash': hash_frase})
    item = response.get("Item")

    return item