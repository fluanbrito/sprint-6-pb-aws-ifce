from flask import Flask, render_template, flash, redirect, request, jsonify
import os
from handler import *
from functions import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/v1')
def v1_get():
    return v1_description('', '')

@app.route('/v2')
def v2_get():
    return v2_description('', '')

@app.route('/v1/tts', methods=['POST'])
def v1_post():
    frase = {
        "phrase": request.form.get("textov1")
    }
    return response(json.dumps(frase))
    
@app.route('/v2/tts', methods=['POST'])
def v2_post():
    frase = {
        "phrase": request.form.get("textov2")
    }
    return response(json.dumps(frase))
    

@app.route('/v3/tts', methods=['POST'])
def v3_post():
    frase = {
        "phrase": request.form.get("textov3")
    }
    return response(json.dumps(frase))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True)