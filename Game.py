# coding: utf-8

import sys
import os
import time
import random
import cv2

sys.path.append(os.path.dirname(__file__))

import pyGraphCap as gc


class Game:
    def __init__(self):
        print("窗口列表：")
        windowList = gc.Window.EnumWindows()
        for i in range(len(windowList)):
            window = windowList[i]
            print("{0}.[{1}]{2}".format(i + 1, window.getProcessId(), window.getName()))
        j = int(input("请输入窗口编号："))
        self.window = windowList[j - 1]
        # try:
        #    self.mainWindow = gc.Window.FindByName("BlueStacks")
        #    self.pluginWindow = self.mainWindow.findChildByName("BlueStacks Android PluginAndroid")
        #    self.appWindow = self.pluginWindow.findChildByName("_ctl.Window")
        # except Exception as e:
        #    print("查找游戏窗口失败，请先运行游戏。")
        #    raise
        if self.window.isMinimized() or self.window.isMaximized():
            self.window.restore()
        # self.window.setSize(gc.Size(1422 + 14, 800 + 94)) # 1422 * 800, 960 * 540
        self.window.foreground()

        self.capturer = gc.DesktopCapturer()
        self.buffer = gc.Image()
        self.rect = gc.Rect()
        self.input = gc.DesktopInput()
        self.pos = gc.Point()

    def capture(self):
        while True:
            self.rect = self.window.getRect()
            if not self.capturer.capture(self.buffer, self.rect):
                print("抓图失败：桌面没有变化导致超时，或者窗口位置超出桌面范围。")
                continue
            return self.buffer.toNdarray()

    def click(self, pos, size=None):
        if size is None:
            self.pos.x = self.rect.x + pos[0]
            self.pos.y = self.rect.y + pos[1]
        else:
            self.pos.x = self.rect.x + pos[0] + random.randint(0, size[0] - 1)
            self.pos.y = self.rect.y + pos[1] + random.randint(0, size[1] - 1)
        self.input.setMousePos(self.pos)
        self.input.mouseLeftPress()
        self.input.mouseLeftRelease()


if __name__ == "__main__":
    game = Game()
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
