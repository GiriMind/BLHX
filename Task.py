# coding: utf-8

import Scene


class C03S04Task:
    def __init__(self, window):
        self.window = window

    def run(self):
        precombat = Scene.PrecombatScene(self.window)
        c03s04 = Scene.C03S04Scene(self.window)
        battle = Scene.BattleScene(self.window)
        #while True:
        #    precombat.enterC03S04()
        #    while c03s04.bossExist:
        c03s04.enterBattle()
        #        battle.leaveBattle()
