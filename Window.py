# coding: utf-8

import random
import win32gui
import pyautogui

import GraphCap as gc
import GraphCapCon as gcc


class DesktopWindow:
    def __init__(self):
        # self.hWnd = win32gui.FindWindow(None, "BlueStacks")
        # if self.hWnd == 0:
        #    raise Exception("{0} 窗口未找到。".format("BlueStacks"))

        print("正在枚举窗口……")
        windowList = gc.Window.EnumWindows()
        for i in range(len(windowList)):
            window = windowList[i]
            print("{0}.[{1}]{2}".format(i + 1, window.getPid(), window.getName()))
        i = int(input("请输入窗口编号："))
        self.window = windowList[i - 1]

        self.capturer = gc.DesktopCapturer()
        self.image = gc.Image()
        self.rect = gc.Rect()

        self.input = gc.DesktopInput()

    def capture(self):
        # left, top, right, bottom = win32gui.GetWindowRect(self.hWnd)
        # self.rect.x = left
        # self.rect.y = top
        # self.rect.width = right - left
        # self.rect.height = bottom - top

        self.rect = self.window.getRect()

        # print("窗口位置：x={0}, y={1}, width={2}, height={3}".format(
        #    self.rect.x, self.rect.y, self.rect.width, self.rect.height))
        if not self.capturer.capture(self.image, self.rect):
            print("捕获图像失败：桌面超时未更新，或者窗口位置错误。")
            return None
        if self.image.getType() != gcc.IT_8UC4:
            raise Exception("图像格式错误：请将桌面设置为32位色。")
        # print("捕获位置：x={0}, y={1}, width={2}, height={3}".format(
        #    self.rect.x, self.rect.y, self.rect.width, self.rect.height))
        dsize = gc.Size(974, 634)
        if self.rect.width != dsize.width and self.rect.height != dsize.height:
            # print("调整捕获的图像大小至(974,634)。")
            dimage = self.image.resize(dsize)
            return dimage
        else:
            return self.image

    def click(self, location, size):
        x = self.rect.x + location.x + random.randint(0, size.width - 1)
        y = self.rect.y + location.y + random.randint(0, size.height - 1)
        # pyautogui.moveTo(x, y)
        # pyautogui.click()

        pos = gc.Point(x, y)
        self.input.mouseMove(pos)
        self.input.mouseLeftDown()
        self.input.mouseLeftUp()

    def getPid(self):
        return self.window.getPid()
