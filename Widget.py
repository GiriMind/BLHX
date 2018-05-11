# coding: utf-8

import GraphCap as gc
import GraphCapCon as gcc


class Template:
    def __init__(self, window, name, templName, maskName=None):
        self.window = window
        self.name = name
        self.templ = gc.Image()
        self.templ.read(templName, gcc.RF_UNCHANGED)
        if self.templ.getType() != gcc.IT_8UC4:
            raise Exception("图片格式错误：请将图片保存为32位色。\n{0}".format(templName))
        if maskName is None:
            self.mask = None
        else:
            self.mask = gc.Image()
            self.mask.read(maskName, gcc.RF_UNCHANGED)
            if self.mask.getType() != gcc.IT_8UC4:
                raise Exception("掩码格式错误：请将掩码保存为32位色。\n{0}".format(maskName))

    def canny(self, threshold1=100.0, threshold2=200.0):
        self.templ = self.templ.canny(threshold1, threshold2)

    def matchMultiOn(self, image, threshold):
        if self.mask is None:
            result = image.matchTemplate(self.templ, gcc.TM_CCOEFF_NORMED)
        else:
            result = image.matchTemplate(self.templ, gcc.TM_CCORR_NORMED, self.mask)
        targetList = []
        while True:
            minMaxLoc = result.minMaxLoc()
            if minMaxLoc.maxVal > threshold:
                print("匹配[{0}]成功，相似度是{1}。".format(self.name, minMaxLoc.maxVal))
                targetList.append(Target(self.window, minMaxLoc.maxLoc, self.templ.getSize()))
            else:
                print("匹配[{0}]失败，相似度是{1}。".format(self.name, minMaxLoc.maxVal))
                break
            result.eraseMaxLoc(minMaxLoc, self.templ.getSize())
        return targetList


class Button:
    def __init__(self, window, name, templName):
        self.window = window
        self.name = name
        self.templ = gc.Image()
        self.templ.read(templName, gcc.RF_UNCHANGED)
        if self.templ.getType() != gcc.IT_8UC4:
            raise Exception("图片格式错误：请将图片保存为32位色。\n{0}".format(templName))

    def match(self, image, threshold):
        result = image.matchTemplate(self.templ, gcc.TM_CCOEFF_NORMED)
        minMaxLoc = result.minMaxLoc()
        if minMaxLoc.maxVal > threshold:
            print("匹配[{0}]成功，相似度是{1}。".format(self.name, minMaxLoc.maxVal))
            return Target(self.window, self.templ.getSize(), minMaxLoc.maxLoc)
        else:
            print("匹配[{0}]失败，相似度是{1}。".format(self.name, minMaxLoc.maxVal))
            return None


class Target:
    def __init__(self, window, size, location):
        self.window = window
        self.size = size
        self.location = location

    def click(self):
        self.window.click(self.location, self.size)
