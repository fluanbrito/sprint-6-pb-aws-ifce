from flask import jsonify

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        return "404: Not Found", 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return "500: Internal Server Error", 500