
import os
import time


def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/todaytoutiao.png')
    os.system(r'adb pull /sdcard/todaytoutiao.png  C:\Users\machunpo\Desktop\myimages')


def put_page_up():
    # //从 320 410 经历0.5秒滑动到 320 1000  手指向下滑
    os.system('adb shell input swipe 320 410 320 1000 500')


def put_page_down():
    # //从 320 1000经历0.5秒滑动到 320 410   手指向上滑
    os.system('adb shell input swipe 320 1000 320 410 500')


# 点击坐标x，y
def check(x, y):
    os.system('adb shell input tap ' + str(x) + ' ' + str(y))



if __name__ == '__main__':

    os.system('adb devices')
    os.system('adb version')
    time.sleep(1)
    pull_screenshot()
    os.system('adb shell input keyevent HOME')










# 常用adb命令：

# adb shell input swipe 320 410 320 1000 500  #滑动
# adb shell input tap 100 200 #点击坐标

# adb shell input keyevent BACK   #后退键

# adb shell input keyevent 3    #模拟home按键
# or adb shell input keyevent HOME


# adb shell input keyevent 82   #菜单键


# 截屏并且传输到电脑
# adb shell screencap -p /sdcard/funtoutiao.png
# adb pull /sdcard/funtoutiao.png  C:\Users\machunpo\Desktop\myimages