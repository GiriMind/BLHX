# coding: utf-8

import Scene


class C03S04Task:
    def __init__(self, window):
        self.window = window

    def run(self):
        precombatScene = Scene.PrecombatScene(self.window)
        precombatScene.enterC03S04()
        c03s04Scene = Scene.C03S04Scene(self.window)
        c03s04Scene.enterBattle()
