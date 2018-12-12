# coding: utf-8

import random

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
            x = self.rect.x + pos.x
            y = self.rect.y + pos.y
        else:
            x = self.rect.x + pos.x + random.randint(0, size.width - 1)
            y = self.rect.y + pos.y + random.randint(0, size.height - 1)
        self.input.setMousePos(gc.Point(x, y))
        self.input.mouseLeftDown()
        self.input.mouseLeftUp()
