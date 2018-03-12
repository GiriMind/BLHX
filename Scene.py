# coding: utf-8

import time

import Widget


class MainScene:
    def __init__(self, window):
        self.window = window
        self.windowImage = None
        self.formationButton = Widget.Button(window, "./Main/Formation.png")
        self.weighAnchorButton = Widget.Button(window, "./Main/WeighAnchor.png")

    def clear(self):
        self.windowImage = None
        self.formationButton.clear()
        self.weighAnchorButton.clear()

    def match(self, timeout=15):
        self.clear()
        print("正在匹配主场景……")
        beginTime = time.time()
        while True:
            if time.time() - beginTime > timeout:
                print("匹配主场景超时。")
                return False

            self.windowImage = self.window.capture()
            if self.windowImage is None:
                time.sleep(1)
                continue

            if not self.weighAnchorButton.isMatched():
                self.weighAnchorButton.matchOn(self.windowImage)
                if self.weighAnchorButton.isMatched():
                    print("匹配到出击按钮，相似度是{0}".format(self.weighAnchorButton.similarity))
                    return True

    def weighAnchor(self):
        if not self.weighAnchorButton.isMatched():
            self.weighAnchorButton.matchOn(self.windowImage)
            if not self.weighAnchorButton.isMatched():
                print("匹配不到出击按钮。")
                return False

        self.weighAnchorButton.click()
        print("进入出击场景。")

        self.clear()
        return True


class PrecombatScene:
    def __init__(self, window):
        self.window = window
        self.windowImage = None
        self.precombatWidget = Widget.Widget(window, "./Precombat/Precombat.png")
        self.prevChapterButton = Widget.Button(window, "./Precombat/PrevChapter.png", "./Precombat/PrevChapterMask.png")
        self.nextChapterButton = Widget.Button(window, "./Precombat/NextChapter.png", "./Precombat/NextChapterMask.png")
        self.chapter1Widget = Widget.Widget(window, "./Precombat/Chapter1.png")
        self.chapter2Widget = Widget.Widget(window, "./Precombat/Chapter2.png")
        self.chapter3Widget = Widget.Widget(window, "./Precombat/Chapter3.png")
        self.chapter4Widget = Widget.Widget(window, "./Precombat/Chapter4.png")
        self.chapter5Widget = Widget.Widget(window, "./Precombat/Chapter5.png")
        self.chapter6Widget = Widget.Widget(window, "./Precombat/Chapter6.png")
        self.chapter = 0

    def clear(self):
        self.windowImage = None
        self.precombatWidget.clear()
        self.prevChapterButton.clear()
        self.nextChapterButton.clear()
        self.chapter1Widget.clear()
        self.chapter2Widget.clear()
        self.chapter3Widget.clear()
        self.chapter4Widget.clear()
        self.chapter5Widget.clear()
        self.chapter6Widget.clear()
        self.chapter = 0

    def match(self, timeout=15):
        self.clear()
        print("正在匹配出击场景……")
        beginTime = time.time()
        while True:
            if time.time() - beginTime > timeout:
                print("匹配出击场景超时。")
                return False

            self.windowImage = self.window.capture()
            if self.windowImage is None:
                time.sleep(1)
                continue

            if not self.precombatWidget.isMatched():
                self.precombatWidget.matchOn(self.windowImage)
                if self.precombatWidget.isMatched():
                    print("匹配到出击标签，相似度是{0}".format(self.precombatWidget.similarity))
                    return True

    def prevChapter(self):
        if not self.prevChapterButton.isMatched():
            self.prevChapterButton.matchMaskOn(self.windowImage)
            if not self.prevChapterButton.isMatched():
                print("匹配不到上一章按钮。")
                return False

        self.prevChapterButton.click()
        print("进入上一章场景。")

        self.clear()
        return True

    def nextChapter(self):
        if not self.nextChapterButton.isMatched():
            self.nextChapterButton.matchMaskOn(self.windowImage)
            if not self.nextChapterButton.isMatched():
                print("匹配不到下一章按钮。")
                return False

        self.nextChapterButton.click()
        print("进入下一章场景。")

        self.clear()
        return True
