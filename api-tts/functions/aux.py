import boto3
import hashlib
import os
import json
from datetime import datetime
from time import timezone

class Data:
    """ Esta classe tem por objetivo apenas agrupar os principais
        atributos que serão usados na API """

    def __init__(self,*args, text, url, unique_id):
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
    nome_arquivo = "audio-" + hash_ + ".mp3"
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
                date=datetime.now(),
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
