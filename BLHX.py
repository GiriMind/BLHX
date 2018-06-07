# coding: utf-8

import random

import GraphCap as gc
import Window
import Task


def BLHX():
    random.seed()

    window = Window.DesktopWindow()
    # while True:
    #    image = window.capture()
    #    if image is not None:
    #        image.show("test")
    #        gc.Utils.WaitKey(1)

    print("脚本开始。")
    task = Task.ExerciseTask(window)
    task.run()
    print("脚本结束。")


if __name__ == "__main__":
    BLHX()
