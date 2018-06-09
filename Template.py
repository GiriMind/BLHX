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
            raise Exception("模板图片格式错误：请保存为32位色。\n{0}".format(templName))
        if maskName is None:
            self.mask = None
        else:
            self.mask = gc.Image()
            self.mask.read(maskName, gcc.RF_UNCHANGED)
            if self.mask.getType() != gcc.IT_8UC4:
                raise Exception("掩码图片格式错误：请保存为32位色。\n{0}".format(maskName))

    def matchOn(self, image, threshold):
        if self.mask is None:
            result = image.matchTemplate(self.templ, gcc.MTM_CCOEFF_NORMED)
        else:
            result = image.matchTemplate(self.templ, gcc.MTM_CCORR_NORMED, self.mask)
        minMaxLoc = result.minMaxLoc()
        if minMaxLoc.maxVal > threshold:
            print("匹配[{0}]成功，相似度是{1}。".format(self.name, minMaxLoc.maxVal))
            return Target(self.window, minMaxLoc.maxLoc, self.templ.getSize())
        else:
            print("匹配[{0}]失败，相似度是{1}。".format(self.name, minMaxLoc.maxVal))
            return None

    def matchMultiOn(self, image, threshold):
        if self.mask is None:
            result = image.matchTemplate(self.templ, gcc.MTM_CCOEFF_NORMED)
        else:
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
