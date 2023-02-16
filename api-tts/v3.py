import boto3
import hashlib
import json
import uuid
import os
from datetime import datetime
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

def v1_tts(event, context):
    try:
    # Obtém o texto do corpo da solicitação
         text = event["phrase"]

    # Calcula o hash do texto para verificar se já foi convertido antes
    hash_ = hashlib.md5(text.encode('utf-8')).hexdigest()
    try:

        # Verifica se o hash já existe na tabela DynamoDB
        response = tabela.query(KeyConditionExpression=Key('id').eq(hash_))
        if response['Count'] > 0:
            # Se o hash já existir, retorna a URL do áudio salvo no S3
            url = response['Items'][0]['url']
            return jsonify({'url': url})
        else:
            # Se o hash não existir, converte o texto em áudio
            polly = boto3.client('polly', region_name='us-east-1')
            response = polly.synthesize_speech(Text=text,
                                             OutputFormat='mp3',
                                             VoiceId='Camila')

            # Salva o arquivo de áudio no S3
            nome_arquivo = hash_ + '.mp3'
            s3.put_object(Bucket='BUCKET_NAME',
                         Key=nome_arquivo, 
                         Body=response['AudioStream'].read())

            url = furl = "https://" \
            + str(os.environ['BUCKET_NAME']) \
            + ".s3.amazonaws.com/" \
            + str(identificador) \
            + ".mp3"

            # Salva a referência no DynamoDB
            tabela.put_item(Item={'unique_id': hash_, 
                                'phrase': text, 
                                'url': url})

            return jsonify({
                'url': url,
                    "status": 200,
                "body": {
                "received_phrase": text,
                "url_to_audio": url,
                "created_audio": f"{datetime.now()}",
                "unique_id": hash_
            }
        })

    except ClientError as e:
        print(e.response['Error']['Message'])
        return jsonify({'error': 'Erro ao converter texto em áudio.'}), 500