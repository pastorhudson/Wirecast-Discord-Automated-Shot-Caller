import json


class Camera:
    def __init__(self):
        # self.left = ''
        # self.right = ''
        # self.center = ''
        self.qued = ''
        self.live = ''

    def __repr__(self):
        return self.toJSON()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

    def set_camera(self, camera):
        if self.qued != camera:
            self.qued = camera
        elif self.qued == camera:
            self.live = camera
            self.qued = ''

        return self

    def live_camera(self, camera):
        if camera == 'left':
            self.left = 'live'
        elif self.left != 'qued':
            self.left = ''
        if camera == 'right':
            self.right = 'live'
        elif self.right != 'qued':
            self.right = ''
        if camera == 'center':
            self.center = 'live'
        elif self.center != 'qued':
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