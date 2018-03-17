# coding: utf-8

import time

import Widget


class PrecombatScene:
    def __init__(self, window):
        self.window = window
        self.delay = 2.0

    def enterC03S04(self):
        c03s04 = Widget.Button(self.window, "3-4按钮", "./Precombat/C03S04.png")
        if c03s04.match(0.98):
            c03s04.click()
            time.sleep(self.delay)
            lkqw = Widget.Button(self.window, "立刻前往按钮", "./Precombat/LKQW.png")
            if lkqw.match():
                lkqw.click()
                time.sleep(self.delay)
                if lkqw.match(0.98):
                    lkqw.click()
                    time.sleep(self.delay)


class C03S04Scene:
    def __init__(self, window):
        self.window = window
        self.delay = 2.0

    def enterBattle(self):
        enemyBB = Widget.Button(self.window, "主力舰队", "./SubChapter/EnemyBB.png", "./SubChapter/EnemyBBMask.png")
        if enemyBB.match():
            enemyBB.click()
            time.sleep(self.delay)
            weighAnchor = Widget.Button(self.window, "出击按钮", "./SubChapter/WeighAnchor.png")
            if weighAnchor.match():
                weighAnchor.click()
                time.sleep(self.delay)
