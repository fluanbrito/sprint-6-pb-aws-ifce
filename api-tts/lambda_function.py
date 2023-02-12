import boto3
import os
import uuid

def lambda_handler(event, context):

    recordId = str(uuid.uuid4())
    voice = event["voice"]
    text = event["text"]

    print('Gerando um novo registro DynamoDB, com ID: ' + recordId)
    print('Texto de entrada: ' + text)
    print('Voz selecionada: ' + voice)

    #Criando um novo registro na tabela do DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['BD_TABLE_NAME'])
    table.put_item(
        Item={
            'id' : recordId,
            'text' : text,
            'voice' : voice,
            'status' : 'PROCESSANDO'
        }
    )

    #Enviando notificação sobre novos posts para SNS
    client = boto3.client('sns')
    client.publish(
        TopicArn = os.environ['SNS_TOPIC'],
        Message = recordId
    )

    return recordId
    