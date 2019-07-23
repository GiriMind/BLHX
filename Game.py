# coding: utf-8

import sys, os, time, random
import win32gui, win32process, win32con
import pyautogui
import cv2

sys.path.append(os.path.dirname(__file__))

import pyGraphCap as pygc

pyautogui.PAUSE = 2.5
pyautogui.FAILSAFE = True


def EnumFunc(window, lParam):
    windows = lParam
    if win32gui.IsWindowVisible(window):
        windows.append(window)


class Game:
    def __init__(self):
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
        # win32gui.SetWindowPos(self.window, None, 0, 0, 1280 + 14, 720 + 94, win32con.SWP_NOZORDER | win32con.SWP_NOMOVE)
        # win32gui.SetForegroundWindow(self.window)

        self.capturer = pygc.DesktopCapturer()
        self.buffer = pygc.Image()
        self.rect = pygc.Rect()

    def getWindowRect(self):
        left, top, right, bottom = win32gui.GetWindowRect(self.window)
        return (left, top, right, bottom)

    def getClientRect(self):
        left, top, right, bottom = win32gui.GetClientRect(self.window)
        left, top = win32gui.ClientToScreen(self.window, (left, top))
        right, bottom = win32gui.ClientToScreen(self.window, (right, bottom))
        return (left, top, right, bottom)

    def capture(self):
        while True:
            left, top, right, bottom = self.getWindowRect()
            # left, top, right, bottom = self.getClientRect()
            self.rect.x = left
            self.rect.y = top
            self.rect.width = right - left
            self.rect.height = bottom - top
            if not self.capturer.capture(self.buffer, self.rect):
                print("抓图失败：桌面没有变化导致超时，或者窗口位置超出桌面范围。")
                print("窗口位置：({0},{1})({2},{3})".format(left, top, right, bottom))
                continue
            return self.buffer.toNdarray()

    def mouseClick(self, pos, size=None):
        if size is None:
            x = self.rect.x + pos[0]
            y = self.rect.y + pos[1]
        else:
            x = self.rect.x + pos[0] + random.randint(0, size[0] - 1)
            y = self.rect.y + pos[1] + random.randint(0, size[1] - 1)
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
