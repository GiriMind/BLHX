# coding: utf-8

import win32gui
import pyautogui

import GraphCap as gc
import Image


class Window:
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
        if self.image.type() != Image.CV_8UC4:
            raise Exception("图像格式错误：请将桌面设置为32位色。")
        # print("捕获位置：x={0}, y={1}, width={2}, height={3}".format(
        #    self.rect.x, self.rect.y, self.rect.width, self.rect.height))
        return self.image

    def click(self, location, size):
        x = location.x + size.width / 2
        y = location.y + size.height / 2
        pyautogui.moveTo(self.rect.x + x, self.rect.y + y)
        pyautogui.click()
