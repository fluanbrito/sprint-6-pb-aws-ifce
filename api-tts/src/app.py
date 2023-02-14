# Importando bibliotecas
from flask import Flask, request, render_template
import boto3

#
app = Flask(__name__)

# Criando rota e conectanto ao serviço aws polly
@app.route('/')
def index():
    return render_template("index.html")
   



app.run(debug=True)
