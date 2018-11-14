# coding: utf-8

import sys
import time
import random

import GraphCap as gc
import Template


class Scene:
    def __init__(self, game):
        self.game = game

    def sleep(self, min=1.0, max=2.0):
        time.sleep(random.uniform(min, max))

    def clickOnce(self, template):
        scene = self.game.capture()
        target = template.matchOn(scene)
        if target is not None:
            target.click()
            return True
        else:
            print("匹配[{0}]失败。".format(template.name))
            return False

    def click(self, template, timeout=sys.float_info.max):
        beginTime = time.time()
        while True:
            if time.time() - beginTime > timeout:
                print("匹配[{0}]超时。".format(template.name))
                return False
            if self.clickOnce(template):
                return True


class MainScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.weighAnchor = Template.Template(game, "出击", "./Main/WeighAnchor.png")
        self.maid = Template.Template(game, "演习作战", "./Main/Maid.png")

    def enterPrecombat(self):
        self.click(self.weighAnchor)

    def enterMaid(self):
        self.click(self.maid)


class PrecombatScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.back = Template.Template(game, "返回", "./Precombat/Back.png")
        self.exercise = Template.Template(game, "演习", "./Precombat/Exercise.png")
        self.goNow = Template.Template(game, "立刻前往", "./Precombat/GoNow.png")
        self.goNow2 = Template.Template(game, "立刻前往2", "./Precombat/GoNow2.png")

        self.chapterTemplates = []
        self.chapterTemplates.append(Template.Template(game, "第1章", "./Precombat/C01.png"))
        self.chapterTemplates.append(Template.Template(game, "第2章", "./Precombat/C02.png"))
        self.chapterTemplates.append(Template.Template(game, "第3章", "./Precombat/C03.png"))
        self.chapterTemplates.append(Template.Template(game, "第4章", "./Precombat/C04.png"))
        self.chapterTemplates.append(Template.Template(game, "第5章", "./Precombat/C05.png"))
        self.chapterTemplates.append(Template.Template(game, "第6章", "./Precombat/C06.png"))
        self.chapterTemplates.append(Template.Template(game, "第7章", "./Precombat/C07.png"))
        self.chapterTemplates.append(Template.Template(game, "第8章", "./Precombat/C08.png"))
        self.chapterTemplates.append(Template.Template(game, "第9章", "./Precombat/C09.png"))
        self.chapterTemplates.append(Template.Template(game, "第10章", "./Precombat/C10.png"))
        self.chapterTemplates.append(Template.Template(game, "第11章", "./Precombat/C11.png"))
        self.chapterTemplates.append(Template.Template(game, "第12章", "./Precombat/C12.png"))

        self.subcapterTargets = {}
        self.subcapterTargets[100 * 1 + 1] = Template.Target(game, gc.Point(160, 376), gc.Size(114, 24))
        self.subcapterTargets[100 * 3 + 4] = Template.Target(game, gc.Point(507, 306), gc.Size(137, 25))

        self.prevPageTarget = Template.Target(game, gc.Point(40, 300), gc.Size(25, 35))
        self.nextPageTarget = Template.Target(game, gc.Point(910, 300), gc.Size(25, 35))

    def back(self):
        self.click(self.back)

    def enterExercise(self):
        self.click(self.exercise)

    def getChapter(self):
        while True:
            scene = self.game.capture()
            subScene = scene.clip(gc.Rect(30, 115, 28, 20))
            for i in range(len(self.chapterTemplates)):
                template = self.chapterTemplates[i]
                target = template.matchOn(subScene)
                if target is not None:
                    return i + 1

    def enterSubcapter(self, capter, subcapter):
        current = self.getChapter()
        print("当前是第{0}章".format(current))
        if capter < current:
            for i in range(current - capter):
                self.prevPageTarget.click()
        if capter > current:
            for i in range(capter - current):
                self.nextPageTarget.click()
        current = self.getChapter()
        if current != capter:
            print("第{0}章不存在。".format(capter))
            return False
        key = 100 * capter + subcapter
        if key not in self.subcapterTargets:
            print("{0}-{1}不存在。".format(capter, subcapter))
            return False
        subcapterTarget = self.subcapterTargets[key]
        subcapterTarget.click()
        self.click(self.goNow)
        self.click(self.goNow2)
        return True


class ExerciseScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.back = Template.Template(game, "返回", "./Exercise/Back.png")
        self.operation = Template.Template(game, "演习", "./Exercise/Operation.png")
        self.firstOne = Template.Target(game, gc.Point(50, 128), gc.Size(160, 228))
        self.startExercise = Template.Template(game, "开始演习", "./Exercise/StartExercise.png")
        self.weighAnchor = Template.Template(game, "出击", "./Exercise/WeighAnchor.png")
        self.ttc = Template.Template(game, "点击继续", "./Exercise/TTC.png")
        self.ttc2 = Template.Template(game, "点击继续2", "./Exercise/TTC2.png")
        self.confirm = Template.Template(game, "确认", "./Exercise/Confirm.png")

    def back(self):
        self.click(self.back)

    def enterExercise(self):
        # self.click(self.operation, self.firstOne)
        self.click(self.startExercise)
        self.click(self.weighAnchor)

    def leaveExercise(self):
        self.click(self.ttc)
        self.click(self.ttc2)
        self.click(self.confirm)


