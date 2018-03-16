# coding: utf-8

import time

import Widget


class C03S04Task:
    def __init__(self, window):
        self.window = window
        self.delay = 2.0

    def run(self):
        c03s04Button = Widget.Button(self.window, "3-4按钮", "./Precombat/C03S04.png")
        if c03s04Button.match():
            c03s04Button.click()
            c03s04Button = None
            time.sleep(self.delay)
            lkqwButton = Widget.Button(self.window, "立刻前往按钮", "./Precombat/lkqw.png")
            if lkqwButton.match():
                lkqwButton.click()
                time.sleep(self.delay)
                if lkqwButton.match(0.98):
                    lkqwButton.click()
                    lkqwButton = None
                    time.sleep(self.delay)
