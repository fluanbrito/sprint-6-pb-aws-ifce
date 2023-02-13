![imagem compass](https://vetores.org/d/compass-uol.svg)
### Atividade Avaliativa - Referente a 6° Sprint do programa de Bolsas Compass UOL 
 
### Projeto foi desenvolvido por: 

* [@Dayanne Bugarim](https://github.com/dayannebugarim)
* [@Jhonatan Lobo](https://github.com/JhonatanLobo)
* [@Tecla Fernandes](https://github.com/TeclaFernandes)

### Recursos necessários

 - [Visual Studio Code](https://code.visualstudio.com/)
 - [Amazon Web Services](https://aws.amazon.com/pt/)
 - HTML
 - [Python](https://www.python.org/) 
### Objetivos da Avaliação
Construir uma aplicação que receba input's em uma página HTML, capture essa frase e faça a transformação dela para um arquivo de audio MP3 via polly, após isso retorne o arquivo de audio para o usuário.

Passos do desenvolvimento da avaliação
* Criação de Branch e Clone de arquivos
* Gerenciamento de credenciais AWS
* Execução (código fonte)
* Deploy

### Organização dos arquivos 

![imagem arquivos](https://i.imgur.com/n9FVOry.jpg)

* ### Construção da avaliação
Instalação framework serverless 
```
npm install -g serverless
```
#### Exemplos de códigos construidos 
### main.py
``` 
from templates.main import main_page

def index(event, context):
    return {
        'statusCode': 200,
        'body': main_page(),
        'headers': {
            'Content-Type': 'text/html'
        }
    }
```
### form 
```
def main_page():
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Conversor de Texto para Áudio</title>
        </head>
        <body>
            <h1>Conversão de Texto para Áudio</h1>
            <div class="container">
                <a href="/v1">V1</a>
                <a href="/v2">V2</a>
                <a href="/v3">V3</a>
            </div>
        </body>
        </html>
```

### v1
```
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
```
### v2
```
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
```
### v3
```
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
```
### Functions 
```

import boto3

def generateAudioWithPolly(phrase):
    polly = boto3.client('polly')

    return polly.synthesize_speech(
        Text=phrase,
        VoiceId='Vitoria',
        OutputFormat='mp3'
    )

def storeAudioOnS3(file_name, response):
    s3 = boto3.client('s3')
    s3.put_object(
        Bucket='api-tts-audio-storage',
        Key=file_name,
        Body=response['AudioStream'].read()
    )

def saveReferenceOnDynamoDB(unique_id, phrase, file_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('api-tts-references')
    table.put_item(
        Item={
            'unique_id': unique_id,
            'received_phrase': phrase,
            'url_to_audio': f'https://api-tts-audio-storage.s3.amazonaws.com/{file_name}'
        }
    )
```
### Deploy


