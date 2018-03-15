# coding: utf-8

import time

import Scene
import Widget


class C03S04Task:
    def __init__(self, window):
        self.window = window

    def run(self):
        c03s04Button = Widget.Button(self.window, "3-4按钮", "./Precombat/C03S04.png")
        if c03s04Button.match():
            c03s04Button.click()
