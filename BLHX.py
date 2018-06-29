# coding: utf-8

import random

import Window
import Task


def BLHX():
    random.seed()

    window = Window.DesktopWindow()

    print("任务列表：")
    print("1.自动打演习")
    print("2.1-1伏击炼金")
    print("3.自动捞吃喝")
    i = int(input("请输入任务编号："))
    if i == 1:
        task = Task.ExerciseTask(window)
    elif i == 2:
        task = Task.C01S01LoopTask(window)
    elif i == 3:
        task = Task.C03S04Task(window)
    else:
        task = None
    print("脚本开始。")
    task.run()
    print("脚本结束。")


if __name__ == "__main__":
    BLHX()
