from functions.aux import getAudioData, putIntoTable

def v2_tts(event, context):
    try:

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
