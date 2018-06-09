# coding: utf-8

import GraphCap as gc
import Template
import Action


class Scene:
    pass


class MainScene(Scene):
    def __init__(self, window):
        self.weighAnchorAct = Action.ClickAction(window, Template.Template(window, "出击", "./Main/WeighAnchor.png"))

    def enterPrecombat(self):
        self.weighAnchorAct.execute()


class PrecombatScene(Scene):
    def __init__(self, window):
        self.backAct = Action.ClickAction(window, Template.Template(window, "返回", "./Precombat/Back.png"))
        self.exerciseAct = Action.ClickAction(window, Template.Template(window, "演习", "./Precombat/Exercise.png"))
        self.c03s04Templ = Template.Template(window, "3-4", "./Precombat/C03S04.png")
        self.goNowTempl = Template.Template(window, "立刻前往", "./Precombat/GoNow.png")
        self.goNowTempl2 = Template.Template(window, "立刻前往2", "./Precombat/GoNow2.png")

    def back(self):
        self.backAct.execute()

    def enterExercise(self):
        self.exerciseAct.execute()

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
        self.backAct = Action.ClickAction(window, Template.Template(window, "返回", "./Exercise/Back.png"))
        self.operationAct = Action.ClickAction(window, Template.Template(window, "演习", "./Exercise/Operation.png"),
                                               specifiedTarget=Template.Target(window, gc.Point(50, 128),
                                                                               gc.Size(160, 228)))
        self.startExerciseAct = Action.ClickAction(window,
                                                   Template.Template(window, "开始演习", "./Exercise/StartExercise.png"))
        self.weighAnchorAct = Action.ClickAction(window, Template.Template(window, "出击", "./Exercise/WeighAnchor.png"))
        self.ttcAct = Action.ClickAction(window, Template.Template(window, "点击继续", "./Exercise/TTC.png"), 0.90,
                                         specifiedTarget=Template.Target(window, gc.Point(50, 420),
                                                                         gc.Size(850, 130)))
        self.ttcAct2 = Action.ClickAction(window, Template.Template(window, "点击继续2", "./Exercise/TTC2.png"),
                                          specifiedTarget=Template.Target(window, gc.Point(50, 420),
                                                                          gc.Size(850, 130)))
        self.confirmAct = Action.ClickAction(window, Template.Template(window, "确认", "./Exercise/Confirm.png"))

    def back(self):
        self.backAct.execute()

    def enterExercise(self):
        self.operationAct.execute()
        self.startExerciseAct.execute()
        self.weighAnchorAct.execute()

    def leaveExercise(self):
        self.ttcAct.execute()
        self.ttcAct2.execute()
        self.confirmAct.execute()


class C03S04Scene(Scene):
    def __init__(self, window):
        self.recFleetTempl = Template.Template(window, "侦查舰队", "./SubChapter/RecFleet.png",
                                               "./SubChapter/RecFleetMask.png")
        self.mainFleetTempl = Template.Template(window, "主力舰队", "./SubChapter/MainFleet.png",
                                                "./SubChapter/MainFleetMask.png")
        self.airFleetTempl = Template.Template(window, "航空舰队", "./SubChapter/AirFleet.png",
                                               "./SubChapter/AirFleetMask.png")
        self.weighAnchorTempl = Template.Template(window, "出击", "./SubChapter/WeighAnchor.png")

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
