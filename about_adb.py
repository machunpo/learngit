#这是一个使用adb进行安卓手机控制的脚本，使用的编程语言是python
import os
import time
from PIL import Image

def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/funtoutiao.png')
    os.system(r'adb pull /sdcard/funtoutiao.png  C:\Users\machunpo\Desktop\images')#./images

def put_page_up():
    os.system('adb shell input swipe 320 410 320 1000 500')  #//从 320 410 经历0.5秒滑动到 320 1000

def put_page_down():
    os.system('adb shell input swipe 320 1000 320 410 500')  #//从 320 1000经历0.5秒滑动到 320 410


def jump(distance):
    press_time = distance * 1.35
    press_time = int(press_time)
    cmd = 'adb shell input swipe 320 410 320 410 ' + str(press_time)
    print(cmd)
    os.system(cmd)

def get_pixel_colour(image_path,x,y):
    img=Image.open(image_path)
    img_array=img.load()

    return  pixel_colour





if __name__ == '__main__':



    
    put_page_up()
    pull_screenshot()
    put_page_down()
    #下一步是取得点的颜色

       # img=Image.open(r'./images/下一页.png')
        #img_array=img.load()
        
        #print(img_array[5,5])
        #print(type(img_array))

        #for i in img_array[5,5]:
         #   print(i)
        














'''
以下是常用的adb命令。

用 ADB 工具获取当前手机截图，并用 ADB 将截图 pull 上来

adb shell screencap -p /sdcard/autojump.png
adb pull /sdcard/autojump.png

用 ADB 工具点击屏幕蓄力一跳
adb shell input swipe x y x y time(ms)

input swipe [duration(ms)]
向设备发送一个滑动指令，并且可以选择设置滑动时长。

//滑动操作

adb shell input swipe 100 100 200 200  300 //从 100 100 经历300毫秒滑动到 200 200

//长按操作

adb shell input swipe 100 100 100 100  1000 //在 100 100 位置长按 1000毫秒+

img=Image.open("demo.jpg")
img_array=img.load()

adb devices #确认已经连接

530，100  #关注的标志点

'''