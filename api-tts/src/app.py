from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/data')
def api_data():
    # aqui você pode retornar os dados da sua API em formato JSON
    return {'data': 'dados da sua API'}


if __name__ == '__main__':
    app.run()
