from templates.form import form
from functions.aws_services import generateAudioWithPolly, storeAudioOnS3
from functions.helpers import getPhrase, generateFileName, dateFormatting

import json

def v1_form(event, context):
    return {
        'statusCode': 200,
        'body': form('/v1/tts', 'V1 - Armazenamento no S3'),
        'headers': {
            'Content-Type': 'text/html'
        }
    }

def v1_tts(event, context):
    try: 
        phrase = getPhrase(event)

        polly_response = generateAudioWithPolly(phrase)

        file_name = generateFileName(phrase)

        storeAudioOnS3(file_name, polly_response)

        formatted_date = dateFormatting(polly_response)

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'received_phrase': phrase,
                'url_to_audio': f'https://api-tts-audio-storage.s3.amazonaws.com/{file_name}',
                'created_audio': formatted_date
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