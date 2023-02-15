import boto3
import json
import hashlib
import datetime

polly_client = boto3.client('polly')
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')


def create(event, context):
    try:
        phrase = json.loads(event['body'])['phrase']

        # Criar ID único para a frase
        unique_id = hashlib.sha256(phrase.encode()).hexdigest()

        response = polly_client.synthesize_speech(
            OutputFormat='mp3',
            Text=phrase,
            VoiceId='Vitoria'
        )

        audio = response['AudioStream'].read()

        s3_client.put_object(
            Body=audio,
            Bucket='audios-sprint-6-grupo-4',
            Key=f'{unique_id}.mp3',
        )

        audio_url = f'https://s3.amazonaws.com/audios-sprint-6-grupo-4/{unique_id}.mp3'

        # Salvar referencia no DynamoDB
        table = dynamodb.Table('TTS_References')
        table.put_item(
            Item={
                'id': unique_id,
                'phrase': phrase,
                'audio_url': audio_url
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'received_phrase': phrase,
                'url_to_audio': audio_url,
                'created_audio':  datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                'unique_id':  unique_id
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Erro ao converter frase para audio',
                                'error': str(e)}),
        }
