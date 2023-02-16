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
