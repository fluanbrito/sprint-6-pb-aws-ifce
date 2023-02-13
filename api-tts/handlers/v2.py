from templates.form import form
from functions.aws_services import *
from functions.helpers import *

import json

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
        phrase = getPhrase(event)

        unique_id = generateUniqueId(phrase)

        polly_response = generateAudioWithPolly(phrase)

        file_name = generateFileName(unique_id)

        storeAudioOnS3(file_name, polly_response)

        formatted_date = dateFormatting(polly_response)
        
        saveReferenceOnDynamoDB(unique_id, phrase, file_name)
        
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