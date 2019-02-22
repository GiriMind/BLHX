# coding: utf-8

import sys
import os
import time
import cv2

sys.path.append(os.path.dirname(__file__))

import pyGraphCap as gc

if __name__ == "__main__":
    capturer = gc.DesktopCapturer()
    image = gc.Image()
    rect = gc.Rect()
    beginTime = time.time()
    fps = 0
    while True:
        if not capturer.capture(image, rect):
            print("抓图失败：桌面没有变化导致超时，或者窗口位置超出桌面范围。")
            continue
        cv2.imshow("Test", image.toNdarray())
        cv2.waitKey(1)
        fps += 1
        if time.time() - beginTime > 1.0:
            beginTime += 1.0
            print(fps)
            fps = 0
