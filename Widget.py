# coding: utf-8

import GraphCap as gc
import Image


class Widget:
    def __init__(self, window, imageName, maskName=None):
        self.window = window
        self.image = gc.Image(imageName, Image.IMREAD_UNCHANGED)
        if self.image.type() != Image.CV_8UC4:
            raise Exception("图片格式错误：请将图片保存为32位色。\n{0}".format(imageName))
        self.mask = None
        if maskName is not None:
            self.mask = gc.Image(maskName, Image.IMREAD_UNCHANGED)
            #if self.mask.type() != Image.CV_8UC4:
            #    raise Exception("掩码格式错误：请将掩码保存为32位色。\n{0}".format(maskName))
        self.similarity = None
        self.location = None

    def clear(self):
        self.similarity = None
        self.location = None

    def matchOn(self, windowImage, threshold=0.95):
        result = windowImage.matchTemplate(self.image, Image.TM_CCOEFF_NORMED)
        minMaxLoc = result.minMaxLoc()
        if minMaxLoc.maxVal > threshold:
            self.similarity = minMaxLoc.maxVal
            self.location = minMaxLoc.maxLoc

    def matchMaskOn(self, windowImage, threshold=0.95):
        if self.mask is None:
            raise Exception("掩码为空。")
        result = windowImage.matchTemplate(self.image, Image.TM_CCORR_NORMED, self.mask)
        minMaxLoc = result.minMaxLoc()
        if minMaxLoc.maxVal > threshold:
            self.similarity = minMaxLoc.maxVal
            self.location = minMaxLoc.maxLoc

    def isMatched(self):
        return self.similarity is not None  # and self.location is not None

    def click(self):
        pass


class Button(Widget):
    def __init__(self, window, fileName, maskName=None):
        super().__init__(window, fileName, maskName)

    def click(self):
        self.window.click(self.location, self.image.size())
