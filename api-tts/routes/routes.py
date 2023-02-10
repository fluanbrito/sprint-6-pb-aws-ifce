from flask import Blueprint, request, abort
from error_handlers import register_error_handlers

blueprint = Blueprint("routes", __name__)

@blueprint.route("/", methods=["GET"])
def root():
    return "Route 1: GET /", 200

@blueprint.route("/v1", methods=["GET"])
def v1_get():
    return "Route 2: GET /v1", 200

@blueprint.route("/v2", methods=["GET"])
def v2_get():
    return "Route 3: GET /v2", 200

@blueprint.route("/v1/tts", methods=["POST"])
def v1_tts():
    try:
        if request.headers.get("Content-Type") != "application/json":
            raise Exception("Invalid Content-Type")
        return "Route 4: POST /v1/tts", 200
    except Exception as e:
        return str(e), 500

@blueprint.route("/v2/tts", methods=["POST"])
def v2_tts():
    try:
        if request.headers.get("Content-Type") != "application/json":
            raise Exception("Invalid Content-Type")
        return "Route 5: POST /v2/tts", 200
    except Exception as e:
        return str(e), 500