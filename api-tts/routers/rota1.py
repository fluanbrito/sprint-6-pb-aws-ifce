import json


def v1_tts(event, context):
    # Carregar o corpo da requisição como um dicionário
    body = json.loads(event.get('body', '{}'))
    
    # Recuperar os dados enviados na requisição
    data = body.get('phrase', [])
    
    # Usar os dados inferidos aqui
    
    # Criar a resposta
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Dados inferidos com sucesso!",
            "data": data
        })
    }
    
    return response