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
    def __init__(self, name, filename, ratio=0.5):
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
    templates.append(Template("立刻前往", "./Precombat/ImmediateStart.png"))
    templates.append(Template("立刻前往2", "./Precombat/ImmediateStart2.png"))
    templates.append(Template("规避", "./Subchapter/Evade.png"))
    templates.append(Template("BOSS舰队", "./Subchapter/BossFleet.png", 0.2))
    templates.append(Template("侦查舰队", "./Subchapter/RecFleet.png", 0.2))
    templates.append(Template("航空舰队", "./Subchapter/AirFleet.png", 0.2))
    templates.append(Template("主力舰队", "./Subchapter/MainFleet.png", 0.2))
    templates.append(Template("运输舰队", "./Subchapter/TranFleet.png", 0.2))
    templates.append(Template("出击", "./Subchapter/WeighAnchor.png"))
    templates.append(Template("点击继续", "./Battle/TTC.png"))
    templates.append(Template("点击继续2", "./Battle/TTC2.png"))
    templates.append(Template("点击继续3", "./Battle/TTC3.png"))
    templates.append(Template("性能", "./Battle/Performance.png"))
    templates.append(Template("确定2", "./Battle/OK2.png"))
    templates.append(Template("大获全胜", "./Battle/Victory.png"))
    templates.append(Template("确定", "./Battle/OK.png"))

    enemies = []
    enemies.append(Template("侦查舰队", "./Subchapter/RecFleet.png", 0.2))
    enemies.append(Template("航空舰队", "./Subchapter/AirFleet.png", 0.2))
    enemies.append(Template("主力舰队", "./Subchapter/MainFleet.png", 0.2))
    enemies.append(Template("运输舰队", "./Subchapter/TranFleet.png", 0.2))

    random.seed()
    game = Game.Game()
    while True:
        scene = game.capture()
        kp, desc = sift.detectAndCompute(scene, None)
        # 全黑图
        if len(kp) == 0 or desc is None:
            continue
        for i in range(len(templates)):
            template = templates[i]
            # 降低CPU使用率
            time.sleep(0.01)
            matches = flann.knnMatch(template.desc, desc, 2)
            good = []
            for m, n in matches:
                if m.distance < n.distance * 0.66:
                    good.append(m)
            if len(good) < len(template.kp) * template.ratio:
                continue
            dstPts = np.float32([kp[m.trainIdx].pt for m in good]).reshape(-1, 2)
            # BOSS
            if i == 4:
                # 截取boss左侧子图
                minX, minY, maxX, maxY = 10000.0, 10000.0, 0.0, 0.0
                for pt in dstPts:
                    # cv2.circle(scene, (int(pt[0]), int(pt[1])), 2, (0, 0, 255))
                    if pt[0] < minX:
                        minX = pt[0]
                    if pt[1] < minY:
                        minY = pt[1]
                    if pt[0] > maxX:
                        maxX = pt[0]
                    if pt[1] > maxY:
                        maxY = pt[1]
                # cv2.imshow("scene", scene)
                # cv2.waitKey()
                width = maxX - minX
                height = maxY - minY
                maxX = maxX - width
                maxY = maxY + height * 3.0
                minX = minX - width * 1.5
                minY = minY - height * 3.0
                # print("{0} {1} {2} {3}".format(minX, minY, width, height))
                target = scene[int(minY):int(maxY), int(minX):int(maxX)]
                if target is None:
                    continue
                # cv2.rectangle(scene, (int(minX), int(minY)), (int(maxX), int(maxY)), (0, 0, 255), 1)
                # cv2.imshow("scene", scene)
                # cv2.imshow("target", target)
                # cv2.waitKey()
                kp2, desc2 = sift.detectAndCompute(target, None)
                # 全黑图
                if len(kp2) == 0 or desc2 is None:
                    continue
                clicked = False
                for i in range(len(enemies)):
                    enemy = enemies[i]
                    # 降低CPU使用率
                    time.sleep(0.01)
                    matches = flann.knnMatch(enemy.desc, desc2, 2)
                    good = []
                    for m, n in matches:
                        if m.distance < n.distance * 0.66:
                            good.append(m)
                    if len(good) < len(enemy.kp) * enemy.ratio:
                        continue
                    dstPts2 = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 2)
                    # x, y = np.mean(dstPts2, axis=0)
                    x2, y2 = dstPts2[random.randint(0, len(dstPts2) - 1)]
                    game.mouseClick((int(minX + x2), int(minY + y2)))
                    time.sleep(1.0)
                    clicked = True
                    print("BOSS被堵塞")
                    break
                # 没点击小弟
                if not clicked:
                    print("BOSS未堵塞")
                    # x, y = np.mean(dstPts, axis=0)
                    x, y = dstPts[random.randint(0, len(dstPts) - 1)]
                    game.mouseClick((int(x), int(y)))
                    time.sleep(1.0)
                    break
            else:
                # x, y = np.mean(dstPts, axis=0)
                x, y = dstPts[random.randint(0, len(dstPts) - 1)]
                game.mouseClick((int(x), int(y)))
                time.sleep(1.0)
                break
