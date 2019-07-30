# coding: utf-8

import sys, os, time, random
import win32gui, win32process, win32con
import pyautogui
import cv2

sys.path.append(os.path.dirname(__file__))

import pyGraphCap as pygc

pyautogui.PAUSE = 2.0
pyautogui.FAILSAFE = True

DEFAULT_WIDTH = 960
DEFAULT_HEIGHT = 540


class Emulator:
    def __init__(self, name, leftBorder, topBorder, rightBorder, bottomBorder):
        self.name = name
        self.leftBorder = leftBorder
        self.topBorder = topBorder
        self.rightBorder = rightBorder
        self.bottomBorder = bottomBorder


def EnumFunc(window, lParam):
    windows = lParam
    if win32gui.IsWindowVisible(window):
        windows.append(window)


class Game:
    def __init__(self):
        # print("模拟器边框列表：")
        # emulators = []
        # emulators.append(Emulator("无边框", 0, 0, 0, 0))
        # emulators.append(Emulator("BlueStacks", 7, 47, 7, 47))
        # emulators.append(Emulator("scrcpy", 0, 0, 0, 0))
        # emulators.append(Emulator("其他模拟器请到Game.py添加，或者提交Issue/PR", 0, 0, 0, 0))
        # for i in range(len(emulators)):
        #    emulator = emulators[i]
        #    print("{0}.{1}({2},{3},{4},{5})".format(i + 1, emulator.name, emulator.leftBorder, emulator.topBorder,
        #                                            emulator.rightBorder, emulator.bottomBorder))
        # j = int(input("请输入模拟器边框编号："))
        # self.emulator = emulators[j - 1]
        print("窗口列表：")
        windows = []
        win32gui.EnumWindows(EnumFunc, windows)
        for i in range(len(windows)):
            window = windows[i]
            tid, pid = win32process.GetWindowThreadProcessId(window)
            print("{0}.[{1}]{2}".format(i + 1, pid, win32gui.GetWindowText(window)))
        j = int(input("请输入窗口编号："))
        self.window = windows[j - 1]
        # if win32gui.IsIconic(self.window):  # or win32gui.IsZoomed(self.window):
        # win32gui.ShowWindow(self.window, win32con.SW_RESTORE)
        # 1280 * 720, 960 * 540
        # win32gui.SetWindowPos(self.window, None, 0, 0, 960 + self.emulator.leftBorder + self.emulator.rightBorder,
        #                      540 + self.emulator.topBorder + self.emulator.bottomBorder,
        #                      win32con.SWP_NOZORDER | win32con.SWP_NOMOVE)
        # win32gui.SetForegroundWindow(self.window)

        self.capturer = pygc.DesktopCapturer()
        self.buffer = pygc.Image()
        self.rect = pygc.Rect()

    def _getWindowRect(self):
        left, top, right, bottom = win32gui.GetWindowRect(self.window)
        return (left, top, right, bottom)

    def _getClientRect(self):
        left, top, right, bottom = win32gui.GetClientRect(self.window)
        left, top = win32gui.ClientToScreen(self.window, (left, top))
        right, bottom = win32gui.ClientToScreen(self.window, (right, bottom))
        return (left, top, right, bottom)

    def capture(self):
        while True:
            # left, top, right, bottom = self._getWindowRect()
            left, top, right, bottom = self._getClientRect()
            self.rect.x = left
            self.rect.y = top
            self.rect.width = right - left
            self.rect.height = bottom - top
            # 裁剪边框
            # self.rect.x += self.emulator.leftBorder
            # self.rect.y += self.emulator.topBorder
            # self.rect.width -= (self.emulator.leftBorder + self.emulator.rightBorder)
            # self.rect.height -= (self.emulator.topBorder + self.emulator.bottomBorder)
            if not self.capturer.capture(self.buffer, self.rect):
                print("抓图失败：桌面没有变化导致超时，或者窗口位置超出桌面范围。")
                # print("窗口位置：({0},{1})({2},{3})".format(self.rect.x, self.rect.y, self.rect.width, self.rect.height))
                continue
            return self.buffer.toNdarray()
            # scene = self.buffer.toNdarray()
            # if self.rect.width == DEFAULT_WIDTH and self.rect.height == DEFAULT_HEIGHT:
            #    return scene
            # else:
            #    return cv2.resize(scene, (DEFAULT_WIDTH, DEFAULT_HEIGHT), interpolation=cv2.INTER_CUBIC)

    def mouseClick(self, pos, size=None):
        x = self.rect.x + pos[0]
        y = self.rect.y + pos[1]
        if size is not None:
            x += random.randint(0, size[0] - 1)
            y += random.randint(0, size[1] - 1)
        # x = x * self.rect.width / DEFAULT_WIDTH
        # y = y * self.rect.height / DEFAULT_HEIGHT
        pyautogui.click(x, y)


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
