# coding: utf-8

import time
import random

import Widget


class Scene:
    def __init__(self, window):
        self.window = window

    def matchSingle(self, template, threshold=0.99, timeout=15.0):
        print("正在匹配[{0}]……".format(template.name))
        beginTime = time.time()
        while time.time() - beginTime < timeout:
            image = self.window.capture()
            if image is None:
                time.sleep(0.5)
                continue
            target = template.matchSingleOn(image, threshold)
            if target is not None:
                print("匹配[{0}]成功。".format(template.name))
                return target
        print("匹配[{0}]超时失败。".format(template.name))
        return None

    def matchMulti(self, template, threshold=0.99, timeout=15.0):
        print("正在匹配[{0}]……".format(template.name))
        beginTime = time.time()
        while time.time() - beginTime < timeout:
            image = self.window.capture()
            if image is None:
                time.sleep(0.5)
                continue
            targetList = template.matchMultiOn(image, threshold)
            if len(targetList) > 0:
                print("匹配[{0}]成功。".format(template.name))
                return targetList
        print("匹配[{0}]超时失败。".format(template.name))
        return []

    def sleep(self):
        time.sleep(random.uniform(3.0, 5.5))


class PrecombatScene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.c03s04Templ = Widget.Template(self.window, "3-4", "./Precombat/C03S04.png")
        self.lkqwTempl = Widget.Template(self.window, "立刻前往", "./Precombat/LKQW.png")

    def enterC03S04(self):
        c03s04Target = self.matchSingle(self.c03s04Templ, 0.92)
        if c03s04Target is not None:
            c03s04Target.click()
            self.sleep()

            lkqwTarget = self.matchSingle(self.lkqwTempl)
            if lkqwTarget is not None:
                lkqwTarget.click()
                self.sleep()

                lkqwTarget = self.matchSingle(self.lkqwTempl, 0.98)
                if lkqwTarget is not None:
                    lkqwTarget.click()
                    self.sleep()


class C03S04Scene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.zljdTempl = Widget.Template(self.window, "主力舰队", "./SubChapter/ZLJD.png", "./SubChapter/ZLJDMask.png")
        self.weighAnchorTempl = Widget.Template(self.window, "出击", "./SubChapter/WeighAnchor.png")

    def enterBattle(self):
        zljdTargetList = self.matchMulti(self.zljdTempl, 0.98)
        if len(zljdTargetList) > 0:
            zljdTargetList[0].click()
            self.sleep()

            weighAnchorTarget = self.matchSingle(self.weighAnchorTempl)
            if weighAnchorTarget is not None:
                weighAnchorTarget.click()
                self.sleep()


class BattleScene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.ttcTempl = Widget.Template(self.window, "点击继续", "./Battle/TTC.png")
        self.performanceTempl = Widget.Template(self.window, "性能", "./Battle/Performance.png")
        self.confirmTempl = Widget.Template(self.window, "确认", "./Battle/Confirm.png")

    def leaveBattle(self):
        ttcTarget = self.matchSingle(self.ttcTempl, 0.99, 300.0)
        if ttcTarget is not None:
            ttcTarget.click()
            self.sleep()

            ttcTarget = self.matchSingle(self.ttcTempl)
            if ttcTarget is not None:
                ttcTarget.click()
                self.sleep()

                performanceTarget = self.matchSingle(self.performanceTempl)
                if performanceTarget is not None:
                    performanceTarget.click()
                    self.sleep()

                confirmTarget = self.matchSingle(self.confirmTempl)
                if confirmTarget is not None:
                    confirmTarget.click()
                    self.sleep()
