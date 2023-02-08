import json

def response(frase):
    texto = json.loads(frase)

    body = {
        "received_phrase": texto["phrase"],
        "url_to_audio": "https://meu-buckect/audio-xyz.mp3",
        "created_audio": "02-02-2023 17:00:00"
    }

    response = {"statusCode": 200, "body": body}

    return response  