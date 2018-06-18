# coding: utf-8

import sys
import time


class Action:
    def __init__(self, window, template, threshold, timeout):
        self.window = window
        self.template = template
        self.threshold = threshold
        self.timeout = timeout

    def execute(self):
        pass


class ClickAction(Action):
    def __init__(self, window, template, threshold=0.98, timeout=sys.float_info.max, specifiedTarget=None):
        super().__init__(window, template, threshold, timeout)
        self.specifiedTarget = specifiedTarget

    def execute(self):
        beginTime = time.time()
        while time.time() - beginTime < self.timeout:
            image = self.window.capture()
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
