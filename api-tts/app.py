from flask import Flask
from routes.routes import blueprint
from errors.error_handlers import register_error_handlers

app = Flask(__name__)
app.register_blueprint(blueprint)
register_error_handlers(app)

if __name__ == "__main__":
    app.run()