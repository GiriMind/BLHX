# coding: utf-8


class Point:
    def __init__(self):
        self.x = 0
        self.y = 0


class Size:
    def __init__(self):
        self.width = 0
        self.height = 0


class Rect:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0


class Image:
    def toNdarray(self):
        pass


class Direct3D:
    pass


class DesktopCapturer:
    def __init__(self, d3d):
        pass

    def capture(self, image, rect, timeout=17):
        pass
