import os
import time
from PIL import Image
import win32com.client as win
#pip install pypiwin32
speak = win.Dispatch("SAPI.SpVoice")  
speak.Rate=-1 
#增加语音播报的模块

def put_page_up():
    os.system('adb shell input swipe 320 410 320 1000 500')  #//从 320 410 经历0.5秒滑动到 320 1000  手指向下滑

def put_page_down():
    os.system('adb shell input swipe 320 1000 320 410 500')  #//从 320 1000经历0.5秒滑动到 320 410   手指向上滑

#检测adb连接是否有问题
#方法是发送一条adb命令，看看是否被执行,执行成功了会返回  Flase  。
def cheak_adb_link(order):
    return_txt=os.system(order)#执行成功了会返回0
    if return_txt != 0 :
        return True
    else:
        return False


if __name__ == '__main__':

    os.system('adb devices')

    for i in range(20):
        if cheak_adb_link('adb shell input swipe 320 410 320 1000 500'):
            cmd='手机链接出问题了，重新链接一下把。'
            print(cmd)
            speak.Speak(cmd)


        #下面写逻辑