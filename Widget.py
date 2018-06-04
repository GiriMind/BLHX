# coding: utf-8

import GraphCap as gc
import GraphCapCon as gcc


class Button:
    def __init__(self, window, name, templName):
        self.window = window
        self.name = name
        self.templ = gc.Image()
        self.templ.read(templName, gcc.RF_UNCHANGED)
        if self.templ.getType() != gcc.IT_8UC4:
            raise Exception("图片格式错误：请将图片保存为32位色。\n{0}".format(templName))

    def match(self, image, threshold=0.98):
        result = image.matchTemplate(self.templ, gcc.MTM_CCOEFF_NORMED)
        minMaxLoc = result.minMaxLoc()
        if minMaxLoc.maxVal > threshold:
            print("匹配[{0}]成功，相似度是{1}。".format(self.name, minMaxLoc.maxVal))
            return Target(self.window, minMaxLoc.maxLoc, self.templ.getSize())
        else:
            print("匹配[{0}]失败，相似度是{1}。".format(self.name, minMaxLoc.maxVal))
            return None


class Enemy:
    def __init__(self, window, name, templName, maskName):
        self.window = window
        self.name = name
        self.templ = gc.Image()
        self.templ.read(templName, gcc.RF_UNCHANGED)
        if self.templ.getType() != gcc.IT_8UC4:
            raise Exception("图片格式错误：请将图片保存为32位色。\n{0}".format(templName))
        self.mask = gc.Image()
        self.mask.read(maskName, gcc.RF_UNCHANGED)
        if self.mask.getType() != gcc.IT_8UC4:
            raise Exception("图片格式错误：请将图片保存为32位色。\n{0}".format(maskName))

    def match(self, image, threshold=0.98):
        result = image.matchTemplate(self.templ, gcc.MTM_CCORR_NORMED, self.mask)
        targetList = []
        while True:
            minMaxLoc = result.minMaxLoc()
            if minMaxLoc.maxVal > threshold:
                # print("匹配[{0}]成功，相似度是{1}。".format(self.name, minMaxLoc.maxVal))
                targetList.append(Target(self.window, minMaxLoc.maxLoc, self.templ.getSize()))
            else:
                # print("匹配[{0}]失败，相似度是{1}。".format(self.name, minMaxLoc.maxVal))
                break
            result.floodFill(minMaxLoc.maxLoc, gc.Scalar(0.0))
        return targetList


class Target:
    def __init__(self, window, location, size):
        self.window = window
        self.location = location
        self.size = size

    def click(self):
        self.window.click(self.location, self.size)
