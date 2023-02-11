import json
import boto3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

polly = boto3.client('polly')
s3 = boto3.client('s3')

@app.route('/v1', methods=['GET'])
def v1_form():
    with open('form.html') as file:
        return file.read()

@app.route('/v1/tts', methods=['POST'])
def v1_tts():
    received_phrase = request.form['phrase']
    response = polly.synthesize_speech(
        Text=received_phrase,
        OutputFormat='mp3',
        VoiceId='Joanna'
    )
    audio = response['AudioStream'].read()

    s3.put_object(
        Bucket='api-tts-audio-storage',
        Body=audio,
        Key=f'{received_phrase}.mp3'
    )

    url = f'https://s3.amazonaws.com/api-tts-audio-storage/{received_phrase}.mp3'
    return jsonify({
        'received_phrase': received_phrase,
        'url_to_audio': url,
        'created_audio': 'data não disponível'
    })

def handler(event, context):
    return app(event, context)
