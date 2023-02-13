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

- [⬇️ Desenvolvimento da API(Functions.py)](#%EF%B8%8F-desenvolvimento-api)

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
- Amazon Web Services(AWS Polly, S3, Dynamo DB, Lambda, Serverless)
- Python
- HTML, CSS

<hr>
<br>

## 😌 Impedimentos Resolvidos

- Interpretação inicial da construção, organização do código como também de sua arquitetura.
- Construção das rotas, como também a sua "successfully executed", cada rota haviam erros que foram resolvidos após estudo e pequisa.
- Dificuldade na utilização dos serviços da AWS, descobrimento de funções e atribuições no código.
- Criação das funções e com quais bibliotecas seria trabalhado, houve momentos que foi debatido a utilização de Flask, por exemplo.

<hr>
<br>

## 📝 Organização do Código

![img](https://i.imgur.com/KuHHUi8.png)

Acima é o demonstrativo de como foi organizado o projeto e subdivido em pastas conforme era a atuação do código.

A organização do código ajudou a evitar erros e bugs, uma vez que as partes do código estão claramente separadas e identificadas. Ela também facilitou a implementação de novas funcionalidades e a resolução de problemas, pois se tornou mais fácil localizar e corrigir o código relevante. 

Em resumo, a organização do código foi fundamental para o sucesso do projeto, pois tornou o processo de desenvolvimento mais eficiente e efetivo.
<hr>
<br>

## 🖥 Captura de frase e converver em Audio MP3 via Polly(Rota 1 , Rota 2, Rota 3)

```bash
import json
from datetime import datetime
from utils import functions

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

```bash
def v1_tts(event, context):
    
    bibliotecas = functions.bibliotecas()
    dados = functions.dados(event, bibliotecas[2])
    functions.gerar_audio(dados[1], dados[4], dados[5], bibliotecas[0], bibliotecas[1])

    return functions.retorno(dados[1], '', dados[4], dados[5])
```

A função v1_tts começa carregando as bibliotecas necessárias para sua execução, fazendo uma chamada para a função "bibliotecas". Em seguida, faz uma chamada para a função "dados", passando como argumentos "event" e "bibliotecas[2]". Essa função retorna dados que são armazenados na variável "dados".

Em resumo, é responsável por gerar áudios a partir de texto, carregar as bibliotecas necessárias, obter os dados de entrada, gerar o áudio e retornar o resultado da operação.

<hr>
<br>

## 📤 Atividade - Parte 2(Hash, AWS Polly, Armazenamento S3, DynamoDB, Chamada API)

```bash
def v2_tts(event, context):
    
    bibliotecas = functions.bibliotecas()
    dados = functions.dados(event, bibliotecas[2])
    functions.gerar_audio(dados[1], dados[4], dados[5], bibliotecas[0], bibliotecas[1])
    functions.audio_dynamo(dados[1], dados[2], dados[3], dados[4], dados[5])

    return functions.retorno(dados[1], dados[3], dados[4], dados[5])
```

A função v2_tts primeiro importa bibliotecas necessárias e obtém dados relevantes a partir do evento passado como argumento. Em seguida, a função gera o áudio TTS e armazena o resultado em um banco de dados. Por fim, a função retorna um resultado com informações sobre a geração do áudio.

<hr>
<br>

## 📤 Atividade - Parte 3(Hash, AWS Polly, Armazenamento S3, DynamoDB)
```bash
def v3_tts(event, context):
    
    bibliotecas = functions.bibliotecas()
    dados = functions.dados(event, bibliotecas[2])
    busca_dynamo = functions.busca_dynamo(dados[2], dados[3])

    if busca_dynamo is None:
        functions.gerar_audio(dados[1], dados[4], dados[5], bibliotecas[0], bibliotecas[1])
        functions.audio_dynamo(dados[1], dados[2], dados[3], dados[4], dados[5])

        return functions.retorno(dados[1], dados[3], dados[4], dados[5])
        
    else:
        return functions.retorno(dados[1], dados[3], dados[4], dados[5])
```
A função v3_tts começa importando as bibliotecas necessárias a partir de outra função functions.bibliotecas(). Em seguida, obtém os dados relevantes para a geração do áudio, utilizando a função functions.dados(event, bibliotecas[2]). Em seguida, a função functions.busca_dynamo(dados[2], dados[3]) é usada para verificar se o áudio já foi gerado previamente e armazenado.

Se o áudio ainda não foi gerado, então a função functions.gerar_audio(dados[1], dados[4], dados[5], bibliotecas[0], bibliotecas[1]) é chamada para gerar o áudio e a função functions.audio_dynamo(dados[1], dados[2], dados[3], dados[4], dados[5]) é chamada para armazená-lo. Finalmente, a função functions.retorno(dados[1], dados[3], dados[4], dados[5]) é chamada para retornar os dados relevantes para a geração do áudio.

Se o áudio já foi gerado e armazenado, então apenas a função functions.retorno(dados[1], dados[3], dados[4], dados[5]) é chamada para retornar os dados relevantes para a geração do áudio, sem a necessidade de gerar o áudio novamente.

<hr>
<br>

## ⬇️ Desenvolvimento da API(Functions.py)
```bash
import boto3
import json
import inspect
from datetime import datetime

def dados(event, db):
    payload = json.loads(event["body"])
    phrase = payload["phrase"]

    hash_frase = str(hash(phrase))[1:len(phrase)]
    filename = f"{hash_frase}.mp3"
    bucket = "bucket-sprint6"
    table = db.Table("audio-data-sprint6")
    
    return payload, phrase, table, hash_frase, filename, bucket

def bibliotecas():

    s3 = boto3.client('s3')
    polly = boto3.client('polly', region_name='us-east-1')
    db = boto3.resource('dynamodb')

    return s3, polly, db

def gerar_audio(phrase, filename, bucket, s3, polly):

    response = polly.synthesize_speech(
        OutputFormat='mp3',
        Text=phrase,
        VoiceId='Camila'
    )
    audio = response['AudioStream'].read()

    s3.put_object(
        Bucket=bucket,
        Key=filename,
        Body=audio,
    )

def audio_dynamo(phrase, table, hash_frase, filename, bucket):

    table.put_item(
        Item={
        'hash': hash_frase,
        'frase': phrase,
        'url':f"https://{bucket}.s3.amazonaws.com/{filename}"
        }
    )

def retorno(phrase, hash_frase, filename, bucket):

    stack = inspect.stack()
    caller = stack[1]
    
    if (caller.function == 'v1_tts'):
        return {
            "received_phrase": phrase,
            "url_to_audio": f"https://{bucket}.s3.amazonaws.com/{filename}",
            "created_audio": str(datetime.now())
        }

    else:
        return {
            "received_phrase": phrase,
            "url_to_audio": f"https://{bucket}.s3.amazonaws.com/{filename}",
            "created_audio": str(datetime.now()),
            "unique_id": hash_frase
        }

def busca_dynamo(table, hash_frase):

    response = table.get_item(Key={'hash': hash_frase})
    item = response.get("Item")

    return item
```


Função em Python que se conecta ao AWS (Amazon Web Services), utilizando as bibliotecas Boto3. Ela realiza as seguintes tarefas:

- Lê o evento enviado por uma requisição e extrai a frase
- Gera um hash aleatório para a frase e monta o nome do arquivo de áudio MP3
- Inicializa as bibliotecas de S3 (Armazenamento na Nuvem), Polly (Text-to-Speech) e DynamoDB (Banco de Dados NoSQL)
- Gera o áudio MP3 baseado na frase usando a voz "Camila" da biblioteca Polly
- Armazena o áudio gerado no S3
- Insere na tabela do DynamoDB a frase, URL do áudio e hash da frase
- Retorna a frase, URL do áudio, data de criação e (opcionalmente) a hash da frase em um objeto JSON
- Busca na tabela do DynamoDB por uma hash idêntica à gerada pela frase. Se encontrada, retorna o item já existente na tabela.
<hr>
<br>

## 📤 Deploy


<br>

<br>
<hr>

## ♾️ Equipe
- [Davi Santos](https://github.com/davi222-santos)
- [Edivalço Araújo](https://github.com/EdivalcoAraujo)
- [Luan Ferreira](https://github.com/fluanbrito)
- [Nicolas](https://github.com/Niccofs)


<br>

<hr>

## 📌 Considerações finais

<br>

Em resumo, o projeto envolvendo o uso da plataforma AWS com Amazon Polly, Amazon S3, Dynamo DB foi muito proveitoso. 

Com uso de Amazon Polly é possível gerar fala sintetizada com qualidade humana, enquanto Amazon S3 fornece armazenamento de arquivos para armazenar as respostas geradas. DynamoDB, por sua vez, é uma base de dados NoSQL de alta disponibilidade que pode ser usada para armazenar informações sobre as respostas geradas, incluindo data e hora de geração, parâmetros de fala e outros dados relevantes.

Além disso, o uso destes três serviços da Amazon juntos teve potencial de proporcionar escalabilidade, segurança e facilidade de gerenciamento para o projeto.

Em resumo, a combinação de Amazon Polly, Amazon S3 e DynamoDB é uma solução poderosa e flexível para aplicações de inteligência artificial de fala que permite aos usuários transformar texto em fala natural de forma rápida e fácil, garantindo a escalabilidade, segurança e facilidade de gerenciamento do projeto.
