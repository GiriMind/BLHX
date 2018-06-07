# coding: utf-8

import Scene


class ExerciseTask:
    def __init__(self, window):
        self.window = window

    def run(self):
        mainScene = Scene.MainScene(self.window)
        mainScene.enterPrecombat()
        precombatScene = Scene.PrecombatScene(self.window)
        precombatScene.enterExercise()
        exerciseScene = Scene.ExerciseScene(self.window)
        i = 5
        while i > 0:
            exerciseScene.enterExercise()
            exerciseScene.leaveExercise()
            i -= 1


class C03S04Task:
    def __init__(self, window):
        self.window = window

    def run(self):
        precombatScene = Scene.PrecombatScene(self.window)
        c03s04Scene = Scene.C03S04Scene(self.window)
        battleScene = Scene.BattleScene(self.window)
        #while True:
        #    precombatScene.enterC03S04()
        #    while c03s04Scene.bossExist:
        c03s04Scene.enterBattle()
        #        battleScene.leaveBattle()
