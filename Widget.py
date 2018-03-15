# coding: utf-8

import time

import GraphCap as gc
import Image


class Widget:
    def __init__(self, window, name, imageFile, maskFile=None):
        self.window = window
        self.name = name
        self.image = gc.Image(imageFile, Image.IMREAD_UNCHANGED)
        if self.image.type() != Image.CV_8UC4:
            raise Exception("图片格式错误：请将图片保存为32位色。\n{0}".format(imageFile))
        if maskFile is None:
            self.mask = None
        else:
            self.mask = gc.Image(maskFile, Image.IMREAD_UNCHANGED)
            if self.mask.type() != Image.CV_8UC4:
                raise Exception("掩码格式错误：请将掩码保存为32位色。\n{0}".format(maskFile))
        self.location = None

    def match(self, similarity=0.95, timeout=15.0):
        print("正在匹配{0}……".format(self.name))
        self.location = None
        beginTime = time.time()
        while time.time() - beginTime < timeout:
            image = self.window.capture()
            if image is None:
                time.sleep(0.5)
                continue
            if self.mask is None:
                result = image.matchTemplate(self.image, Image.TM_CCORR_NORMED)  # TM_CCOEFF_NORMED
            else:
                result = image.matchTemplate(self.image, Image.TM_CCORR_NORMED, self.mask)
            minMaxLoc = result.minMaxLoc()
            if minMaxLoc.maxVal > similarity:
                self.location = minMaxLoc.maxLoc
                print("匹配到{0}，相似度是{1}。".format(self.name, minMaxLoc.maxVal))
                return True
        print("匹配{0}失败。".format(self.name))
        return False


class Button(Widget):
    def __init__(self, window, name, fileName, maskName=None):
        super().__init__(window, name, fileName, maskName)

    def click(self):
        self.window.click(self.location, self.image.size())
