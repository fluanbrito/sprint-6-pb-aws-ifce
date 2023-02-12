![Logo_CompassoUOL_Positivo](https://user-images.githubusercontent.com/94761781/212589731-3d9e9380-e9ea-4ea2-9f52-fc6595f8d3f0.png)
# 📑 Avaliação Sprint 6 - Programa de Bolsas Compass.uol / AWS e IFCE

## 📌 Tópicos 

- [📝 Descrição do projeto](#-descrição-do-projeto)

- [🧑‍💻 Ferramentas e Tecnologias](#-ferramentas-e-tecnologias)

- [😌 Impedimentos resolvidos](#-impedimentos-resolvidos)

- [📝 Organização do código](#-descrição-do-projeto)

- [🖥 Captura de frase e converver em Audio MP3 via Polly(Rota 1 , Rota 2, Rota 3)](#%EF%B8%8F-captura-de-frase)

- [📤 Atividade - Parte 1(AWS Polly, Armazenamento S3, chamada da API)](#-cria%C3%A7%C3%A3o-atividade-parte1)

- [📤 Atividade - Parte 2(Hash, AWS Polly, Armazenamento S3, DynamoDB, Chamada API)](#-cria%C3%A7%C3%A3o-atividade-parte2)

- [📤 Atividade - Parte 3(Hash, AWS Polly, Armazenamento S3, DynamoDB)](#-cria%C3%A7%C3%A3o-atividade-parte3)

- [⬇️ Desenvolvimento da API](#%EF%B8%8F-desenvolvimento-api)

- [📤 Deploy](#deploy)

- [📌 Considerações finais](#finais)

## 📝 Descrição do projeto

#### Avaliação da Sexta sprint do programa de bolsas Compass.uol para formação em machine learning para AWS.
<p align="justify">

Com base nas atividades anteriores realizadas, foi criado uma página html que irá capturar uma frase qualquer inserida pelo usuário e transformará essa frase em um audio em mp3 via polly.

1. Criar uma branch para o grupo e efetuar o clone.

2. Instalar o framework serverless no computador.

3. Gerar as credenciais (AWS Acess Key e AWS Secret) na console AWS pelo IAM.

4. Em seguida inserido as credenciais e executado o comando de configuração de credenciais do serveless.

5. Deploy da solução na conta AWS.

6. Abrir o browser e confirmar que a solução está funcionando dos 3 endpoints(Rota 1, Rota 2, Rota 3).

7. Criar a rota /v1/tts que receberá um post(Rota 4).

8. Criar a rota /v2/tts que receberá um post(Rota 5).

9. Criar a rota /v3/tts que receberá um post(Rota 6).


 <br>
<hr>

## 🧑‍💻👩‍💻 Ferramentas e Tecnologias 
<br>

- Visual Studio Code
- Amazon Web Services(AWS Polly, S3, Dynamo DB, Lambda)
- Python
- HTML, CSS
- JavaScript

<hr>
<br>

## 😌 Impedimentos Resolvidos

<hr>
<br>

## 📝 Organização do Código

<hr>
<br>

## 🖥 Captura de frase e converver em Audio MP3 via Polly(Rota 1 , Rota 2, Rota 3)

```
import boto3
import json
from datetime import datetime
from io import BytesIO

def health(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body)
    }
    return response

def v1_description(event, context):
    body = {
        "message": "TTS api version 1."
    }
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body)
    }
    return response

def v2_description(event, context):
    body = {
        "message": "TTS api version 2."
    }
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body)
    }
    return response
```
Este é o código em Python para a API de geração de voz utilizando a Amazon Polly. A API tem três versões (v1, v2, v3) e cada uma das versões tem seu próprio endpoint para receber requisições.

A função health retorna uma mensagem "Go Serverless v3.0! Sua função foi executada com sucesso!" e a entrada do evento em formato JSON.

A função v1_description retorna a mensagem "TTS api version 1." em formato JSON.

A função v2_description retorna a mensagem "TTS api version 2." em formato JSON.

<hr>
<br>

## 📤 Atividade - Parte 1(AWS Polly, Armazenamento S3, chamada da API)

```
def v1_tts(event, context):
    phrase = event['phrase']
    s3 = boto3.client('s3')
    polly = boto3.client('polly')
    response = polly.synthesize_speech(
        OutputFormat='mp3',
        Text=phrase,
        VoiceId='Joanna'
    )
    audio = response['AudioStream'].read()

    filename = "audio-xyz.mp3"
    s3.put_object(
        Bucket='bucket-sprint6',
        Key=filename,
        Body=audio,
    )

    return {
        "received_phrase": phrase,
        "url_to_audio": f"https://bucket-sprint6.s3.amazonaws.com/{filename}",
        "created_audio": str(datetime.now())
    }
```

A função v1_tts recebe uma frase como entrada na requisição e usa a Amazon Polly para converter a frase em um arquivo de áudio MP3. Em seguida, o arquivo de áudio é salvo no Amazon S3 e a URL para o arquivo de áudio é retornada como resposta da API.

<hr>
<br>

## 📤 Atividade - Parte 2(Hash, AWS Polly, Armazenamento S3, DynamoDB, Chamada API)

```
def v2_tts(event, context):
    phrase = event['phrase']
    s3 = boto3.client('s3')
    polly = boto3.client('polly')
    response = polly.synthesize_speech(
        OutputFormat='mp3',
        Text=phrase,
        VoiceId='Joanna'
    )

    audio = response['AudioStream'].read()

    filename = "audio-xyz.mp3"
    s3.put_object(
        Bucket='bucket-sprint6',
        Key=filename,
        Body=audio,
    )

    hash_frase = str(hash(phrase))[1:len(phrase)]

    db = boto3.resource('dynamodb')
    table = db.Table("audio-data-sprint6")

    table.put_item(
        Item={
        'hash': hash_frase,
        'frase': phrase,
        'url':f"https://bucket-sprint6.s3.amazonaws.com/{filename}"
        }
    )
    return {
        "received_phrase": phrase,
        "url_to_audio": f"https://bucket-sprint6.s3.amazonaws.com/{filename}",
        "created_audio": str(datetime.now()),
        "unique_id": hash_frase
    }
```

A função v2_tts funciona de maneira semelhante à função v1_tts, mas também gera uma hash para a frase e salva a frase, a URL do arquivo de áudio e a hash em uma tabela no Amazon DynamoDB.

<hr>
<br>

## 📤 Atividade - Parte 3(Hash, AWS Polly, Armazenamento S3, DynamoDB)
```
def v3_tts(event, context):
    phrase = event['phrase']
    s3 = boto3.client('s3')
    polly = boto3.client('polly')
    response = polly.synthesize_speech(
        OutputFormat='mp3',
        Text=phrase,
        VoiceId='Joanna'
    )
    
    audio = response['AudioStream'].read()

    filename = "audio-xyz.mp3"
    s3.put_object(
        Bucket='bucket-sprint6',
        Key=filename,
        Body=audio,
    )
    return {
        "received_phrase": phrase,
        "url_to_audio": f"https://bucket-sprint6.s3.amazonaws.com/{filename}",
        "created_audio": str(datetime.now())
    }
```
A função v3_tts é similar à função v1_tts, mas não possui nenhuma funcionalidade adicional.

<hr>
<br>

## ⬇️ Desenvolvimento da API
```
from flask import Flask, render_template, flash, redirect, request, jsonify
import os
from handler import *

app = Flask(__name__)

@app.route('/')
def index():
    return health('','')
@app.route('/v1')
def v1_get():
    return v1_description('', '')
@app.route('/v2')
def v2_get():
    return v2_description('', '')

@app.route('/v1/tts', methods=['GET', 'POST'])
def v1_post():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        frase = {
            "phrase": request.form.get("textov1")
        }
        return v1_tts(frase, '')

@app.route('/v2/tts', methods=['GET','POST'])
def v2_post():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        frase = {
            "phrase": request.form.get("textov2")
        }
        return v2_tts(frase, '')

@app.route('/v3/tts', methods=['GET','POST'])
def v3_post():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        frase = {
            "phrase": request.form.get("textov3")
        }
        return v2_tts(frase, '')
```


A API em Python cria uma aplicação web usando o framework Flask.

A aplicação tem as seguintes rotas:

- '/': retorna o resultado da chamada à função "health"
- '/v1': retorna o resultado da chamada à função "v1_description"
- '/v2': retorna o resultado da chamada à função "v2_description"
- '/v1/tts': retorna o resultado da chamada à função "v1_tts". Este é um recurso que permite enviar uma solicitação POST que inclui um formulário de texto. O conteúdo do formulário é enviado como uma frase que é passada como um dicionário à função "v1_tts". Se for uma solicitação GET, será renderizada a página "index.html".
- '/v2/tts': funciona de forma semelhante à rota '/v1/tts', mas chama a função "v2_tts" em vez de "v1_tts".
- '/v3/tts': funciona de forma semelhante à rota '/v2/tts', mas chama a função "v2_tts" em vez de "v3_tts".

As funções "health", "v1_description", "v2_description", "v1_tts" e "v2_tts" são importadas do módulo "handler".

A aplicação é iniciada com o comando "app.run(debug=True)" é a porta para a qual a aplicação deve escutar é definida como "5000" ou a porta especificada na variável de ambiente "PORT".
<hr>
<br>

## 📤 Deploy


<br>

<br>
<hr>

## ♾️ Equipe
- Davi Santos
- Edivalço Araújo
- Luan Ferreira
- Nicolas


<br>

<hr>

## 📌 Considerações finais

<br>

Em resumo, o projeto envolvendo o uso da plataforma AWS com Amazon Polly, Amazon S3, Dynamo DB foi muito proveitoso. 

Com uso de Amazon Polly é possível gerar fala sintetizada com qualidade humana, enquanto Amazon S3 fornece armazenamento de arquivos para armazenar as respostas geradas. DynamoDB, por sua vez, é uma base de dados NoSQL de alta disponibilidade que pode ser usada para armazenar informações sobre as respostas geradas, incluindo data e hora de geração, parâmetros de fala e outros dados relevantes.

Além disso, o uso destes três serviços da Amazon juntos teve potencial de proporcionar escalabilidade, segurança e facilidade de gerenciamento para o projeto.

Em resumo, a combinação de Amazon Polly, Amazon S3 e DynamoDB é uma solução poderosa e flexível para aplicações de inteligência artificial de fala que permite aos usuários transformar texto em fala natural de forma rápida e fácil, garantindo a escalabilidade, segurança e facilidade de gerenciamento do projeto.
