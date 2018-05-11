# coding: utf-8

import time
import random

import GraphCap as gc
import GraphCapCon as gcc
import Widget

class Scene:
    def __init__(self, window):
        self.window = window
        self.bossExist = True

    def matchButton(self, button, timeout, threshold):
        print("{0}秒内匹配[{1}]……".format(timeout, button.name))
        beginTime = time.time()
        while time.time() - beginTime < timeout:
            image = self.window.capture()
            if image is None:
                time.sleep(0.5)
                continue
            target = button.match(image, threshold)
            if target is not None:
                return target
        print("匹配[{0}]超时。".format(button.name))
        return None

    def matchMulti(self, template, timeout, threshold):
        print("{0}秒内匹配[{1}]……".format(timeout, template.name))
        beginTime = time.time()
        while time.time() - beginTime < timeout:
            image = self.window.capture()
            if image is None:
                time.sleep(0.5)
                continue
            targetList = template.matchMultiOn(image, threshold)
            if len(targetList) > 0:
                return targetList
        print("匹配[{0}]超时。".format(template.name))
        return []

    def sleep(self):
        time.sleep(random.uniform(1.0, 3.0))


class PrecombatScene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.c03s04Btn = Widget.Button(self.window, "3-4", "./Precombat/C03S04.png")
        self.lkqwBtn = Widget.Button(self.window, "立刻前往", "./Precombat/LKQW.png")

    def enterC03S04(self):
        c03s04Target = self.matchButton(self.c03s04Btn, 5.0, 0.92)
        if c03s04Target is not None:
            c03s04Target.click()
            self.sleep()

            lkqwTarget = self.matchButton(self.lkqwBtn, 5.0, 0.98)
            if lkqwTarget is not None:
                lkqwTarget.click()
                self.sleep()

                lkqwTarget = self.matchButton(self.lkqwBtn, 5.0, 0.98)
                if lkqwTarget is not None:
                    lkqwTarget.click()
                    self.sleep()


class C03S04Scene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.zljdTempl = Widget.Template(self.window, "主力舰队", "./SubChapter/ZLJD.png", "./SubChapter/ZLJDMask.png")
        self.weighAnchorBtn = Widget.Button(self.window, "出击", "./SubChapter/WeighAnchor.png")

    def enterBattle(self):
        zljdTargetList = self.matchMulti(self.zljdTempl, 5.0, 0.98)
        if len(zljdTargetList) > 0:
            zljdTargetList[0].click()
            self.sleep()

            weighAnchorTarget = self.matchButton(self.weighAnchorBtn, 5.0, 0.98)
            if weighAnchorTarget is not None:
                weighAnchorTarget.click()
                self.sleep()


class BattleScene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.ttcBtn = Widget.Button(self.window, "点击继续", "./Battle/TTC.png")
        self.performanceBtn = Widget.Button(self.window, "性能", "./Battle/Performance.png")
        self.confirmBtn = Widget.Button(self.window, "确认", "./Battle/Confirm.png")

    def leaveBattle(self):
        ttcTarget = self.matchButton(self.ttcBtn, 302.0, 0.98)
        if ttcTarget is not None:
            ttcTarget.click()
            self.sleep()

            ttcTarget = self.matchButton(self.ttcBtn, 5.0, 0.98)
            if ttcTarget is not None:
                ttcTarget.click()
                self.sleep()

                performanceTarget = self.matchButton(self.performanceBtn, 5.0, 0.98)
                if performanceTarget is not None:
                    target = Widget.Target(self.window, gc.Point(100, 100), gc.Size(800, 320))
                    target.click()
                    self.sleep()

                confirmTarget = self.matchButton(self.confirmBtn, 5.0, 0.98)
                if confirmTarget is not None:
                    confirmTarget.click()
                    self.sleep()
