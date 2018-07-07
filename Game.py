# coding: utf-8

import time
import random

import GraphCap as gc
import GraphCapCon as gcc


class Game:
    def __init__(self):
        # print("窗口列表：")
        # windowList = gc.Window.EnumWindows()
        # for i in range(len(windowList)):
        #    window = windowList[i]
        #    print("{0}.[{1}]{2}".format(i + 1, window.getPid(), window.getName()))
        # j = int(input("请输入窗口编号："))
        # self.window = windowList[j - 1]
        try:
            self.mainWindow = gc.Window.FindByName("BlueStacks")
            # self.pluginWindow = self.mainWindow.findChildByName("BlueStacks Android PluginAndroid")
            # self.appWindow = self.pluginWindow.findChildByName("_ctl.Window")
        except Exception as e:
            print("查找窗口失败，请先运行模拟器。")
            raise
        if self.mainWindow.isZoomed() or self.mainWindow.isIconic():
            self.mainWindow.restore()
        self.mainWindow.setSize(gc.Size(974, 634))
        self.capturer = gc.DesktopCapturer()
        self.image = gc.Image()
        self.image24 = gc.Image()
        self.rect = gc.Rect()
        self.input = gc.DesktopInput()

    def capture(self):
        while True:
            self.rect = self.mainWindow.getRect()
            # print("窗口位置：x={0}, y={1}, width={2}, height={3}".format(
            #    self.rect.x, self.rect.y, self.rect.width, self.rect.height))
            if not self.capturer.capture(self.image, self.rect):
                print("捕获图像失败，桌面超时未更新，或者窗口位置错误。")
                time.sleep(0.1)
                continue
            if self.image.getType() == gcc.IT_8UC3:
                return self.image
            else:
                self.image.cvtColor(self.image24, gcc.CCC_BGRA2BGR)
                return self.image24

    def click(self, location, size):
        x = self.rect.x + location.x + random.randint(0, size.width - 1)
        y = self.rect.y + location.y + random.randint(0, size.height - 1)
        self.input.setMousePos(gc.Point(x, y))
        self.input.mouseLeftDown()
        self.input.mouseLeftUp()
