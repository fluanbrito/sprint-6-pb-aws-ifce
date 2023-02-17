# Aplicação que receba inputs de 3 rotas em uma página HTML, para um arquivo de audio MP3 via polly, após isso retorne o arquivo de audio para o usuário

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/LogoCompasso-positivo.png/440px-LogoCompasso-positivo.png)](https://compass.uol/pt/home/)

Este arquivo tem o objetivo de documentar o desenvolvimento de uma plicação em python que obtenha uma página simples HTML responsável por receber os inputs de 3 rotas, capture a frase e converta ela num arquivo de audio via polly, por fim retorne o arquivo.

A apresentação será desenrolada em duas etapas principais, sendo-as:
- Execução (código fonte)
- Deploy.

### Sumário
- Organização e preparação da aplicação
- Ferramentas
- Comandos

# Organização e preparação da aplicação
![estrutura_arquivos_sprint6](https://user-images.githubusercontent.com/119500249/219551929-ee86fe3c-853a-4314-988a-cd4e304dbe4d.png)
Segue o exemplo de como vai ficar a organização dos arquivos, cada qual com teus arquivos e pastas separadas.

## Ferramentas

As principais ferramentas utilizadas no projeto foram:

- [Python](https://www.python.org/) - Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte.
- [HTML] - O que é HTML e para que serve?
HTML (Linguagem de Marcação de HiperTexto) é o bloco de construção mais básico da web. Define o significado e a estrutura do conteúdo da web. Outras tecnologias além do HTML geralmente são usadas para descrever a aparência/apresentação (CSS) ou a funcionalidade/comportamento (JavaScript) de uma página da web.
- [Visual Studio Code v.1.73.1](https://code.visualstudio.com/) - Editor de código aberto desenvolvido pela Microsoft. Nesse caso, ele foi usado em prol do desenvolvimento deste README do projeto.
- [AWS](https://aws.amazon.com/pt/) - Também conhecido como AWS, é uma plataforma de serviços de computação em nuvem, que formam uma plataforma de computação na nuvem oferecida pela Amazon.com. Os serviços são oferecidos em várias áreas geográficas distribuídas pelo mundo. Dentre teus principais serviços, estão: 1º Computação. 2º Armazenamento. 3º Banco de dados. 4º Redes e entrega de conteúdo. 5º Análises. 6º /Machine learning. 7º Segurança, identidade e conformidade. Dentre muito outros.

## Comandos
### Capturação da frase e conversão para a AWS Polly das rotas v1, v2 e v3 usando o arquivo `handler.py`

```python
import json


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

def html_route(event, context):

    with open('templates/index.html', 'r') as f:
        html_content = f.read()
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
        },
        'body': html_content,

    }
```

O código acima é responsável pela geração de voz utilizando a Amazon Polly. A API Gateway desenvolvida possui três versões e cada uma das versões tem seu próprio endpoint para receber requisições.
Ele também tem uma função especifica `html_route` como forma de requisição do HTML para conversão das rotas.
A função v1_description retorna a mensagem "TTS api version 1." em formato JSON.
A função v2_description retorna a mensagem "TTS api version 2." em formato JSON.

### Arquivo responsável por descreve toda a infraestrutura de aplicativos, desde a linguagem de programação até o acesso a recursos.

**Serveless.yml**

```
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
    handler: v1.v1_tts
    events:
      - httpApi:
          path: /v1/tts
          method: post
  v2_tts:
    handler: v2.v2_tts
    events:
      - httpApi:
          path: /v2/tts
          method: post
  v3_tts:
    handler: v3.v3_tts
    events:
      - httpApi:
          path: /v3/tts
          method: post
  html_route:
    handler: handler.html_route
    events:
      - httpApi:
          path: /home
          method: get
```
 **v1.py**

```python
from functions.aux import getAudioData

def v1_tts(event, context):
    try:
        text = event["phrase"]

        dados = getAudioData(text)

        return {
            "status": 200,
            "body": {
                "received_phrase": dados.text,
                "url_to_audio": dados.url,
                "created_audio": dados.date
            }
        }

    except Exception as err:
        return {
            "status": 500,
            "error": {
                "type": type(err).__name__,
                "message": str(err),
            }
        }
```

**v2.py**


**v3.py**
```python
from functions.aux import *

def v3_tts(event, context):
    try:
        # Obtém o texto do corpo da solicitação
        text = event["phrase"]

        dados = getFromTable(text)
        if dados:
            return {
                "status": 200,
                "body": {
                    "received_phrase": text,
                    "url_to_audio": dados.url,
                    "created_audio":dados.date,
                    "unique_id": dados.unique_id
                }
            }

        else:
            # Se o hash não existir, converte o texto em áudio
            text = event["phrase"]

            dados = getAudioData(text)

            if putIntoTable(dados):
                return {
                    "status": 200,
                    "body": {
                        "received_phrase": dados.text,
                        "url_to_audio": dados.url,
                        "created_audio": dados.date,
                        "unique_id": dados.unique_id
                    }
                }

    except Exception as err:
        return {
            "status": 500,
            "error": {
                "type": type(err).__name__,
                "message": str(err),
            }
        }
```

### Atividade das funções que são utilizadas em comum desenvolvidas nas rotas v1, v2 e v3

**aux.py**

```python
import boto3
import hashlib
import os
import json
from datetime import datetime
from time import timezone

class Data:
    """ Esta classe tem por objetivo apenas agrupar os principais
        atributos que serão usados na API """

    def __init__(self, *args, text, url, unique_id):
        self.text = text
        self.unique_id = unique_id
        self.url = url
        timezone = -3 # converte da padrão para a UTC -3
        self.date = str(datetime.now())


def getAudioData(text: str) -> Data:
    """ Esta função tem por objetivo obter a classe Data, e para isto
        instancia o client polly para obter o audio usando a função
        synthesize_speech() """

    polly = boto3.Session(
            region_name='us-east-1').client('polly')

    response = polly.synthesize_speech(
            OutputFormat='mp3',
            Text=text,
            VoiceId="Camila"
        )

    hash_ = hashlib.md5(text.encode('utf-8')).hexdigest()
    nome_arquivo = "audio-" + text + "-" + hash_[:10] + ".mp3"
    url = "https://" \
        + str(os.environ['BUCKET_NAME']) \
        + ".s3.amazonaws.com/" \
        + nome_arquivo 

    s3 = boto3.client('s3')
    s3.put_object(Key=nome_arquivo,
                  Bucket=os.environ['BUCKET_NAME'],
                  Body=response['AudioStream'].read())


    return Data(text = text,
                unique_id=hash_,
                url=url)


def putIntoTable(dados: Data)-> bool:
    """ Esta função tem por objetivo colocar alguns dos dados 
    da classe Data na tabela do DynamoDB """
    try:
        dynamoDB = boto3.resource('dynamodb')

        tabela = dynamoDB.Table("sprint6grupo1")

        tabela.put_item(
            Item={
                "unique_id": dados.unique_id,
                "phrase": dados.text,
                "url": dados.url
            }
        )
        return True
    except:
        return False


def getFromTable(text: str) -> dict:
    """ Esta função tem por objetivo consultar a tabela no DynamoDB para 
        verificar a existẽncia do hash da frase passada como parâmetro,
        e então, caso exista retorna o objeto Data, senão devolve None """
    # Calcula o hash do texto para verificar se já foi convertido antes
    hash_ = hashlib.md5(text.encode('utf-8')).hexdigest()

    dynamoDB = boto3.resource('dynamodb')
    tabela = dynamoDB.Table("sprint6grupo1")

    # Verifica se o hash já existe na tabela DynamoDB
    response = tabela.get_item(
        Key={
            "unique_id": hash_
        }
    )
    response = json.loads(json.dumps(response))
    if len(response.keys()) > 1:
        return Data(text=text,
                    url = response["Item"]["url"],
                    unique_id = response["Item"]["unique_id"])
    else:
        return None
```

### HTML responsável pela requisição das rotas e conversão do texto para audio

**index.html**
```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>API Text To Speech</title>
    <link
      rel="stylesheet"
      href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    />
    <style>
      .btn-pink {
        background-color: #ffc2d9;
        border-color: #ffc2d9;
      }

      .btn-pink:hover {
        background-color: #f4a4c4;
        border-color: #f4a4c4;
      }
    </style>
  </head>

  <body>
    <div
      class="container d-flex align-items-center justify-content-center vh-100"
    >
      <div class="card">
        <div class="card-body d-flex align-items-center flex-column">
          <h5 class="card-title text-center">Digite um texto:</h5>
          <form>
            <div class="form-group">
              <input type="text" class="form-control" id="valorInput" />
            </div>
            <button
              type="button"
              class="btn btn-pink btn-block"
              onclick="enviarValor()"
            >
              Enviar
            </button>
          </form>
          <div id="resultadoDiv" class="mt-3"></div>
        </div>
      </div>
    </div>

    <script>
      function enviarValor() {
        const urlAtual = window.location.href;
        const valor = document.getElementById("valorInput").value;

        const data = {
          phrase: valor,
        };

        const xhr = new XMLHttpRequest();
        xhr.open("POST", urlAtual);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onload = function () {
          const response = JSON.parse(xhr.responseText);
          if (xhr.status === 200) {
            document.getElementById("resultadoDiv").innerText = JSON.stringify(
              response,
              null,
              2
            );
            console.log(xhr.responseText);
          } else {
            document.getElementById("resultadoDiv").innerText = JSON.stringify(
              response,
              null,
              2
            );
            console.error(xhr.responseText);
          }
        };
        xhr.onerror = function () {
          console.error("Erro de rede");
        };
        xhr.send(JSON.stringify(data));
      }
    </script>
  </body>
</html>
```

## Autores

* [@Humberto-Sampaio](https://github.com/Humbert010)
* [@Jeef-Moreira](https://github.com/Jeef-Moreira)
* [@Josiana-Silva](https://github.com/JosianaSilva)
* [@Rosemelry-Mendes](https://github.com/Rosemelry)