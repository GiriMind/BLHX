# coding: utf-8

import time
import random

import GraphCap as gc
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

    def matchEnemy(self, enemy, timeout, threshold):
        print("{0}秒内匹配[{1}]……".format(timeout, enemy.name))
        beginTime = time.time()
        while time.time() - beginTime < timeout:
            image = self.window.capture()
            if image is None:
                time.sleep(0.5)
                continue
            targetList = enemy.match(image, threshold)
            if len(targetList) > 0:
                return targetList
        print("匹配[{0}]超时。".format(enemy.name))
        return []

    def sleep(self):
        time.sleep(random.uniform(1.0, 3.0))


class PrecombatScene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.c03s04Button = Widget.Button(self.window, "3-4", "./Precombat/C03S04.png")
        self.goNowButton = Widget.Button(self.window, "立刻前往", "./Precombat/GoNow.png")

    def enterC03S04(self):
        c03s04Target = self.matchButton(self.c03s04Button, 5.0, 0.98)
        if c03s04Target is not None:
            c03s04Target.click()
            self.sleep()

            goNowTarget = self.matchButton(self.goNowButton, 5.0, 0.98)
            if goNowTarget is not None:
                goNowTarget.click()
                self.sleep()

                goNowTarget = self.matchButton(self.goNowButton, 5.0, 0.98)
                if goNowTarget is not None:
                    goNowTarget.click()
                    self.sleep()


class C03S04Scene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.recFleetEnemy = Widget.Enemy(self.window, "侦查舰队", "./SubChapter/RecFleet.png",
                                          "./SubChapter/RecFleetMask.png")
        self.airFleetEnemy = Widget.Enemy(self.window, "航空舰队", "./SubChapter/AirFleet.png",
                                          "./SubChapter/AirFleetMask.png")
        self.mainFleetEnemy = Widget.Enemy(self.window, "主力舰队", "./SubChapter/MainFleet.png",
                                           "./SubChapter/MainFleetMask.png")
        self.weighAnchorButton = Widget.Button(self.window, "出击", "./SubChapter/WeighAnchor.png")

    def enterBattle(self):
        zljdTargetList = self.matchEnemy(self.mainFleetEnemy, 5.0, 0.98)
        if len(zljdTargetList) > 0:
            zljdTargetList[0].click()
            self.sleep()

            weighAnchorTarget = self.matchButton(self.weighAnchorButton, 5.0, 0.98)
            if weighAnchorTarget is not None:
                weighAnchorTarget.click()
                self.sleep()


class BattleScene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.ttcButton = Widget.Button(self.window, "点击继续", "./Battle/TTC.png")
        self.performanceButton = Widget.Button(self.window, "性能", "./Battle/Performance.png")
        self.confirmButton = Widget.Button(self.window, "确认", "./Battle/Confirm.png")

    def leaveBattle(self):
        ttcTarget = self.matchButton(self.ttcButton, 310.0, 0.98)
        if ttcTarget is not None:
            ttcTarget.click()
            self.sleep()

            ttcTarget = self.matchButton(self.ttcButton, 5.0, 0.98)
            if ttcTarget is not None:
                ttcTarget.click()
                self.sleep()

                performanceTarget = self.matchButton(self.performanceButton, 5.0, 0.98)
                if performanceTarget is not None:
                    target = Widget.Target(self.window, gc.Point(100, 100), gc.Size(800, 320))
                    target.click()
                    self.sleep()

                confirmTarget = self.matchButton(self.confirmButton, 5.0, 0.98)
                if confirmTarget is not None:
                    confirmTarget.click()
                    self.sleep()
