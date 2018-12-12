# coding: utf-8

import cv2
import numpy as np


class Template:
    def __init__(self, game, name, filename):
        self.game = game
        self.name = name
        self.image = cv2.imread(filename)
        if self.image is None:
            raise Exception("载入图片失败：{0}".format(filename))

    def matchOn(self, scene):
        sift = cv2.xfeatures2d.SIFT_create()
        # surf = cv2.xfeatures2d.SURF_create()
        kp1, desc1 = sift.detectAndCompute(self.image, None)
        kp2, desc2 = sift.detectAndCompute(scene, None)
        matcher = cv2.BFMatcher(cv2.NORM_L2)
        matches = matcher.knnMatch(desc1, desc2, 2)
        good = []
        for m, n in matches:
            if m.distance < 0.66 * n.distance:
                good.append(m)
        
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
