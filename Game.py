# coding: utf-8

import time
import random
import cv2

import GraphCap as gc


class Game:
    def __init__(self):
        # print("窗口列表：")
        # windowList = gc.Window.EnumWindows()
        # for i in range(len(windowList)):
        #    window = windowList[i]
        #    print("{0}.[{1}]{2}".format(i + 1, window.getProcessId(), window.getName()))
        # j = int(input("请输入窗口编号："))
        # self.window = windowList[j - 1]
        try:
            self.mainWindow = gc.Window.FindByName("BlueStacks")
            self.pluginWindow = self.mainWindow.findChildByName("BlueStacks Android PluginAndroid")
            self.appWindow = self.pluginWindow.findChildByName("_ctl.Window")
        except Exception as e:
            print("查找游戏窗口失败，请先运行游戏。")
            raise
        if self.mainWindow.isMinimized() or self.mainWindow.isMaximized():
            self.mainWindow.restore()
        self.mainWindow.setSize(gc.Size(974, 634))
        self.capturer = gc.DesktopCapturer()
        self.buffer = gc.Image()
        self.rect = gc.Rect()
        self.input = gc.DesktopInput()

    def capture(self):
        while True:
            self.rect = self.mainWindow.getRect()
            if not self.capturer.capture(self.buffer, self.rect):
                # print("捕获图像失败，桌面超时未更新，或者窗口位置错误。")
                continue
            return self.buffer.toNdarray()

    def click(self, pos, size=None):
        if size is None:
            x = self.rect.x + pos[0]
            y = self.rect.y + pos[1]
        else:
            x = self.rect.x + pos[0] + random.randint(0, size[0] - 1)
            y = self.rect.y + pos[1] + random.randint(0, size[1] - 1)
        self.input.setMousePos(gc.Point(x, y))
        self.input.mouseLeftDown()
        self.input.mouseLeftUp()


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
