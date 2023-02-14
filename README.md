![imagem compass](https://vetores.org/d/compass-uol.svg)
### Atividade Avaliativa - Referente a 6° Sprint do programa de Bolsas Compass UOL 
 
### Projeto foi desenvolvido por: 

* [@Dayanne Bugarim](https://github.com/dayannebugarim)
* [@Jhonatan Lobo](https://github.com/JhonatanLobo)
* [@Tecla Fernandes](https://github.com/TeclaFernandes)

# Recursos necessários

 - [Visual Studio Code](https://code.visualstudio.com/)
 - [Amazon Web Services](https://aws.amazon.com/pt/)
 - HTML
 - [Python](https://www.python.org/) 
# Objetivos da Avaliação
Construir uma aplicação que receba input's em uma página HTML, capture essa frase e faça a transformação dela para um arquivo de audio MP3 via polly, após isso retorne o arquivo de audio para o usuário.

Passos do desenvolvimento da avaliação
* Criação de Branch e Clone de arquivos
* Gerenciamento de credenciais AWS
* Execução (código fonte)
* Deploy

# Organização dos arquivos 

A imagem abaixo mostra commo está organizado o projeto e suas subdivisões.

![imagem arquivos](https://i.imgur.com/n9FVOry.jpg)

# Construção da avaliação
Instalação framework serverless 
```
npm install -g serverless
```
Em seguida foi gerado as credenciais na aws e configuradas com o seguinte código.

```py
serverless config credentials -o --provider aws --key {key} --secret {secret}
```
> **key** e **secret** são informados ao gerar as credenciais.

Obs.: código todo na mesma linha pra evitar erro.

# Códigos construidos
## Captura e conversão da frase em audio via Polly

O código permite a conversão do texto em audio pela AWS.

```py
def getPhrase(event):
    body = event['body']
    parsed_body = urllib.parse.parse_qs(body)
    phrase = parsed_body.get('phrase')[0]

    # retirando caracteres de quebra de linha
    if phrase.find("\r\n"):
        phrase = phrase.replace("\r\n", "")
    
    return phrase

def generateFileName(phrase):
    if len(phrase) > 6:
        return 'audio_' + phrase[:20].replace(" ", "_") + '.mp3'
        
    return 'audio_' + phrase + '.mp3'

def dateFormatting(response):
    date_string = response['ResponseMetadata']['HTTPHeaders']['date']
    date_object = datetime.datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S %Z')

    return date_object.strftime('%d-%m-%Y %H:%M:%S')

def generateUniqueId(phrase):
    return hashlib.sha256(phrase.encode()).hexdigest()[:6]
```

---

## main.py
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
---
## form 
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
---
## Function v1

O código começa fazendo os imports nescessarios, em seguida pega os dados nescessarios a partir dos eventos passados como argumetos, gera os audios e retorna um arquivo JSON.

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

---

## Function v2

O código faz os imports nescessarios e coleta os dados significativos sobre os eventos passados como argumentos, após isso ela armazena no S3.AWS e DynamoDB, depois lhes retorna em resposta um JSON com as informações geradas.

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

---

## Function v3

Por fim, após realizar os imports nescessarios, a função coleta os dados nescessarios para conseguir gerar o audio que foram armazenados no S3 e DynamoDB. Logo após, o código verifica a existencia do item na tabela, em caso positivo a função é chamada sem precisar fazer nenhuma outra ação para retornar os dados expressivos e em caso negativo é chamada novamente a função pra gerar e efetuar o armazenamento para assim retornar os dados eexpressivos.

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

---

## Functions 
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
---
## Estrutura do serverless

```py
service: api-tts
frameworkVersion: '3'

provider:
  name: aws
  runtime: python3.9

functions:
  index:
    handler: main.index
    events:
      - httpApi:
          path: /
          method: get
  v1_form:
    handler: handlers/v1.v1_form
    events:
      - httpApi:
          path: /v1
          method: get
  v2_form:
    handler: handlers/v2.v2_form
    events:
      - httpApi:
          path: /v2
          method: get
  v3_form:
    handler: handlers/v3.v3_form
    events:
      - httpApi:
          path: /v3
          method: get
  v1_tts:
    handler: handlers/v1.v1_tts
    events:
      - httpApi:
          path: /v1/tts
          method: post
  v2_tts:
    handler: handlers/v2.v2_tts
    events:
      - httpApi:
          path: /v2/tts
          method: post
  v3_tts:
    handler: handlers/v3.v3_tts
    events:
      - httpApi:
          path: /v3/tts
          method: post
```

> O **HANDLER** é ativada por um método Get que retorna na rota **/**

> Os **v1_form**, **v2_form** e **v3_form** são acionados por um método Get que retornam na rota **/v1**, **/v2** e **/v3**

>Os **v1_tts**, **v2_tts** e **v3_tts** são acionadas por um método Post que retornam na **/v1/tts**, **/v2/tts** e **/v1/tts**

# Deploy

Efetuando o deploy

```py
$ serverless deploy
```

Em seguida deve aparecer uma tela mais ou menos assim: 

*[tela pós deploy]*

# Dificuldades
* Ao configurar pra receber o JSON
