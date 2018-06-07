# coding: utf-8

import time
import random

import GraphCap as gc
import Template


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
            target = button.matchOn(image, threshold)
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
            targetList = enemy.matchOn(image, threshold)
            if len(targetList) > 0:
                return targetList
        print("匹配[{0}]超时。".format(enemy.name))
        return []

    def sleep(self, min=1.0, max=3.0):
        time.sleep(random.uniform(min, max))


class MainScene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.weighAnchorTempl = Template.Template(self.window, "出击", "./Main/WeighAnchor.png")

    def enterPrecombat(self):
        while True:
            image = self.window.capture()
            if image is None:
                time.sleep(0.1)
                continue
            weighAnchorTarget = self.weighAnchorTempl.matchOn(image)
            if weighAnchorTarget is not None:
                weighAnchorTarget.click()
                self.sleep()
                break


class PrecombatScene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.exerciseTempl = Template.Template(self.window, "演习", "./Precombat/Exercise.png")
        self.c03s04Templ = Template.Template(self.window, "3-4", "./Precombat/C03S04.png")
        self.goNowTempl = Template.Template(self.window, "立刻前往", "./Precombat/GoNow.png")
        self.goNowTempl2 = Template.Template(self.window, "立刻前往2", "./Precombat/GoNow2.png")

    def enterExercise(self):
        while True:
            image = self.window.capture()
            if image is None:
                time.sleep(0.1)
                continue
            exerciseTarget = self.exerciseTempl.matchOn(image)
            if exerciseTarget is not None:
                exerciseTarget.click()
                self.sleep()
                break

    def enterC03S04(self):
        c03s04Target = None
        goNowTarget = None
        goNowTarget2 = None
        while True:
            image = self.window.capture()
            if image is None:
                time.sleep(0.1)
                continue
            if c03s04Target is None:
                c03s04Target = self.c03s04Templ.matchOn(image, 0.97)
                if c03s04Target is not None:
                    c03s04Target.click()
                    self.sleep()
                continue
            if goNowTarget is None:
                goNowTarget = self.goNowTempl.matchOn(image)
                if goNowTarget is not None:
                    goNowTarget.click()
                    self.sleep()
                continue
            if goNowTarget2 is None:
                goNowTarget2 = self.goNowTempl2.matchOn(image)
                if goNowTarget2 is not None:
                    goNowTarget2.click()
                    self.sleep()
                    break


class ExerciseScene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.operationTempl = Template.Template(self.window, "演习", "./Exercise/Operation.png")
        self.startExerciseTempl = Template.Template(self.window, "开始演习", "./Exercise/StartExercise.png")
        self.weighAnchorTempl = Template.Template(self.window, "出击", "./Exercise/WeighAnchor.png")
        self.ttcTempl = Template.Template(self.window, "点击继续", "./Exercise/TTC.png")
        self.ttcTempl2 = Template.Template(self.window, "点击继续2", "./Exercise/TTC2.png")
        self.confirmTempl = Template.Template(self.window, "确认", "./Exercise/Confirm.png")

    def enterExercise(self):
        operationTarget = None
        startExerciseTarget = None
        weighAnchorTarget = None
        while True:
            image = self.window.capture()
            if image is None:
                time.sleep(0.1)
                continue
            if operationTarget is None:
                operationTarget = self.operationTempl.matchOn(image)
                if operationTarget is not None:
                    target = Template.Target(self.window, gc.Point(50, 128), gc.Size(160, 228))
                    target.click()
                    self.sleep()
                continue
            if startExerciseTarget is None:
                startExerciseTarget = self.startExerciseTempl.matchOn(image)
                if startExerciseTarget is not None:
                    startExerciseTarget.click()
                    self.sleep()
                continue
            if weighAnchorTarget is None:
                weighAnchorTarget = self.weighAnchorTempl.matchOn(image)
                if weighAnchorTarget is not None:
                    weighAnchorTarget.click()
                    self.sleep()
                    break

    def leaveExercise(self):
        ttcTarget = None
        ttcTarget2 = None
        confirmTarget = None
        while True:
            image = self.window.capture()
            if image is None:
                time.sleep(0.1)
                continue
            if ttcTarget is None:
                ttcTarget = self.ttcTempl.matchOn(image, 0.90)
                if ttcTarget is not None:
                    ttcTarget.click()
                    self.sleep()
                else:
                    time.sleep(1.0)
                continue
            if ttcTarget2 is None:
                ttcTarget2 = self.ttcTempl2.matchOn(image)
                if ttcTarget2 is not None:
                    ttcTarget2.click()
                    self.sleep()
                continue
            if confirmTarget is None:
                confirmTarget = self.confirmTempl.matchOn(image)
                if confirmTarget is not None:
                    confirmTarget.click()
                    self.sleep()
                    break


class C03S04Scene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.recFleetTempl = Template.Template(self.window, "侦查舰队", "./SubChapter/RecFleet.png",
                                               "./SubChapter/RecFleetMask.png")
        self.mainFleetTempl = Template.Template(self.window, "主力舰队", "./SubChapter/MainFleet.png",
                                                "./SubChapter/MainFleetMask.png")
        self.airFleetTempl = Template.Template(self.window, "航空舰队", "./SubChapter/AirFleet.png",
                                               "./SubChapter/AirFleetMask.png")
        self.weighAnchorTempl = Template.Template(self.window, "出击", "./SubChapter/WeighAnchor.png")

    def enterBattle(self):
        while True:
            image = self.window.capture()
            if image is None:
                time.sleep(0.1)
                continue

            recFleetTargetList = self.recFleetTempl.matchMultiOn(image, 0.985)
            mainFleetTargetList = self.mainFleetTempl.matchMultiOn(image, 0.985)
            airFleetTargetList = self.airFleetTempl.matchMultiOn(image, 0.985)

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

            # weighAnchorTarget = self.weighAnchorTempl.match(image)
            # if weighAnchorTarget is not None:
            #    weighAnchorTarget.click()
            #    self.sleep()


class BattleScene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.ttcTempl = Template.Template(self.window, "点击继续", "./Battle/TTC.png")
        self.performanceTempl = Template.Template(self.window, "性能", "./Battle/Performance.png")
        self.confirmTempl = Template.Template(self.window, "确认", "./Battle/Confirm.png")

    def leaveBattle(self):
        ttcTarget = self.matchButton(self.ttcTempl, 310.0, 0.98)
        if ttcTarget is not None:
            ttcTarget.click()
            self.sleep()

            ttcTarget = self.matchButton(self.ttcTempl, 5.0, 0.98)
            if ttcTarget is not None:
                ttcTarget.click()
                self.sleep()

                performanceTarget = self.matchButton(self.performanceTempl, 5.0, 0.98)
                if performanceTarget is not None:
                    target = Template.Target(self.window, gc.Point(100, 100), gc.Size(800, 320))
                    target.click()
                    self.sleep()

                confirmTarget = self.matchButton(self.confirmTempl, 5.0, 0.98)
                if confirmTarget is not None:
                    confirmTarget.click()
                    self.sleep()
