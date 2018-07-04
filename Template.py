# coding: utf-8

import GraphCap as gc
import GraphCapCon as gcc


class Template:
    def __init__(self, game, name, templName, maskName=None):
        self.game = game
        self.name = name
        self.templImage = gc.Image()
        self.templImage.read(templName, gcc.RF_UNCHANGED)
        if self.templImage.getType() != gcc.IT_8UC4:
            raise Exception("模板图片格式错误，请保存为32位色。\n{0}".format(templName))
        if maskName is None:
            self.maskImage = None
        else:
            self.maskImage = gc.Image()
            self.maskImage.read(maskName, gcc.RF_UNCHANGED)
            if self.maskImage.getType() != gcc.IT_8UC4:
                raise Exception("掩码图片格式错误，请保存为32位色。\n{0}".format(maskName))

    def getSize(self):
        return self.templImage.getSize()

    def matchOn(self, image):
        if self.maskImage is None:
            result = image.matchTemplate(self.templImage, gcc.MTM_CCOEFF_NORMED)
        else:
            result = image.matchTemplate(self.templImage, gcc.MTM_CCORR_NORMED, self.maskImage)
        return Target(self.game, self, result)


class Target:
    def __init__(self, game, template, result):
        self.game = game
        self.template = template
        self.result = result
        minMaxLoc = result.minMaxLoc()
        self.location = minMaxLoc.maxLoc
        self.similarity = minMaxLoc.maxVal
        print("[{0}]的相似度是{1}。".format(self.template.name, self.similarity))

    def getSize(self):
        return self.template.getSize()

    def next(self):
        try:
            self.result.floodFill(self.location, gc.Scalar(0.0))
        except Exception as e:
            print(e)
            print("location:{0},{1}".format(self.location.x, self.location.y))
        return Target(self.game, self.template, self.result)

    def click(self):
        self.game.click(self.location, self.template.getSize())


class SpecifiedTarget:
    def __init__(self, game, location, size):
        self.game = game
        self.location = location
        self.size = size

    def click(self):
        self.game.click(self.location, self.size)
