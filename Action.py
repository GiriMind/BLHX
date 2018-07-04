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
    def __init__(self, game, template, threshold=0.95, timeout=sys.float_info.max, specifiedTarget=None):
        super().__init__(game, template, threshold, timeout)
        self.specifiedTarget = specifiedTarget

    def execute(self):
        beginTime = time.time()
        while time.time() - beginTime < self.timeout:
            image = self.game.capture()
            target = self.template.matchOn(image)
            if target.similarity > self.threshold:
                self.click(target)
                return True
        return False

    def click(self, target):
        if self.specifiedTarget is not None:
            self.specifiedTarget.click()
        else:
            target.click()
