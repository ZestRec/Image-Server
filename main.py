from flask import Flask, request, jsonify, send_file, redirect, make_response, url_for, render_template, Response, abort, session
from flask_cors import CORS
import json
import requests
import os
import uuid

name = f"{__name__}.py"

app = Flask(__name__)
app.config["SECRET_KEY"] = "PLS DO NOT KEEP THIS"
CORS(app)

dbPath = ""#* Example "C:\\ZestRec\\db\\""
imgPath = ""#* Example "C:\\ZestRec\\img\\""
recRoomImgUrl = "https://img.rec.net/"


@app.errorhandler(404)
def q405(e):
    data = ""
    return data, 404

@app.errorhandler(405)
def q405(e):
    data = ""
    return data, 405

@app.errorhandler(401)
def q401(e):
    data = ""
    return data, 401

@app.errorhandler(403)
def q403(e):
    data = ""
    return data, 403

@app.errorhandler(500)
def q405(e):
    data = {"Message":"An error has occurred."}
    return jsonify(data), 500

@app.route("/", methods=["GET"])
def index():
    return abort(404)

@app.route("/<path:img>", methods=["GET"])
def img(img):
    if os.path.exists(f"{imgPath}{img}"):
        try:
            return send_file(f"{imgPath}{img}")
        except:
            return abort(500)
    else:
        return abort(404)
    
@app.route("/health", methods=["GET"])
def health():
    return jsonify("Healthy")

def run():
    Port = 8080
    Ip = "0.0.0.0"
    app.run(str(Ip), int(Port))
    #ssl_context='adhoc'

run()