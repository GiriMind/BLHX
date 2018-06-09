# coding: utf-8

import time
import random

import GraphCap as gc
import Template


class Action:
    def __init__(self, window, template, threshold):
        self.window = window
        self.template = template
        self.threshold = threshold

    def execute(self):
        pass

    def sleep(self, min=1.0, max=2.0):
        time.sleep(random.uniform(min, max))


class ClickAction(Action):
    def __init__(self, window, template, threshold=0.98, specifiedTarget=None):
        super().__init__(window, template, threshold)
        self.specifiedTarget = specifiedTarget

    def execute(self):
        self.sleep()
        while True:
            image = self.window.capture()
            if image is not None:
                target = self.template.matchOn(image, self.threshold)
                if target is not None:
                    self.click(target)
                    break
            else:
                time.sleep(0.1)
        self.sleep()

    def click(self, target):
        if self.specifiedTarget is not None:
            self.specifiedTarget.click()
        else:
            target.click()
