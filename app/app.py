from flask import Flask
from app.camera import Camera
app = Flask(__name__)

camera = Camera()

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/camera')
def camera_status():
    return camera.toJSON()


@app.route('/left')
def left_cam():
    camera.set_camera('left')
    return camera.toJSON()


@app.route('/right')
def right_cam():
    camera.set_camera('right')
    return camera.toJSON()


@app.route('/center')
def center_cam():
    camera.set_camera('center')
    return camera.toJSON()