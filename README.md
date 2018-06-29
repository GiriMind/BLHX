# BLHX

基于图像识别的碧蓝航线挂机脚本。

## 模拟器

推荐挂代理去[bluestacks.com](https://www.bluestacks.com/)下载原版的BlueStacks，使用[BSTweaker](https://forum.xda-developers.com/general/general/bluestacks-tweaker-2-tool-modifing-t3622681)关闭Google账号登录要求。

设置模拟器窗口分辨率为`974*634`，即游戏分辨率为`960*540`，以获得最佳的图像识别效果。

## 环境配置

安装Python3。

下载[OpenCV](https://github.com/opencv/opencv)，拷贝`opencv-3.4.1/build/x64/vc15/bin/opencv_world341.dll`到项目根目录。

下载[GraphCap](https://github.com/GiriMind/GraphCap)，拷贝`GraphCap.pyd`到项目根目录。

## 使用

1. 登录游戏到主界面。

2. 在项目根目录下执行`python BLHX.py`，运行脚本。

3. 输入标题为`BlueStacks`的窗口ID。

4. 输入任务ID。

## 已实现功能

1. 自动打演习。
