# coding: utf-8

import time

import Scene


class ChapterTask:
    def __init__(self, window, chapter, subChapter):
        self.window = window
        self.chapter = chapter
        self.subChapter = subChapter

    def run(self):
        mainScene = Scene.MainScene(self.window)
        if mainScene.match():
            if mainScene.weighAnchor():
                mainScene = None

                time.sleep(3)

                precombatScene = Scene.PrecombatScene(self.window)
                if precombatScene.match():
                    while True:
                        precombatScene.prevChapter()
