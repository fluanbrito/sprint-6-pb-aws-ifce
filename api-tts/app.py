from flask import Flask, render_template, flash, redirect, request, jsonify
import os
from handler import *

app = Flask(__name__)

@app.route('/')
def index():
    return health('','')

@app.route('/v1')
def v1_get():
    return v1_description('', '')

@app.route('/v2')
def v2_get():
    return v2_description('', '')

@app.route('/v1/tts', methods=['GET', 'POST'])
def v1_post():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        frase = {
            "phrase": request.form.get("textov1")
        }
        return v1_tts(frase, '')

@app.route('/v2/tts', methods=['GET','POST'])
def v2_post():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        frase = {
            "phrase": request.form.get("textov2")
        }
        return v2_tts(frase, '')


@app.route('/v3/tts', methods=['GET','POST'])
def v3_post():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        frase = {
            "phrase": request.form.get("textov3")
        }
        return v2_tts(frase, '')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True)