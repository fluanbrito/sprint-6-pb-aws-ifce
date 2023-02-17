from functions.aux import *


def v3_tts(event, context):
    try:
        # Obtém o texto do corpo da solicitação
        text = json.loads(event.get('body', '{}'))
        text = text.get('phrase', [])

        dados = getFromTable(text)
        if dados:
            return {
                "status": 200,
                "body": {
                    "received_phrase": text,
                    "url_to_audio": dados.url,
                    "created_audio": dados.date,
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
