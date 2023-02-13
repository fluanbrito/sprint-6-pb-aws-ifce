# Importando bibliotecas
from flask import Flask, request, render_template
import boto3

#
app = Flask(__name__)

# Criando rota e conectanto ao serviço aws polly
@app.route('/v1/tts', methods=['POST'])
def process():
    text = request.form['text']
    client = boto3.client('polly')
    response = client.synthesize_speech(
        OutputFormat='mp3',
        Text=text,
        VoiceId='Joana'
    )
    # exibindo o audio para o user
    file = open('speech.mp3', 'wb')
    file.write(response['AudioStream'].read())
    file.close()
    return render_template('speech.html')


if __name__ == '__main__':
    app.run()
