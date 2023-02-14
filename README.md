# Avaliação Sprint 6 - Programa de Bolsas Compass.uol / AWS e IFCE

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/LogoCompasso-positivo.png/440px-LogoCompasso-positivo.png)](https://compass.uol/pt/home/)

Avaliação da sexta sprint do programa de bolsas Compass UOL para formação em machine learning para AWS.

***

## Sumário
* [Objetivo](#objetivo)
* [Ferramentas](#ferramentas)
* [Desenvolvimento](#desenvolvimento)
  * [Conversão para áudio](#conversão-de-texto-em-áudio-via-polly)
  * [Arquitetura serverless](#estrutura-serverless)

## Objetivo

Realizar a conversão de texto para áudio utilizando *text to speech* e salvá-lo em um banco de dados.

***

## Ferramentas

* [AWS](https://aws.amazon.com/pt/) plataforma de computação em nuvem da Amazon.
  * [Polly](https://aws.amazon.com/polly/) funcionalidade ideal para sintetizar discurso a partir de texto em uma variedade de vozes e idiiomas.
  * [DynamoDB](https://aws.amazon.com/dynamodb/) banco de dados não relacional que oferece rápida e escalável performance.
  * [S3](https://aws.amazon.com/s3/) serviço de armazenamento.
  * [API Gateway](https://aws.amazon.com/api-gateway/) serviço para criação, implantação e gerenciamento de APIs.
  * [Lambda](https://aws.amazon.com/lambda/) serviço de computação *serverless* que permite a execução de código sem a preocupação de gerenciar servidores.

***

## Desenvolvimento

### Conversão de texto em áudio via Polly

```py
def health(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def v1_description(event, context):
    body = {
        "message": "TTS api version 1."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def v2_description(event, context):
    body = {
        "message": "TTS api version 2."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
```
Esse [trecho de código](https://github.com/Compass-pb-aws-2022-IFCE/sprint-6-pb-aws-ifce/blob/Grupo-5/api-tts/handler.py) permite a geração de voz pela Amazon e contém os *endpoints* da API.

### Estrutura serverless

```yml
service: api-tts
frameworkVersion: '3'

provider:
  name: aws
  runtime: python3.9

functions:
  health:
    handler: handler.health
    events:
      - httpApi:
          path: /
          method: get
  v1Description:
    handler: handler.v1_description
    events:
      - httpApi:
          path: /v1
          method: get
  v2Description:
    handler: handler.v2_description
    events:
      - httpApi:
          path: /v2
          method: get
  v1_tts:
    handler: routers/rota1.v1_tts
    events:
      - http:
          path: v1/tts
          method: post
  v2_tts:
    handler: routers/rota2.v2_tts
    events:
      - http:
          path: v2/tts
          method: post
  v3_tts:
    handler: routers/rota3.v3_tts
    events:
      - http:
          path: v3/tts
          method: post
```

O [arquivo YAML](https://github.com/Compass-pb-aws-2022-IFCE/sprint-6-pb-aws-ifce/blob/Grupo-5/api-tts/serverless.yml) define uma aplicação *serverless* na AWS utilizando o serviço de *text-to-speech*.

O bloco de *functions* que definem o serviço de TTS, sendo elas:
* **health** retorna uma resposta em JSON ao ser acionada pelo método GET no caminho raiz "/".
* **v1Description**, **v2Description**, e **v3Description** são acionadas por um GET para os endpoints **/v1**, **/v2**, **/v3** respectivamente.
* Já as funções **v1_tts**, **v2_tts**, e **v3_tts** são ativadas pelo método POST para as rotas **/v1/tts**, **/v2/tts**, e **/v3/tts**.

# Polly to S3
Este script tem como objetivo criar um áudio utilizando a tecnologia Polly da Amazon Web Services (AWS) e armazenar esse áudio no serviço S3 também da AWS.

## Funcionamento 
O script recebe como entrada uma string que será utilizada para criar o áudio. A biblioteca boto3 é utilizada para se conectar à API Polly e criar o áudio, além de armazená-lo no S3.

O arquivo de áudio é salvo com o nome "polly-X.mp3", onde X é o número de arquivos já presentes na pasta do bucket do S3. Além disso, é gerado um link de acesso público ao arquivo armazenado no S3.

O script também retorna um objeto JSON com as informações da frase utilizada para criar o áudio, o link de acesso ao arquivo de áudio e a data e hora em que o arquivo foi criado.
```sh
import datetime
import json
from datetime import timedelta

import boto3


def polly_to_s3(text):
    polly = boto3.client('polly')
    s3 = boto3.client('s3')

    bucket = 'polly-spint6'
    result = s3.list_objects(Bucket=bucket)
    count = result.get('Contents', [])

    response = polly.synthesize_speech(
        VoiceId='Ricardo',
        OutputFormat='mp3',
        Text=str(text)
    )

    s3.put_object(
        Body=response['AudioStream'].read(),
        Bucket='polly-spint6',
        Key='polly-'+str(len(count))+'.mp3'
    )

    url= s3.generate_presigned_url(
    ClientMethod='get_object',
    Params={
        'Bucket': bucket,
        'Key': 'polly-'+str(len(count))+'.mp3'
    })
    

    brasilia_offset = timedelta(hours=-3)
    brasilia_time = datetime.datetime.utcnow() + brasilia_offset
    formatted_time = brasilia_time.strftime("%Y-%m-%d %H:%M:%S")

    dados = {
        "received_phrase": str(text),
        "url_to_audio": url,
        "created_audio": formatted_time
    }

    return json.dumps(dados)


```

## Uso

```sh
polly_to_s3("Texto a ser transformado em áudio")
```
## Saída
```sh
{
    "received_phrase": "Texto a ser transformado em áudio",
    "url_to_audio": "https://polly-spint6.s3.amazonaws.com/polly-X.mp3",
    "created_audio": "2023-02-13 12:34:56"
}
```


### Rotas
