import os
import time
from PIL import Image
import win32com.client as win
#pip install pypiwin32
speak = win.Dispatch("SAPI.SpVoice")  
speak.Rate=-1 
#增加语音播报的模块
loop_time=25

def put_page_up():
    os.system('adb shell input swipe 320 410 320 1000 500')  #//从 320 410 经历0.5秒滑动到 320 1000  手指向下滑

def put_page_down():
    os.system('adb shell input swipe 320 1000 320 410 500')  #//从 320 1000经历0.5秒滑动到 320 410   手指向上滑

def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/funtoutiao.png')
    os.system(r'adb pull /sdcard/funtoutiao.png  C:\Users\machunpo\Desktop\images')#./images

def check():
    os.system('adb shell input tap 240 460') 

def get_pixel_colour(image_path,x,y):
    img=Image.open(image_path)
    img_array=img.load()
    pixel_colour=img_array[x,y]
    img.close()
    return  pixel_colour

#检测adb连接是否有问题
#方法是发送一条adb命令，看看是否被执行,执行成功了会返回  Flase  。
def cheak_adb_link(order):
    return_txt=os.system(order)#执行成功了会返回0
    if return_txt != 0 :
        return True
    else:
        return False
        
def speak_and_print(command):
    print(command)
    speak.Speak(command)

if __name__ == '__main__':

    os.system('adb devices')

    for i in range(loop_time):
    

        if cheak_adb_link('adb shell input swipe 320 410 320 1000 500'):
            cmd='手机链接出问题了，重新链接一下把。手机链接出问题了，重新链接一下把。手机链接出问题了，重新链接一下把。'
            speak_and_print(cmd)
            break

        time.sleep(12)#等待顶部的更新条消失
        pull_screenshot()
        iskongbai=get_pixel_colour(r'C:\Users\machunpo\Desktop\images\funtoutiao.png',240,460)
        isdingwei=get_pixel_colour(r'C:\Users\machunpo\Desktop\images\funtoutiao.png',500,100)
        
        if iskongbai[0]==255 and isdingwei[0]==243:
            chengong_or_shibai='成功'
            check()
            for j in range(6):
                time.sleep(2)
                put_page_down()
                time.sleep(2)
            for j in range(5):
                time.sleep(2)
                put_page_up()
                time.sleep(2)
            os.system('adb shell input keyevent BACK') 
            time.sleep(5)
        else:
            chengong_or_shibai='失败'
            
            time.sleep(1)
            put_page_up()
            time.sleep(3)

        speak_and_print('循环共{}次，{}结束第{}次'.format(loop_time,chengong_or_shibai,i+1))

        print(iskongbai[0]==255 and isdingwei[0]==243)
        print(iskongbai[0])#255.255.255 255
        print(isdingwei[0])#(243, 247, 246, 255)
        #下面写逻辑
        #240   460
        #480   460
 
        #500   100
    speak_and_print('本次卫星发射圆满成功。')

    #下一次把参数传进函数
    #adb如何断开和链接
    
    