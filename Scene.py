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

    def sleep(self, min=1.0, max=3.0):
        time.sleep(random.uniform(min, max))


class PrecombatScene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.c03s04Button = Widget.Button(self.window, "3-4", "./Precombat/C03S04.png")
        self.goNowButton = Widget.Button(self.window, "立刻前往", "./Precombat/GoNow.png")
        self.goNow2Button = Widget.Button(self.window, "立刻前往2", "./Precombat/GoNow2.png")

    def enterC03S04(self):
        c03s04Target = None
        goNowTarget = None
        goNow2Target = None
        while True:
            image = self.window.capture()
            if image is None:
                time.sleep(0.1)
                continue

            if c03s04Target is None:
                c03s04Target = self.c03s04Button.match(image, 0.97)
                if c03s04Target is not None:
                    c03s04Target.click()
                    self.sleep()
                continue

            if goNowTarget is None:
                goNowTarget = self.goNowButton.match(image)
                if goNowTarget is not None:
                    goNowTarget.click()
                    self.sleep()
                continue

            if goNow2Target is None:
                goNow2Target = self.goNow2Button.match(image)
                if goNow2Target is not None:
                    goNow2Target.click()
                    self.sleep()
                    break


class C03S04Scene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.recFleetEnemy = Widget.Enemy(self.window, "侦查舰队", "./SubChapter/RecFleet.png",
                                          "./SubChapter/RecFleetMask.png")
        self.mainFleetEnemy = Widget.Enemy(self.window, "主力舰队", "./SubChapter/MainFleet.png",
                                           "./SubChapter/MainFleetMask.png")
        self.airFleetEnemy = Widget.Enemy(self.window, "航空舰队", "./SubChapter/AirFleet.png",
                                          "./SubChapter/AirFleetMask.png")
        self.weighAnchorButton = Widget.Button(self.window, "出击", "./SubChapter/WeighAnchor.png")

    def enterBattle(self):
        while True:
            image = self.window.capture()
            if image is None:
                time.sleep(0.1)
                continue

            recFleetTargetList = self.recFleetEnemy.match(image)
            mainFleetTargetList = self.mainFleetEnemy.match(image)
            airFleetTargetList = self.airFleetEnemy.match(image)

            display = image.clone()
            for recFleetTarget in recFleetTargetList:
                display.rectangle(gc.Rect(recFleetTarget.location, recFleetTarget.size), gc.Scalar(255, 0, 0))
            for mainFleetTarget in mainFleetTargetList:
                display.rectangle(gc.Rect(mainFleetTarget.location, mainFleetTarget.size), gc.Scalar(255, 0, 0))
            for airFleetTarget in airFleetTargetList:
                display.rectangle(gc.Rect(airFleetTarget.location, airFleetTarget.size), gc.Scalar(255, 0, 0))
            display.show("display")
            gc.Utils.WaitKey(1)

            print(len(recFleetTargetList))
            print(len(mainFleetTargetList))
            print(len(airFleetTargetList))
            if len(recFleetTargetList) > 0:
                recFleetTargetList[0].click()
                self.sleep()
            else:
                if len(mainFleetTargetList) > 0:
                    mainFleetTargetList[0].click()
                    self.sleep()
                else:
                    if len(airFleetTargetList) > 0:
                        airFleetTargetList[0].click()
                        self.sleep()

            # weighAnchorTarget = self.weighAnchorButton.match(image)
            # if weighAnchorTarget is not None:
            #    weighAnchorTarget.click()
            #    self.sleep()


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