class MaidScene(ExerciseScene):
    def __init__(self, game):
        super().__init__(game)
        self.advanced = Template.Template(game, "高级演习", "./Events/Advanced.png")

    def enterExercise(self):
        self.click(self.advanced)
        self.click(self.weighAnchor)


class SubchapterScene(Scene):
    def __init__(self, game):
        super().__init__(game)


class C01S01Scene(SubchapterScene):
    def __init__(self, game):
        super().__init__(game)
        self.enterAmbushTarget = Template.Target(game, gc.Point(330, 252), gc.Size(87, 64))
        self.leaveAmbushTarget = Template.Target(game, gc.Point(238, 252), gc.Size(83, 64))
        self.meet = Template.Template(game, "迎击", "./Subchapter/Meet.png")
        self.weighAnchor = Template.Template(game, "出击", "./Subchapter/WeighAnchor.png")

    def enterAmbush(self):
        self.sleep(3.0, 5.0)
        self.enterAmbushTarget.click()
        self.click(self.meet)
        self.click(self.weighAnchor)

    def leaveAmbush(self):
        self.leaveAmbushTarget.click()
        self.sleep(3.0, 5.0)


class C03S04Scene(SubchapterScene):
    def __init__(self, game):
        super().__init__(game)
        self.recFleetTempl = Template.Template("侦查舰队", "./Subchapter/RecFleet.png", "./Subchapter/RecFleetMask.png")
        self.mainFleetTempl = Template.Template("主力舰队", "./Subchapter/MainFleet.png", "./Subchapter/MainFleetMask.png")
        self.airFleetTempl = Template.Template("航空舰队", "./Subchapter/AirFleet.png", "./Subchapter/AirFleetMask.png")
        self.weighAnchorTempl = Template.Template("出击", "./Subchapter/WeighAnchor.png")

        self.mapX = 74
        self.mapY = 250 - (448 - 304)
        self.tileSize = 110
        self.columns = 8
        self.rows = 4
        self.pt = gc.PerspectiveTransform(gc.Size2f(890, 448), 304, 70, 81)
        self.map = [[0 for i in range(self.columns)] for i in range(self.rows)]

    def enterBattle(self):
        while True:
            image = self.game.capture()

            map = [[0 for i in range(self.columns)] for i in range(self.rows)]
            recFleetTarget = self.recFleetTempl.matchOn(image)
            for i in range(5):
                if recFleetTarget.similarity > 0.95:
                    size = recFleetTarget.getSize()
                    x = recFleetTarget.location.x - self.mapX + size.width / 2
                    y = recFleetTarget.location.y - self.mapY + size.height / 2
                    transPos = self.pt.transform(gc.Point2f(x, y))
                    col = int(transPos.x / self.tileSize)
                    row = int(transPos.y / self.tileSize)
                    if 0 <= col < self.columns and 0 <= row < self.rows:
                        map[row][col] = 1
                recFleetTarget = recFleetTarget.next()
            mainFleetTarget = self.mainFleetTempl.matchOn(image)
            for i in range(5):
                if mainFleetTarget.similarity > 0.95:
                    size = recFleetTarget.getSize()
                    x = mainFleetTarget.location.x - self.mapX + size.width / 2
                    y = mainFleetTarget.location.y - self.mapY + size.height / 2
                    transPos = self.pt.transform(gc.Point2f(x, y))
                    col = int(transPos.x / self.tileSize)
                    row = int(transPos.y / self.tileSize)
                    if 0 <= col < self.columns and 0 <= row < self.rows:
                        map[row][col] = 2
                mainFleetTarget = mainFleetTarget.next()
            airFleetTarget = self.airFleetTempl.matchOn(image)
            for i in range(5):
                if airFleetTarget.similarity > 0.95:
                    size = recFleetTarget.getSize()
                    x = airFleetTarget.location.x - self.mapX + size.width / 2
                    y = airFleetTarget.location.y - self.mapY + size.height / 2
                    transPos = self.pt.transform(gc.Point2f(x, y))
                    col = int(transPos.x / self.tileSize)
                    row = int(transPos.y / self.tileSize)
                    if 0 <= col < self.columns and 0 <= row < self.rows:
                        map[row][col] = 3
                airFleetTarget = airFleetTarget.next()
            print("--------------------------------------------")
            for row in range(4):
                line = str()
                for col in range(8):
                    id = map[row][col]
                    line += " %d " % id
                print(line)
            print("--------------------------------------------")
            self.sleep()


class BattleScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.ttc = Template.Template(game, "点击继续", "./Battle/TTC.png")
        self.ttc2 = Template.Template(game, "点击继续2", "./Battle/TTC2.png")
        self.performance = Template.Template(game, "性能", "./Battle/Performance.png")
        self.confirm = Template.Template(game, "确认", "./Battle/Confirm.png")

    def leaveBattle(self):
        self.click(self.ttc)
        self.click(self.ttc2)
        self.click(self.performance, 3.0)
        self.click(self.confirm)
