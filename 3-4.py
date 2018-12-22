# coding: utf-8

import sys
import os
import time
import random
import cv2
import numpy as np

sys.path.append(os.path.dirname(__file__))

import Game

sift = cv2.xfeatures2d.SIFT_create()
# surf = cv2.xfeatures2d.SURF_create(400)

FLANN_INDEX_KDTREE = 0
indexParams = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
searchParams = dict(checks=50)
flann = cv2.FlannBasedMatcher(indexParams, searchParams)


class Template:
    def __init__(self, name, filename, ratio=2):
        self.name = name
        self.image = cv2.imread(filename)
        if self.image is None:
            raise Exception("载入模板图片失败：{0}".format(filename))
        self.kp, self.desc = sift.detectAndCompute(self.image, None)
        if len(self.kp) == 0 or self.desc is None:
            raise Exception("无法检测到特征点：{0}".format(filename))
        self.ratio = ratio


if __name__ == "__main__":
    templates = []
    templates.append(Template("3-4", "./Precombat/3-4.png"))
    templates.append(Template("立刻前往", "./Precombat/GoNow.png"))
    templates.append(Template("立刻前往2", "./Precombat/GoNow2.png"))
    templates.append(Template("规避", "./Subchapter/Evade.png"))
    templates.append(Template("BOSS舰队", "./Subchapter/BossFleet.png", 5))
    templates.append(Template("侦查舰队", "./Subchapter/RecFleet.png", 5))
    templates.append(Template("航空舰队", "./Subchapter/AirFleet.png", 5))
    templates.append(Template("主力舰队", "./Subchapter/MainFleet.png", 5))
    templates.append(Template("运输舰队", "./Subchapter/TranFleet.png", 5))
    templates.append(Template("出击", "./Subchapter/WeighAnchor.png"))
    templates.append(Template("点击继续", "./Battle/TTC.png"))
    templates.append(Template("点击继续2", "./Battle/TTC2.png"))
    templates.append(Template("性能", "./Battle/Performance.png"))
    templates.append(Template("确定", "./Battle/OK.png"))
    templates.append(Template("确认", "./Battle/Confirm.png"))
    templates.append(Template("大获全胜", "./Battle/Victory.png"))

    random.seed()
    game = Game.Game()
    while True:
        scene = game.capture()
        kp, desc = sift.detectAndCompute(scene, None)
        # 全黑图
        if len(kp) == 0 or desc is None:
            continue
        for template in templates:
            # 降低CPU使用率
            time.sleep(0.01)
            matches = flann.knnMatch(template.desc, desc, 2)
            good = []
            for m, n in matches:
                if m.distance < 0.66 * n.distance:
                    good.append(m)
            if len(good) < len(template.kp) / template.ratio:
                continue
            dstPts = np.float32([kp[m.trainIdx].pt for m in good]).reshape(-1, 2)
            # x, y = np.mean(dstPts, axis=0)
            x, y = dstPts[random.randint(0, len(dstPts) - 1)]
            game.click((int(x), int(y)))
            time.sleep(1.0)
            break
