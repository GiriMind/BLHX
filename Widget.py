# coding: utf-8

import GraphCap as gc
import Image


class Template:
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

    def matchSingleOn(self, image, similarity=0.99):
        if self.mask is None:
            result = image.matchTemplate(self.image, Image.TM_CCOEFF_NORMED)
        else:
            result = image.matchTemplate(self.image, Image.TM_CCORR_NORMED, self.mask)
        minMaxLoc = result.minMaxLoc()
        if minMaxLoc.maxVal > similarity:
            print("匹配到{0}，相似度是{1}。".format(self.name, minMaxLoc.maxVal))
            return Target(self, minMaxLoc.maxLoc)
        else:
            print("匹配不到{0}，相似度是{1}。".format(self.name, minMaxLoc.maxVal))
            return None

    def matchMultiOn(self, image, similarity=0.99):
        if self.mask is None:
            result = image.matchTemplate(self.image, Image.TM_CCOEFF_NORMED)
        else:
            result = image.matchTemplate(self.image, Image.TM_CCORR_NORMED, self.mask)
        targetList = []
        while True:
            minMaxLoc = result.minMaxLoc()
            if minMaxLoc.maxVal > similarity:
                print("匹配到{0}，相似度是{1}。".format(self.name, minMaxLoc.maxVal))
                targetList.append(Target(self, minMaxLoc.maxLoc))
            else:
                print("匹配不到{0}，相似度是{1}。".format(self.name, minMaxLoc.maxVal))
                break
            result.eraseMaxLoc(self.image, minMaxLoc)
        return targetList


class Target:
    def __init__(self, template, location):
        self.template = template
        self.location = location

    def click(self):
        self.template.window.click(self.location, self.template.image.size())
