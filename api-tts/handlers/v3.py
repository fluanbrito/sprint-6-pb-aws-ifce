from templates.form import form
from functions.aws_services import *
from functions.helpers import *

import boto3
import json

def v3_form(event, context):
    return {
        'statusCode': 200,
        'body': form('/v3/tts', 'V3 - Armazenamento no S3 e DynamoDB (verifica a existência do item)'),
        'headers': {
            'Content-Type': 'text/html'
        }
    }

def v3_tts(event, context):
    try:
        phrase = getPhrase(event)
        
        unique_id = generateUniqueId(phrase)
        
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('api-tts-references')

        response = table.get_item(Key={'unique_id': unique_id})
        # verifica a existencia do item na tabela
        if 'Item' in response:
            item = response['Item']
            print(f'{unique_id} já existe no DynamoDB')
            return {
                'received_phrase': item['received_phrase'],
                'url_to_audio': item['url_to_audio'],
                'unique_id': item['unique_id']
            }
        
        polly_response = generateAudioWithPolly(phrase)
        
        file_name = generateFileName(unique_id)
        
        storeAudioOnS3(file_name, polly_response)
        
        formatted_date = dateFormatting(polly_response)
        
        table.put_item(
            Item={
                'unique_id': unique_id,
                'received_phrase': phrase,
                'url_to_audio': f'https://api-tts-audio-storage.s3.amazonaws.com/{file_name}'
            }
        )
        
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