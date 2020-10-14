from flask import Flask, jsonify
from flask import request, redirect
app = Flask(__name__)

shot_status = {"live": "", "queued": ""}


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return redirect('/')


@app.route('/')
def hello_world():
    return '<h1>This is a cbc-media tool. Not much to see here.</h1>'


@app.route('/api/shot_status/', methods=['GET', 'POST'])
def shot_api():
    global shot_status
    if request.method == 'POST':
        if request.json != shot_status:
            shot_status = request.json
        return request.json
    elif request.method == 'GET':
        return jsonify(shot_status)
