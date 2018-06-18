# coding: utf-8

import time
import random

import GraphCap as gc
import Template
import Action


class Scene:
    def sleep(self, min=1.0, max=2.0):
        time.sleep(random.uniform(min, max))


class MainScene(Scene):
    def __init__(self, window):
        self.weighAnchorAct = Action.ClickAction(window, Template.Template(window, "出击", "./Main/WeighAnchor.png"))

    def enterPrecombat(self):
        self.sleep()
        self.weighAnchorAct.execute()
        self.sleep()


class PrecombatScene(Scene):
    def __init__(self, window):
        self.backAct = Action.ClickAction(window, Template.Template(window, "返回", "./Precombat/Back.png"))
        self.exerciseAct = Action.ClickAction(window, Template.Template(window, "演习", "./Precombat/Exercise.png"))
        self.c03s04Act = Action.ClickAction(window, Template.Template(window, "3-4", "./Precombat/C03S04.png"), 0.95)
        self.goNowAct = Action.ClickAction(window, Template.Template(window, "立刻前往", "./Precombat/GoNow.png"))
        self.goNowAct2 = Action.ClickAction(window, Template.Template(window, "立刻前往2", "./Precombat/GoNow2.png"))

    def back(self):
        self.sleep()
        self.backAct.execute()
        self.sleep()

    def enterExercise(self):
        self.sleep()
        self.exerciseAct.execute()
        self.sleep()

    def enterC03S04(self):
        self.sleep()
        self.c03s04Act.execute()
        self.sleep()
        self.goNowAct.execute()
        self.sleep()
        self.goNowAct2.execute()
        self.sleep()


class ExerciseScene(Scene):
    def __init__(self, window):
        self.backAct = Action.ClickAction(window, Template.Template(window, "返回", "./Exercise/Back.png"))
        self.operationAct = Action.ClickAction(window, Template.Template(window, "演习", "./Exercise/Operation.png"),
                                               specifiedTarget=Template.SpecifiedTarget(window, gc.Point(50, 128),
                                                                                        gc.Size(160, 228)))
        self.startExerciseAct = Action.ClickAction(window,
                                                   Template.Template(window, "开始演习", "./Exercise/StartExercise.png"))
        self.weighAnchorAct = Action.ClickAction(window, Template.Template(window, "出击", "./Exercise/WeighAnchor.png"))
        self.ttcAct = Action.ClickAction(window, Template.Template(window, "点击继续", "./Exercise/TTC.png"), 0.85,
                                         specifiedTarget=Template.SpecifiedTarget(window, gc.Point(50, 420),
                                                                                  gc.Size(850, 130)))
        self.ttcAct2 = Action.ClickAction(window, Template.Template(window, "点击继续2", "./Exercise/TTC2.png"),
                                          specifiedTarget=Template.SpecifiedTarget(window, gc.Point(50, 420),
                                                                                   gc.Size(850, 130)))
        self.confirmAct = Action.ClickAction(window, Template.Template(window, "确认", "./Exercise/Confirm.png"))

    def back(self):
        self.sleep()
        self.backAct.execute()
        self.sleep()

    def enterExercise(self):
        self.sleep()
        self.operationAct.execute()
        self.sleep()
        self.startExerciseAct.execute()
        self.sleep()
        self.weighAnchorAct.execute()
        self.sleep()

    def leaveExercise(self):
        self.sleep()
        self.ttcAct.execute()
        self.sleep()
        self.ttcAct2.execute()
        self.sleep()
        self.confirmAct.execute()
        self.sleep()


class C03S04Scene(Scene):
    def __init__(self, window):
        self.recFleetTempl = Template.Template(window, "侦查舰队", "./Subchapter/RecFleet.png",
                                               "./Subchapter/RecFleetMask.png")
        self.mainFleetTempl = Template.Template(window, "主力舰队", "./Subchapter/MainFleet.png",
                                                "./Subchapter/MainFleetMask.png")
        self.airFleetTempl = Template.Template(window, "航空舰队", "./Subchapter/AirFleet.png",
                                               "./Subchapter/AirFleetMask.png")
        self.weighAnchorTempl = Template.Template(window, "出击", "./Subchapter/WeighAnchor.png")
        self.window = window
        self.mapX = 75
        self.mapY = 249
        self.mapWidth = 890
        self.mapHeight = 304
        self.map = [[0 for i in range(8)] for i in range(4)]
        self.pt = gc.PerspectiveTransform(gc.Size2f(890, 446), 304, 70, 81)

    def enterBattle(self):
        while True:
            image = self.window.capture()

            display = image.clone()
            recFleetTarget = self.recFleetTempl.matchOn(image)
            for i in range(5):
                if recFleetTarget.similarity > 0.95:
                    display.rectangle(gc.Rect(recFleetTarget.location, recFleetTarget.template.getSize()),
                                      gc.Scalar(255, 0, 0))
                recFleetTarget = recFleetTarget.next()
            mainFleetTarget = self.mainFleetTempl.matchOn(image)
            for i in range(5):
                if mainFleetTarget.similarity > 0.95:
                    display.rectangle(gc.Rect(mainFleetTarget.location, mainFleetTarget.template.getSize()),
                                      gc.Scalar(255, 0, 0))
                mainFleetTarget = mainFleetTarget.next()
            airFleetTarget = self.airFleetTempl.matchOn(image)
            for i in range(5):
                if airFleetTarget.similarity > 0.95:
                    display.rectangle(gc.Rect(airFleetTarget.location, airFleetTarget.template.getSize()),
                                      gc.Scalar(255, 0, 0))
                airFleetTarget = airFleetTarget.next()
            display.show("display")
            gc.Utils.WaitKey(1)


class BattleScene(Scene):
    def __init__(self, window):
        self.ttcTempl = Template.Template(window, "点击继续", "./Battle/TTC.png")
        self.performanceTempl = Template.Template(window, "性能", "./Battle/Performance.png")
        self.confirmTempl = Template.Template(window, "确认", "./Battle/Confirm.png")

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
