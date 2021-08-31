
import os
import time


icon_one = (157 , 832)
icon_two = (411 , 832)

reban_y=300
reban_x=(560,690,820,955,1094,1240,1370,1500,1650,1782,1924,2045)

def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/todaytoutiao.png')
    os.system(r'adb pull /sdcard/todaytoutiao.png  C:\Users\machunpo\Desktop\myimages')

def push_page_left():
    
    os.system('adb shell input swipe 833 1258  258  1258 500')

def push_page_right():
    
    os.system('adb shell input swipe  258  1258 833 1258 500')

def put_page_up():
    # //从 320 410 经历0.5秒滑动到 320 1000  手指向下滑
    os.system('adb shell input swipe 320 410 320 1000 500')


def put_page_down():
    # //从 320 1000经历0.5秒滑动到 320 410   手指向上滑
    os.system('adb shell input swipe 320 1000 320 410 500')


# 点击坐标x，y
def check(x, y):
    os.system('adb shell input tap ' + str(x) + ' ' + str(y))


#刷抖音
def douyin_shua(x):
    for i in range(x):
        put_page_down()
        time.sleep(30)


if __name__ == '__main__':

    os.system('adb devices')
    os.system('adb version')
    os.system('adb shell input keyevent HOME')
    time.sleep(2)
    check(icon_one[0],icon_one[1])

    os.system('adb shell input keyevent BACK')
    time.sleep(4)
    os.system('adb shell input keyevent BACK')
    time.sleep(4)

    
    time.sleep(5)
    push_page_left()
    time.sleep(5)

    #pull_screenshot()

    for i in range(11):                                
        check(reban_y,reban_x[i])
        time.sleep(5)
        check(327,903)
        time.sleep(5)

        for i in range(13):
            put_page_down()
            time.sleep(10)

        os.system('adb shell input keyevent BACK')
        time.sleep(4)
        os.system('adb shell input keyevent BACK')
        time.sleep(4)

    #pull_screenshot()
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')






    check(750,2140)
    time.sleep(4)
    douyin_shua(30)
    os.system('adb shell input keyevent HOME')
    time.sleep(2)




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

#竖坐标 157    411   661    921
#横坐标 832   1123   1417   1699
