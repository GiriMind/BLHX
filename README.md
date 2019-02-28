# BLHX

基于图像识别的BLHX挂机脚本。

## 环境

Win8 64位或者以上，安装[VC++2017可再发行程序包](https://support.microsoft.com/zh-cn/help/2977003/the-latest-supported-visual-c-downloads)。

任意模拟器。

Python37便携版打包失败，需自行折腾。

安装Python37 64位，安装OpenCV`pip install opencv-python opencv-contrib-python`。

自行编译或者下载[xfeatures2d](https://github.com/GiriMind/BLHX/releases/download/0.0.6/xfeatures2d.7z)，覆盖至`Python37/Lib/site-packages/cv2/`。

下载脚本代码，下载[pyGraphCap](https://github.com/GiriMind/BLHX/releases/download/0.0.6/pyGraphCap.7z)，覆盖至`BLHX`根目录。

## 使用

进入游戏出击界面第3章。

运行`python 3-4.py`，选择游戏窗口。

保持游戏窗口在最前，不要被遮挡。
