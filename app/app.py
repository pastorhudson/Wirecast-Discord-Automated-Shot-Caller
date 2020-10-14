from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

shot_status = {"live": "", "queued": ""}


@app.route('/')
def hello_world():
    return 'This is a cbc-media tool. Not much to see here.'


@app.route('/api/shot_status/', methods=['GET', 'POST'])
def shot_api():
    global shot_status
    if request.method == 'POST':
        if request.json != shot_status:
            shot_status = request.json
        return request.json
    elif request.method == 'GET':
        return jsonify(shot_status)
