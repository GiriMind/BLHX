# coding: utf-8

import sys
import time


class Action:
    def __init__(self, game, template, threshold, timeout):
        self.game = game
        self.template = template
        self.threshold = threshold
        self.timeout = timeout

    def execute(self):
        pass


class ClickAction(Action):
    def __init__(self, game, template, threshold=0.95, timeout=sys.float_info.max, specifiedRect=None):
        super().__init__(game, template, threshold, timeout)
        self.specifiedRect = specifiedRect

    def execute(self):
        beginTime = time.time()
        while time.time() - beginTime < self.timeout:
            try:
                image = self.game.capture()
                target = self.template.matchOn(image)
                if target.similarity > self.threshold:
                    self.click(target)
                    return True
            except Exception as e:
                print(e)
        return False

    def click(self, target):
        if self.specifiedRect is not None:
            self.game.click(self.specifiedRect)
        else:
            self.game.click(target.getRect())
