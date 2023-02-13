import urllib.parse
import datetime
import hashlib

def getPhrase(event):
    body = event['body']
    parsed_body = urllib.parse.parse_qs(body)
    phrase = parsed_body.get('phrase')[0]

    # retirando caracteres de quebra de linha
    if phrase.find("\r\n"):
        phrase = phrase.replace("\r\n", "")
    
    return phrase

def generateFileName(phrase):
    if len(phrase) > 6:
        return 'audio_' + phrase[:20].replace(" ", "_") + '.mp3'
        
    return 'audio_' + phrase + '.mp3'

def dateFormatting(response):
    date_string = response['ResponseMetadata']['HTTPHeaders']['date']
    date_object = datetime.datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S %Z')

    return date_object.strftime('%d-%m-%Y %H:%M:%S')

def generateUniqueId(phrase):
    return hashlib.sha256(phrase.encode()).hexdigest()[:6]