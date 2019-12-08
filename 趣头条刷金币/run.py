import os
import time
from PIL import Image
import win32com.client as win
#pip install pypiwin32
speak = win.Dispatch("SAPI.SpVoice")  
speak.Rate=-1 
#增加语音播报的模块
loop_time_news=20
loop_time_video=10

def put_page_up():
    os.system('adb shell input swipe 320 410 320 1000 500')  #//从 320 410 经历0.5秒滑动到 320 1000  手指向下滑

def put_page_down():
    os.system('adb shell input swipe 320 1000 320 410 500')  #//从 320 1000经历0.5秒滑动到 320 410   手指向上滑

def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/funtoutiao.png')
    os.system(r'adb pull /sdcard/funtoutiao.png  C:\Users\machunpo\Desktop\images')#./images

def check():
    os.system('adb shell input tap 240 460') 

def dianji():
    os.system('adb shell input tap 80 1000') 

def get_pixel_colour(image_path,x,y):
    img=Image.open(image_path)
    img_array=img.load()
    pixel_colour=img_array[x,y]
    img.close()
    return  pixel_colour

def is_frist_page():#判断是否首页 返回一个元组  就是点击的坐标
    a=get_pixel_colour(r'C:\Users\machunpo\Desktop\images\funtoutiao.png',43,100)  #得到一个元组 (0, 0, 0, 255)
    b=get_pixel_colour(r'C:\Users\machunpo\Desktop\images\funtoutiao.png',570,100)

    c=get_pixel_colour(r'C:\Users\machunpo\Desktop\images\funtoutiao.png',240,1000)   
    d=get_pixel_colour(r'C:\Users\machunpo\Desktop\images\funtoutiao.png',480,1000) 

    e=get_pixel_colour(r'C:\Users\machunpo\Desktop\images\funtoutiao.png',240,700)   
    f=get_pixel_colour(r'C:\Users\machunpo\Desktop\images\funtoutiao.png',480,700) 
    

    if (a==(129, 140, 136, 255)) & (b==(243, 247, 246, 255)):#检测搜索栏的首页特征
        if (c==(255, 255, 255, 255)) & (d==(255, 255, 255, 255)):#检测图片中间的两条白色竖线
            print('这是状态1')
            return （350, 1000）
        elif (c==(255, 255, 255, 255)) & (d==(255, 255, 255, 255)):#检测图片中间的两条白色竖线
            print('这是状态2')
            return （350, 700）


        

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
    os.system('adb version')

    for i in range(loop_time_news):
    

        if cheak_adb_link('adb shell input swipe 320 410 320 1000 500'):
            os.system('adb devices')
            os.system('adb version')
            os.system('adb kill-server')
            #adb kill-server,adb start-server,
            cmd='手机链接出问题了，重新链接一下。'
            speak_and_print(cmd)
            #os.system('adb shell')
            os.system('adb shell input swipe 320 410 320 1000 500')
            

        time.sleep(12)#等待顶部的更新条消失
        pull_screenshot()
        iskongbai=get_pixel_colour(r'C:\Users\machunpo\Desktop\images\funtoutiao.png',240,460)

        isdingwei=get_pixel_colour(r'C:\Users\machunpo\Desktop\images\funtoutiao.png',500,100)

        iskongbai_again=get_pixel_colour(r'C:\Users\machunpo\Desktop\images\funtoutiao.png',238,975)
        iskongbai_again_2=get_pixel_colour(r'C:\Users\machunpo\Desktop\images\funtoutiao.png',480,892)
        
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

        elif iskongbai_again[0]==255 and  iskongbai_again_2[0]==255 :
            chengong_or_shibai='再次成功'
            dianji()
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
            os.system('adb shell input keyevent BACK') 
            time.sleep(1)
            put_page_up()
            time.sleep(3)

        speak_and_print('共{}次，{}结束第{}次'.format(loop_time_news,chengong_or_shibai,i+1))
        time.sleep(10)

        print(iskongbai[0]==255 and isdingwei[0]==243)
 
    #下面是刷视频
    os.system('adb shell input tap 216 1220') 

    for i in range(loop_time_video):
    

        if cheak_adb_link('adb shell input swipe 320 410 320 1000 500'):
            os.system('adb devices')
            os.system('adb version')
            os.system('adb kill-server')
            #adb kill-server,adb start-server,
            cmd='手机链接出问题了，重新链接一下。'
            speak_and_print(cmd)
            #os.system('adb shell')
            os.system('adb shell input swipe 320 410 320 1000 500')

        time.sleep(10)#等待顶部的更新条消失
        pull_screenshot()
        isbaishesanjiaoxin=get_pixel_colour(r'C:\Users\machunpo\Desktop\images\funtoutiao.png',355,305)

        if isbaishesanjiaoxin[0]==255 :
            os.system('adb shell input tap 355 305') 
            time.sleep(80)
            put_page_up()
            time.sleep(2)
        else:
            put_page_up()
            time.sleep(2)
            put_page_up()
            time.sleep(8)

        speak_and_print('共{}次，结束第{}次'.format(loop_time_video,i+1))

    speak_and_print('本次卫星发射圆满成功。')

    #下一次把参数传进函数
    
    
    