import boto3
import json
import hashlib

polly_client = boto3.client('polly')
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def list(event, context):
    try:
        if():
            lista = table.scan()['Items']
            for e in lista:
                if("id" in lista):
                    response = polly_client.synthesize_speech(
                    OutputFormat='mp3',
                    Text=phrase,
                    VoiceId='Vitoria'
                )

                audio = response['AudioStream'].read()
                
                s3_client.put_object(
                    Body=audio,
                    Bucket='bucketpollysprint6',
                    Key=f'{unique_id}.mp3',
                )

                audio_url = f'https://s3.amazonaws.com/bucketpollysprint6/{unique_id}.mp3'
                return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Frase convertida para audio com sucesso!',
                                    'audio_url': audio_url})}
            
        else:
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
                Bucket='bucketpollysprint6',
                Key=f'{unique_id}.mp3',
            )

            audio_url = f'https://s3.amazonaws.com/bucketpollysprint6/{unique_id}.mp3'
            
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
                'body': json.dumps({'message': 'Frase convertida para audio com sucesso!',
                                    'audio_url': audio_url})
            }
    except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'message': 'Erro ao converter frase para audio',
                                    'error': str(e)})
            }
