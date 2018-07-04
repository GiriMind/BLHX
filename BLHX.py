# coding: utf-8

import sys
import os
import random

sys.path.append(os.path.dirname(__file__))

import Game
import Task


def BLHX():
    random.seed()
    game = Game.Game()
    print("任务列表：")
    print("1.打5次演习")
    print("2.1-1伏击刷好感度")
    print("3.3-4捞吃喝")
    i = int(input("请输入任务编号："))
    if i == 1:
        task = Task.ExerciseTask(game)
    elif i == 2:
        task = Task.C01S01LoopTask(game)
    elif i == 3:
        task = Task.C03S04Task(game)
    else:
        task = Task.Task(game)
    print("任务开始。")
    task.run()
    print("任务结束。")


if __name__ == "__main__":
    BLHX()
