import boto3
import urllib.parse
import hashlib
import json
import datetime
from templates.templates import form


def v2_form(event, context):
    return {
        'statusCode': 200,
        'body': form('/v2/tts', 'V2 - Armazenamento no S3 e DynamoDB'),
        'headers': {
            'Content-Type': 'text/html'
        }
    }

def v2_tts(event, context):
    try:
        # recebe a frase do formulário
        body = event['body']
        parsed_body = urllib.parse.parse_qs(body)
        phrase = parsed_body.get('phrase')[0]

        # retirando caracteres de quebra de linha
        if phrase.find("\r\n"):
            phrase = phrase.replace("\r\n", "")

        print(phrase)
        
        # gera o id unico para a frase
        unique_id = hashlib.sha256(phrase.encode()).hexdigest()[:6]
        print(unique_id)
        
        # gera o audio usando o polly
        polly = boto3.client('polly')
        response = polly.synthesize_speech(
            Text=phrase,
            VoiceId='Vitoria',
            OutputFormat='mp3'
        )
        
        # formatação para o nome do arquivo e url
        file_name = 'audio_' + unique_id + '.mp3'
        
        # salva o audio no bucket
        s3 = boto3.client('s3')
        s3.put_object(
            Bucket='api-tts-audio-storage',
            Key=file_name,
            Body=response['AudioStream'].read()
        )
        
        # formatação da data
        date_string = response['ResponseMetadata']['HTTPHeaders']['date']
        date_object = datetime.datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S %Z')
        formatted_date = date_object.strftime('%d-%m-%Y %H:%M:%S')
        
        # salva uma referencia no dynamoDB
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('api-tts-references')
        table.put_item(
            Item={
                'unique_id': unique_id,
                'received_phrase': phrase,
                'url_to_audio': f'https://api-tts-audio-storage.s3.amazonaws.com/{file_name}'
            }
        )
        
        # retorna a resposta em json formatado
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'received_phrase': phrase,
                'url_to_audio': f'https://api-tts-audio-storage.s3.amazonaws.com/{file_name}',
                'created_audio': formatted_date,
                'unique_id': unique_id
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': str(e)
            })
        }