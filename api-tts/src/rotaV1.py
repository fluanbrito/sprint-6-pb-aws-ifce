import boto3
import json
import datetime
import unicodedata

polly_client = boto3.client('polly')
s3_client = boto3.client('s3')

def tts(event, context):
    try:

        phrase = json.loads(event['body'])['phrase']

        response = polly_client.synthesize_speech(
            OutputFormat='mp3',
            Text=phrase,
            VoiceId='Vitoria'
        )

        audio = response['AudioStream'].read()
        phrase = unicodedata.normalize('NFKD', str(phrase).replace(" ", ""))
        phrase = "".join([c for c in phrase if not unicodedata.combining(c)])
        
        s3_client.put_object(
            Body=audio,
            Bucket='audios-sprint-6-grupo-4',
            Key=f'{phrase}.mp3',
        )

        time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'Frase convertida para audio com sucesso!',
                            'audio_url': f'https://s3.amazonaws.com/audios-sprint-6-grupo-4/{phrase}.mp3',
                            'timestamp': time})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Erro ao converter frase para audio',
                                'error': str(e)})
        }


