import json


class Camera:
    def __init__(self):
        # self.left = ''
        # self.right = ''
        # self.center = ''
        self.queued = ''
        self.live = ''

    def __repr__(self):
        return self.toJSON()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

    def set_camera(self, camera):
        if self.queued != camera:
            self.queued = camera
        elif self.queued == camera:
            self.live = camera
            self.queued = ''

        return self

    def live_camera(self, camera):
        if camera == 'left':
            self.left = 'live'
        elif self.left != 'queued':
            self.left = ''
        if camera == 'right':
            self.right = 'live'
        elif self.right != 'queued':
            self.right = ''
        if camera == 'center':
            self.center = 'live'
        elif self.center != 'queued':
            self.center = ''

        return


if __name__ == '__main__':
    cam = Camera()
    print(cam.set_camera('left'))
    print(cam.set_camera('left'))
    print(cam.set_camera('right'))
    print(cam.set_camera('right'))
    print(cam.set_camera('center'))
    print(cam.set_camera('left'))
    print(cam.set_camera('left'))