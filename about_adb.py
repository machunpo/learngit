#这是一个使用adb进行安卓手机控制的脚本，使用的编程语言是python
import os
import time
from PIL import Image
import win32com.client as win #pip install pypiwin32

speak = win.Dispatch("SAPI.SpVoice")  #增加语音播报的模块
speak.Rate=-1 
delay_time=2

def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/funtoutiao.png')
    os.system(r'adb pull /sdcard/funtoutiao.png  C:\Users\machunpo\Desktop\images')#./images

def put_page_up():
    os.system('adb shell input swipe 320 410 320 1000 500')  #//从 320 410 经历0.5秒滑动到 320 1000  手指向下滑

def put_page_down():
    os.system('adb shell input swipe 320 1000 320 410 500')  #//从 320 1000经历0.5秒滑动到 320 410   手指向上滑

'''
def jump(distance):
    press_time = distance * 1.35
    press_time = int(press_time)
    cmd = 'adb shell input swipe 320 410 320 410 ' + str(press_time)
    print(cmd)
    os.system(cmd)
'''

def get_pixel_colour(image_path,x,y):
    img=Image.open(image_path)
    img_array=img.load()
    pixel_colour=img_array[x,y]
    img.close()
    return  pixel_colour
    
#检测adb连接是否有问题
#方法是发送一条adb命令，看看是否被执行。
def cheak_adb_link(order):
    return_txt=os.system(order)#执行成功了会返回0
    if return_txt != 0 :
        return True
    else:
        return False



if __name__ == '__main__':

    os.system('adb devices')


    for j in range(3):
        speak.Speak('好的，开始第{}次循环。'.format(j+1))
        #此处要增加adb是否连接的判断
        if cheak_adb_link('adb shell input swipe 320 410 320 1000 500'):
            speak.Speak('手机链接出问题了，重新链接一下把。')
            break
        for i in range(1):
            count=0
            a=53
            while(a==53):
                    put_page_up();time.sleep(delay_time);put_page_up();put_page_up()
                    pull_screenshot()
                    isguanzhu=get_pixel_colour(r'C:\Users\machunpo\Desktop\images\funtoutiao.png',530,100)
                    a=isguanzhu[0]
                    count=count+1
                    time.sleep(delay_time)

            print('swipe time is:',count)

            for i in range(count):
                put_page_down();put_page_down();time.sleep(delay_time);put_page_down()
                print('put page down.',i)
                time.sleep(delay_time)

            time.sleep(delay_time)
        os.system('adb shell input keyevent BACK')       #是🔙后退怎么搞

    speak.Speak('本次卫星回收任务圆满成功。')
 
        #下一步是简单版本


        



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

530，100  #关注的标志点 (53, 175, 93, 255)对比绿  (255, 255, 255, 255)白色

'''