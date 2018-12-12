# coding: utf-8

import sys
import os
import time
import cv2

sys.path.append(os.path.dirname(__file__))

import Game


def Test():
    game = Game.Game()
    beginTime = time.time()
    fps = 0
    while True:
        scene = game.capture()
        cv2.imshow("Test", scene)
        cv2.waitKey(1)
        fps += 1
        if time.time() - beginTime > 1.0:
            beginTime += 1.0
            print(fps)
            fps = 0


if __name__ == "__main__":
    Test()
