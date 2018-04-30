# coding: utf-8

import GraphCap as gc
import GraphCapCon as gcc


class Template:
    def __init__(self, window, name, imageName, maskName=None):
        self.window = window
        self.name = name
        self.image = gc.Image()
        self.image.read(imageName, gcc.RF_UNCHANGED)
        if self.image.type() != gcc.IT_8UC4:
            raise Exception("图片格式错误：请将图片保存为32位色。\n{0}".format(imageName))
        if maskName is None:
            self.mask = None
        else:
            self.mask = gc.Image()
            self.mask.read(maskName, gcc.RF_UNCHANGED)
            if self.mask.type() != gcc.IT_8UC4:
                raise Exception("掩码格式错误：请将掩码保存为32位色。\n{0}".format(maskName))

    def matchSingleOn(self, image, threshold=0.99):
        if self.mask is None:
            result = image.matchTemplate(self.image, gcc.TM_CCOEFF_NORMED)
        else:
            result = image.matchTemplate(self.image, gcc.TM_CCORR_NORMED, self.mask)
        minMaxLoc = result.minMaxLoc()
        if minMaxLoc.maxVal > threshold:
            print("匹配到[{0}]，相似度是{1}。".format(self.name, minMaxLoc.maxVal))
            return Target(self.window, minMaxLoc.maxLoc, self.image.size())
        else:
            print("匹配不到[{0}]，相似度是{1}。".format(self.name, minMaxLoc.maxVal))
            return None

    def matchMultiOn(self, image, threshold=0.99):
        if self.mask is None:
            result = image.matchTemplate(self.image, gcc.TM_CCOEFF_NORMED)
        else:
            result = image.matchTemplate(self.image, gcc.TM_CCORR_NORMED, self.mask)
        targetList = []
        while True:
            minMaxLoc = result.minMaxLoc()
            if minMaxLoc.maxVal > threshold:
                print("匹配到[{0}]，相似度是{1}。".format(self.name, minMaxLoc.maxVal))
                targetList.append(Target(self.window, minMaxLoc.maxLoc, self.image.size()))
            else:
                print("匹配不到[{0}]，相似度是{1}。".format(self.name, minMaxLoc.maxVal))
                break
            result.eraseMaxLoc(minMaxLoc, self.image.size())
        return targetList


class Target:
    def __init__(self, window, location, size):
        self.window = window
        self.location = location
        self.size = size

    def click(self):
        self.window.click(self.location, self.size())
