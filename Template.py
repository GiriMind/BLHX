# coding: utf-8

import GraphCap as gc


class Template:
    def __init__(self, game, name, imageFile):
        self.game = game
        self.name = name
        self.image = gc.Image(imageFile)
        if self.image.isEmpty():
            raise Exception("载入图片失败：{0}".format(imageFile))

    def matchOn(self, scene):
        ret, pos = scene.match(self.image)
        if ret:
            return Target(self.game, pos)
        else:
            return None


class Target:
    def __init__(self, game, pos, size=None):
        self.game = game
        self.pos = pos
        self.size = size

    def click(self):
        self.game.click(self.pos, self.size)
