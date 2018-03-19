# coding: utf-8

import time

import Widget


class Scene:
    def __init__(self, window):
        self.window = window

    def matchSingle(self, template, similarity=0.99, timeout=15.0):
        print("正在匹配{0}……".format(template.name))
        beginTime = time.time()
        while time.time() - beginTime < timeout:
            image = self.window.capture()
            if image is None:
                time.sleep(0.5)
                continue
            target = template.matchSingleOn(image, similarity)
            if target is not None:
                return target
        print("匹配{0}失败。".format(template.name))
        return None


class PrecombatScene(Scene):
    def __init__(self, window):
        super().__init__(self.window)
        self.delay = 2.0

    def enterC03S04(self):
        c03s04 = Widget.Template(self.window, "3-4按钮", "./Precombat/C03S04.png")
        if c03s04.match(0.98):
            c03s04.click()
            time.sleep(self.delay)
            lkqw = Widget.Template(self.window, "立刻前往按钮", "./Precombat/LKQW.png")
            if lkqw.match():
                lkqw.click()
                time.sleep(self.delay)
                if lkqw.match(0.98):
                    lkqw.click()
                    time.sleep(self.delay)


class C03S04Scene(Scene):
    def __init__(self, window):
        super().__init__(self.window)
        self.delay = 2.0

    def enterBattle(self):
        zljdTemplate = Widget.Template(self.window, "主力舰队", "./SubChapter/ZLJD.png", "./SubChapter/ZLJDMask.png")
        zljdTarget = zljdTemplate.matchSingle()
        if zljdTarget is not None:
            zljdTarget.click()
            time.sleep(self.delay)
            weighAnchor = Widget.Template(self.window, "出击按钮", "./SubChapter/WeighAnchor.png")
            if weighAnchor.match():
                weighAnchor.click()
                time.sleep(self.delay)
