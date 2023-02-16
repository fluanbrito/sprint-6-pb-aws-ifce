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
    hash_texto = hashlib.md5(texto.encode('utf-8')).hexdigest()
    try:

        # Verifica se o hash já existe na tabela DynamoDB
        response = table.query(KeyConditionExpression=Key('id').eq(hash_texto))
        if response['Count'] > 0:
            # Se o hash já existir, retorna a URL do áudio salvo no S3
            url = response['Items'][0]['url']
            return jsonify({'url': url})
        else:
            # Se o hash não existir, converte o texto em áudio
            polly = boto3.client('polly', region_name='us-east-1')
            response = polly.synthesize_speech(Text=texto,
                                             OutputFormat='mp3',
                                             VoiceId='Camila')

            # Salva o arquivo de áudio no S3
            nome_arquivo = hash_texto + '.mp3'
            s3.put_object(Bucket='BUCKET_NAME',
                         Key=nome_arquivo, 
                         Body=response['AudioStream'].read())

            url = furl = "https://" \
            + str(os.environ['BUCKET_NAME']) \
            + ".s3.amazonaws.com/" \
            + str(identificador) \
            + ".mp3"

            # Salva a referência no DynamoDB
            table.put_item(Item={'id': hash_texto, 'url': url})
            return jsonify({'url': url})
    except ClientError as e:
        print(e.response['Error']['Message'])
        return jsonify({'error': 'Erro ao converter texto em áudio.'}), 500

if __name__ == '__main__':
    app.run()
