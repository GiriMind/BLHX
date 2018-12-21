# coding: utf-8

import cv2
import numpy as np


class Template:
    def __init__(self, game, name, filename):
        self.game = game
        self.name = name
        self.image = cv2.imread(filename)
        if self.image is None:
            raise Exception("载入模板图片失败：{0}".format(filename))

    def matchOn(self, scene):
        # sift = cv2.xfeatures2d.SIFT_create()
        surf = cv2.xfeatures2d.SURF_create(400)
        kp1, desc1 = surf.detectAndCompute(self.image, None)
        kp2, desc2 = surf.detectAndCompute(scene, None)

        # bf = cv2.BFMatcher(cv2.NORM_L2)
        # matches = bf.knnMatch(desc1, desc2, 2)
        FLANN_INDEX_KDTREE = 0
        indexParams = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        searchParams = dict(checks=50)
        flann = cv2.FlannBasedMatcher(indexParams, searchParams)
        matches = flann.knnMatch(desc1, desc2, 2)

        good = []
        for m, n in matches:
            if m.distance < 0.66 * n.distance:
                good.append(m)
        if len(good) < len(kp1) / 2:
            return None

        # srcPts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,2)
        dstPts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 2)
        x, y = np.mean(dstPts, axis=0)
        return Target(self.game, (int(x), int(y)))


class Target:
    def __init__(self, game, pos, size=None):
        self.game = game
        self.pos = pos
        self.size = size

    def click(self):
        self.game.click(self.pos, self.size)


if __name__ == "__main__":
    scene = cv2.imread("1.png")
    templ = Template(None, None, "./Main/WeighAnchor.png")
    templ.matchOn(scene)
