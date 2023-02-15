![Logo_CompassoUOL_Positivo](https://user-images.githubusercontent.com/94761781/212589731-3d9e9380-e9ea-4ea2-9f52-fc6595f8d3f0.png)
# 📑 Avaliação Sprint 6 - Programa de Bolsas Compass.uol / AWS e IFCE

<hr>
<p align="center">
  
<img src="https://img.shields.io/static/v1?label=STATUS&message=construindo&color=RED&style=for-the-badge" />
</p>


## 📌 Tópicos 

- [📝 Descrição do projeto](#-descrição-do-projeto)

- [🧑‍💻👩‍💻 Ferramentas e Tecnologias](#-ferramentas-e-tecnologias)

- [🖥️ Código](#%EF%B8%8F-código)

- [📤 Deploy - serviço Elastic Beanstalck](#-deploy)

- [♾️ Equipe](#%EF%B8%8F-equipe)

- [📌 Dificuldades](#-dificuldades)

<br>

## 📝 Descrição do projeto 
Criação de uma página html que captura uma frase qualquer inserida pelo usuário e transformará essa frase em um áudio em mp3 via polly.

<p align="justify">
<hr>

## 🧑‍💻👩‍💻 Ferramentas e Tecnologias 

<br>
<a href="https://aws.amazon.com/pt/polly/" target="_blank"> 
<img src="https://imgs.search.brave.com/Q8TsMuqn0Ggx-ePHHX5cbZ6wcQkAb6tpaR6EZoOMe8o/rs:fit:200:200:1/g:ce/aHR0cHM6Ly9rYWxs/aW9wZS1wcm9qZWN0/LmdpdGh1Yi5pby9p/bWFnZXMvcG9sbHlf/dHRzLnBuZw" alt="androidStudio" width="40" title="Polly" height="40"/> </a> <a href="https://aws.amazon.com/pt/api-gateway/ target="_blank"> <img src="https://imgs.search.brave.com/-mAOrY3RTIz9jBKsHpv8wvpy2cOF7CV6YtfUxnUN9Bo/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly9jZG4u/ZnJlZWJpZXN1cHBs/eS5jb20vbG9nb3Mv/bGFyZ2UvMngvYXdz/LWFwaS1nYXRld2F5/LWxvZ28tcG5nLXRy/YW5zcGFyZW50LnBu/Zw" title="API GATEWAY" alt="java" width="40" height="40"/> </a> 
<a href="https://aws.amazon.com/pt/lambda/" target="_blank"> <img src="https://imgs.search.brave.com/u5UqI1qsoHqoY1QGcfWS7WU9jmaGEgxhwqlYZbJ9Eoo/rs:fit:725:750:1/g:ce/aHR0cHM6Ly9pMS53/cC5jb20vYmxvZy5j/b250YWN0c3Vubnku/Y29tL3dwLWNvbnRl/bnQvdXBsb2Fkcy8y/MDE5LzExL2F3c19s/YW1iZGFfbG9nby5w/bmc_c3NsPTE" alt="firebase" width="40" height="40" title="AWS Lambda"/> </a><a href="https://aws.amazon.com/pt/dynamodb/" target="_blank"> <img src="https://imgs.search.brave.com/84pQUKFRPnJD0Fcoc-rwRZMAGrjIWdFHC9C1lX02LFc/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly9jZG4u/ZnJlZWJpZXN1cHBs/eS5jb20vbG9nb3Mv/bGFyZ2UvMngvYXdz/LWR5bmFtb2RiLWxv/Z28tcG5nLXRyYW5z/cGFyZW50LnBuZw" alt="firebase" width="40" height="40" title="AWS DYnanmo DB"/> </a> <a href="https://aws.amazon.com/pt/s3/" target="_blank"> <img src="https://imgs.search.brave.com/uKMT5jd0yYlnw-jAFoeBgq4XT-Shdlgto1NoX2NHSUs/rs:fit:1057:1200:1/g:ce/aHR0cHM6Ly9icmFu/ZHNsb2dvcy5jb20v/d3AtY29udGVudC91/cGxvYWRzL2ltYWdl/cy9sYXJnZS9hd3Mt/czMtbG9nby5wbmc" alt="firebase" width="40" height="40" title="AWS S3"/> </a><a href="https://www.serverless.com/" target="_blank"> <img src="https://imgs.search.brave.com/D8PnoWnRnNIFBk7YnDttFF4TrmsEhr3LWU-ernO7WUU/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly9zMy11/cy13ZXN0LTIuYW1h/em9uYXdzLmNvbS9h/c3NldHMuc2l0ZS5z/ZXJ2ZXJsZXNzLmNv/bS9sb2dvcy9zZXJ2/ZXJsZXNzLXNxdWFy/ZS1pY29uLXRleHQu/cG5n" alt="firebase" width="40" height="40" title="Serveless"/> </a>

<br>

<hr>

## 🖥️ Código - Execução (Código Fonte)

**Configurações Iniciais**:

Passo a passo para iniciar o projeto:

1. Instale o framework serverless em seu computador. Mais informações [aqui](https://www.serverless.com/framework/docs/getting-started)
```json
npm install -g serverless
```

2. Gere suas credenciais (AWS Acess Key e AWS Secret) na console AWS pelo IAM. Mais informações [aqui](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/)

3. Em seguida insira as credenciais e execute o comando conforme exemplo:

```json
serverless config credentials --provider aws --key XXXXXXX --secret XXXXXXX
  ```

Também é possivel configurar via [aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) executando o comando:

```json
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-east-1
Default output format [None]: ENTER
  ```

## Atividade -> Parte 1 

### Página HTML

Conforme especificações da avaliação, foi criada uma página HTML para receber do usuário uma frase qualquer que passará pela rotas da API de forma a ser convertida em áudio mp3 utilizando o serviço Amazon Polly e o resultado será retornado ao usuário. 
Na página apresentada o usuário fornece a frase e pode verificar o resultado no botão converter ou baixar o link de acesso para o arquivo em mp3 que está armazenado no bucket do serviço S3.

![mp3](https://user-images.githubusercontent.com/103959633/219032662-3485251c-af62-4ede-8133-6c925befbea4.jpg)

**Código HTML**
```
<!DOCTYPE html>
<html>
<head>
    <title>Conversor de Texto em Áudio</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
<body>
    <div class="container">
        <div class="row" style="margin-top: 40px;">
            <div class="col-md-3"></div>
            <div class="col-md-6 bg-info text-white text-center" style="padding: 20px;">
                <h2 class="text-center">Conversor de Texto em Áudio</h2>
                <hr>
                <form>
                    <div class="form-group text-left">
                        <label for="texto">Texto a Converter:</label>
                        <textarea class="form-control" id="texto" name="texto" rows="4"></textarea>
                    </div>
                    <div class="form-group text-right">
                        <button type="submit" class="btn btn-warning">Converter</button>
                    </div>
                    <hr>
                    <div class=" form-group">
                        <label for="">Link</label>
                            <a class="btn btn-danger" href="https://s3.amazonaws.com/audios-sprint-6-grupo-4/convertaessetextoparaaudio.mp3" >Baixe o Audio</a>
                    </div>
                </form>
                <hr>
                <p>
                    Compass Uol - PB IFCE - Grupo 4
                </p>
            </div>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>
</body>
</html>
```
### API Externa

Para a conexão entre o arquivo HTML e os serviços que serão acessados através das rotas foi desenvolvida a API externa que recebe a frase que será converdita em audio e transmite o resultado da rota para o usuário por meio do retorno na página web.
  
```
# Importando bibliotecas
from flask import Flask, request, render_template
import boto3

app = Flask(__name__)

# Criando rota e conectanto ao serviço aws polly
@app.route('/')
def index():
    return render_template("index.html")
   
app.run(debug=True)  
```

### Rota V1 -> Post /v1/tts

A primeria rota utiliza o método POST para enviar a frase recebida através da API para o serviço Amazon Polly. Conforme as configurações no arquivo Serverless.yml que será exposto ao final da explanação dos códigos das rotas, os dados recebidos na rota v1/tts serão encaminhados para o serviço Polly e convertidos em um arquivo mp3, o qual será armazenado em um bucket do serviço Amazon S3. 
O resultado que será retornado ao usuário será o endereço para o acesso ao áudio gerado que está armazenado no bucket.
  
```
import boto3 
import json
import datetime
import unicodedata

#Acessando os serviços Polly e S3
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
        
        #salvando arquivo no bucket
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
  
```

Arquitetura rota /v1/tts:

![post-v1-tts](./assets/post-v1-tts.png)


## Atividade -> Parte 2 
### Rota V2 -> Post /v2/tts

Para o desenvolvimento da rota /v2/tts, a função que recebe a informação do usuário por meio da rota da API, gera um id único para identificação da frase, esse id funcionará como atributo principal para o armazenamento da referência do arquivo em áudio fornecido pelo serviço Polly no banco de dados NoSQL DynamoDB. Semelhante a rota anterior o arquivo fica armazenado do bucket após conversão da frase e o método principal da rota é o post.

```
import boto3
import json
import hashlib

#acesso aos serviços das aws
polly_client = boto3.client('polly')
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def create(event, context):
    try:
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
  
```
  
Arquitetura rota /v2/tts:

![post-v2-tts](./assets/post-v2-tts.png)


## Atividade -> Parte 3 
### Rota V3 -> Post /v3/tts

A rota /v3/tts segue a mesma lógica de geração do id único para armazenamento da referência no DynamoDB e do arquivo no bucket do S3. Porém, nesta rota a função irá verificar se a frase informada já foi gerada anteriormente, e caso seja positivo ele faz o retorno do endereço para acesso ao arquivo. Se o id não for localizado, a rota segue o processo de geração do id, conversão em áudio e armazenamento, conforme apresentado na rota /v2/tts.

```
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
  
```  

Arquitetura rota /v3/tts:

![post-v3-tts](./assets/post-v3-tts.png)

***

## 📤 Deploy

<br>
Para realização do deploy, realizamos as configurações no arquivo serverless.yml, conforme especificado no código. 

```
service: api-tts
frameworkVersion: '3'

provider:
  name: aws
  runtime: python3.9
  iam:
    role:
      statements:
        - Effect: Allow
          Action: dynamodb:PutItem
          Resource: "arn:aws:dynamodb:*:*:table/TTS_References"
        - Effect: Allow
          Action: dynamodb:Scan
          Resource: "arn:aws:dynamodb:*:*:table/TTS_References"

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
  rota-v1_tts:
    handler: src/rotaV1.tts
    events:
      - http:
          path: /v1/tts
          method: post
          cors: true       
  rota-v2_tts:
    handler: src/rotaV2.create
    events:
      - http:
          path: /v2/tts
          method: post
          cors: true
  rota-v3_tts:
    handler: src/rota.list
    events:
      - http:
          path: /v3/tts
          method: post
          cors: true

resources:
  Resources:
    ttsDynamoDbTable:
      Type: AWS::DynamoDB::Table
      Properties:
        TableName: TTS_References
        AttributeDefinitions:
          - AttributeName: id
            AttributeType: S
        KeySchema:
          - AttributeName: id
            KeyType: HASH
        ProvisionedThroughput:
          ReadCapacityUnits: 1
          WriteCapacityUnits: 1
    ttsIamRole:
      Type: "AWS::IAM::Role"
      Properties:
        AssumeRolePolicyDocument:
          Version: "2012-10-17"
          Statement:
            - Effect: "Allow"
              Principal:
                Service:
                  - "lambda.amazonaws.com"
              Action:
                - "sts:AssumeRole"
        Policies:
          - PolicyName: "ttsDynamoDbAccess"
            PolicyDocument:
              Version: "2012-10-17"
              Statement:
                - Effect: "Allow"
                  Action:
                    - "dynamodb:PutItem"
                    - "dynamodb:Scan"
                    - "dynamodb: Query"
                  Resource: !GetAtt [ttsDynamoDbTable, Arn] 
```
  
Via cli, na pasta `api-tts` acionamos o comando a seguir:
  
```
$ serverless deploy
```

### Observações retorno esperado

![hj](https://user-images.githubusercontent.com/103959633/219063523-f5c21650-8763-44a8-be15-9dbc2766211e.jpg)

Após a execução do comando as configurações e ferramentas nos serviços da AWS serão criados e especificados para que assim, as rotas possam funcionar conforme projetadas. 

<hr>

## ♾️ Equipe
<br>

- [Mylena Soares](https://github.com/mylensoares)
- [Samara Alcantara](https://github.com/SamaraAlcantara)
- [Julio Cesar](https://github.com/JC-Rodrigues)
- [Jhonatan Gonçalves](https://github.com/jhonatangoncalvespereira)

<br>
<hr>

## 📌 Dificuldades
<br>
- Liberação das permissões de acesso as aplicações da AWS, particurlarmente no serviço Polly.
- 


***
Avaliação da sexta sprint do programa de bolsas Compass.uol para formação em machine learning para AWS.

