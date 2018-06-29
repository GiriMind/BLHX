# coding: utf-8

import Scene


class Task:
    def run(self):
        pass


class ExerciseTask(Task):
    def __init__(self, window):
        self.window = window

    def run(self):
        mainScene = Scene.MainScene(self.window)
        precombatScene = Scene.PrecombatScene(self.window)
        exerciseScene = Scene.ExerciseScene(self.window)
        mainScene.enterPrecombat()
        precombatScene.enterExercise()
        for i in range(5):
            exerciseScene.enterExercise()
            exerciseScene.leaveExercise()
        exerciseScene.back()
        precombatScene.back()


class C01S01LoopTask(Task):
    def __init__(self, window):
        self.window = window

    def run(self):
        mainScene = Scene.MainScene(self.window)
        precombatScene = Scene.PrecombatScene(self.window)
        #mainScene.enterPrecombat()
        #while True:
        precombatScene.enterSubcapter(1, 1)



class C03S04Task(Task):
    def __init__(self, window):
        self.window = window

    def run(self):
        # mainScene = Scene.MainScene(self.window)
        # precombatScene = Scene.PrecombatScene(self.window)
        c03s04Scene = Scene.C03S04Scene(self.window)
        # battleScene = Scene.BattleScene(self.window)
        # while True:
        #    precombatScene.enterC03S04()
        #    while c03s04Scene.bossExist:
        c03s04Scene.enterBattle()
        #        battleScene.leaveBattle()
