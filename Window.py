# coding: utf-8

import random
import win32gui
import pyautogui

import GraphCap as gc
import GraphCapCon as gcc


class DesktopWindow:
    def __init__(self, name):
        self.hWnd = win32gui.FindWindow(None, name)
        if self.hWnd == 0:
            raise Exception("{0} 窗口未找到。".format(name))
        self.capturer = gc.DesktopCapturer()
        self.image = gc.Image()
        self.rect = gc.Rect()

    def capture(self):
        left, top, right, bottom = win32gui.GetWindowRect(self.hWnd)
        self.rect.x = left
        self.rect.y = top
        self.rect.width = right - left
        self.rect.height = bottom - top
        # print("窗口位置：x={0}, y={1}, width={2}, height={3}".format(
        #    self.rect.x, self.rect.y, self.rect.width, self.rect.height))
        if not self.capturer.capture(self.image, self.rect):
            print("捕获图像失败：桌面超时未更新，或者窗口位置错误。")
            return None
        if self.image.type() != gcc.CV_8UC4:
            raise Exception("图像格式错误：请将桌面设置为32位色。")
        # print("捕获位置：x={0}, y={1}, width={2}, height={3}".format(
        #    self.rect.x, self.rect.y, self.rect.width, self.rect.height))
        return self.image

    def click(self, location, size):
        x = self.rect.x + location.x + random.randint(0, size.width - 1)
        y = self.rect.y + location.y + random.randint(0, size.height - 1)
        pyautogui.moveTo(x, y)
        pyautogui.click()
