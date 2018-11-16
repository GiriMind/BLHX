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

    def match(self, template, timeout=sys.float_info.max):
        beginTime = time.time()
        while time.time() - beginTime < timeout:
            scene = self.game.capture()
            target = template.matchOn(scene)
            if target is not None:
                print("匹配[{0}]成功。".format(template.name))
                return target
            else:
                print("匹配[{0}]失败。".format(template.name))
        print("匹配[{0}]超时。".format(template.name))
        return None

    def click(self, template, timeout=sys.float_info.max):
        target = self.match(template, timeout)
        if target is not None:
            target.click()
            return True
        else:
            return False

    def matchList(self, templates):
        scene = self.game.capture()
        for i in range(len(templates)):
            template = templates[i]
            target = template.matchOn(scene)
            if target is not None:
                print("匹配[{0}]成功。".format(template.name))
                return target, i
            else:
                print("匹配[{0}]失败。".format(template.name))
        return None, -1


class MainScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.weighAnchor = Template.Template(game, "出击", "./Main/WeighAnchor.png")

        self.maid = Template.Template(game, "演习作战", "./Events/Maid.png")

    def enterPrecombat(self):
        self.click(self.weighAnchor)

    def enterMaid(self):
        return self.click(self.maid, 5.0)


class PrecombatScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.back1 = Template.Template(game, "返回", "./Precombat/Back.png")
        self.exercise = Template.Template(game, "演习", "./Precombat/Exercise.png")
        self.goNow = Template.Template(game, "立刻前往", "./Precombat/GoNow.png")
        self.goNow2 = Template.Template(game, "立刻前往2", "./Precombat/GoNow2.png")

        self.chapters = []
        self.chapters.append(Template.Template(game, "第1章", "./Precombat/Chapter01.png"))
        self.chapters.append(Template.Template(game, "第2章", "./Precombat/Chapter02.png"))
        self.chapters.append(Template.Template(game, "第3章", "./Precombat/Chapter03.png"))
        self.chapters.append(Template.Template(game, "第4章", "./Precombat/Chapter04.png"))
        self.chapters.append(Template.Template(game, "第5章", "./Precombat/Chapter05.png"))
        self.chapters.append(Template.Template(game, "第6章", "./Precombat/Chapter06.png"))
        self.chapters.append(Template.Template(game, "第7章", "./Precombat/Chapter07.png"))
        self.chapters.append(Template.Template(game, "第8章", "./Precombat/Chapter08.png"))
        self.chapters.append(Template.Template(game, "第9章", "./Precombat/Chapter09.png"))
        self.chapters.append(Template.Template(game, "第10章", "./Precombat/Chapter10.png"))
        self.chapters.append(Template.Template(game, "第11章", "./Precombat/Chapter11.png"))
        self.chapters.append(Template.Template(game, "第12章", "./Precombat/Chapter12.png"))

        self.subcapters = {}
        self.subcapters[100 * 1 + 1] = Template.Target(game, gc.Point(160, 376), gc.Size(114, 24))
        self.subcapters[100 * 3 + 4] = Template.Target(game, gc.Point(507, 306), gc.Size(137, 25))

        self.prevPageTarget = Template.Target(game, gc.Point(40, 300), gc.Size(25, 35))
        self.nextPageTarget = Template.Target(game, gc.Point(910, 300), gc.Size(25, 35))

    def back(self):
        self.click(self.back1)

    def enterExercise(self):
        self.click(self.exercise)

    def enterSubcapter(self, c, sc):
        time.sleep(5.0)
        curTarget, curChapter = self.matchList(self.chapters)
        if curTarget is None:
            print("获取海图章数失败。")
            return False
        curChapter += 1
        if c < curChapter:
            for i in range(curChapter - c):
                self.prevPageTarget.click()
                time.sleep(3.0)
        if c > curChapter:
            for i in range(c - curChapter):
                self.nextPageTarget.click()
                time.sleep(3.0)

        key = 100 * c + sc
        if key not in self.subcapters:
            print("{0}-{1}模板图片不存在。".format(c, sc))
            return False
        subcapterTarget = self.subcapters[key]
        subcapterTarget.click()
        self.click(self.goNow)
        self.click(self.goNow2)
        return True


class ExerciseScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.back1 = Template.Template(game, "返回", "./Exercise/Back.png")
        self.operation = Template.Template(game, "演习", "./Exercise/Operation.png")
        self.firstOne = Template.Target(game, gc.Point(50, 128), gc.Size(160, 228))
        self.startExercise = Template.Template(game, "开始演习", "./Exercise/StartExercise.png")
        self.weighAnchor = Template.Template(game, "出击", "./Exercise/WeighAnchor.png")

    def back(self):
        self.click(self.back1)

    def enterExercise(self):
        target = self.match(self.operation)
        if target is not None:
            self.firstOne.click()
        self.click(self.startExercise)
        self.click(self.weighAnchor)


class MaidScene(ExerciseScene):
    def __init__(self, game):
        super().__init__(game)
        self.advanced = Template.Template(game, "高级演习", "./Events/Advanced.png")

    def enterExercise(self):
        self.click(self.advanced)
        self.click(self.weighAnchor)


class C01S01Scene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.enterAmbushTarget = Template.Target(game, gc.Point(330, 252), gc.Size(87, 64))
        self.leaveAmbushTarget = Template.Target(game, gc.Point(238, 252), gc.Size(83, 64))
        self.meet = Template.Template(game, "迎击", "./Subchapter/Meet.png")
        self.weighAnchor = Template.Template(game, "出击", "./Subchapter/WeighAnchor.png")

    def enterAmbush(self):
        time.sleep(5.0)
        self.enterAmbushTarget.click()
        time.sleep(5.0)
        self.click(self.meet)
        self.click(self.weighAnchor)

    def leaveAmbush(self):
        time.sleep(5.0)
        self.leaveAmbushTarget.click()
        time.sleep(5.0)


class C03S04Scene(Scene):
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
        self.auto = Template.Template(game, "自律战斗", "./Battle/Auto.png")
        self.gotIt = Template.Template(game, "知道了", "./Battle/GotIt.png")
        self.ttc = Template.Template(game, "点击继续", "./Battle/TTC.png")
        self.ttc2 = Template.Template(game, "点击继续2", "./Battle/TTC2.png")
        self.performance = Template.Template(game, "性能", "./Battle/Performance.png")
        self.ok = Template.Template(game, "确定", "./Battle/OK.png")
        self.confirm = Template.Template(game, "确认", "./Battle/Confirm.png")
        self.autoFlag = False

    def enterBattle(self):
        if not self.autoFlag:
            if self.click(self.auto, 5.0):
                self.click(self.gotIt, 5.0)
            self.autoFlag = True

    def leaveBattle(self, drops=True):
        self.click(self.ttc)
        self.click(self.ttc2)
        if drops:
            if self.click(self.performance, 5.0):
                self.click(self.ok)
        self.click(self.confirm)
