
import os
import time

import aircv as ac

imsch2 = ac.imread(r'C:\Users\machunpo\Desktop\myimages\$.png') # 带查找的部分

#点击坐标x，y
def check(x,y):
    os.system('adb shell input tap '+str(x)+' '+str(y)) 

#截屏并发送到电脑
def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/funtoutiao.png')
    os.system(r'adb pull /sdcard/funtoutiao.png  C:\Users\machunpo\Desktop\myimages')

def init():   #初始化
    time.sleep(5)
    check(450,720)   #点击今日头条的图标启动app
    time.sleep(20)

def bjtx():
    pull_screenshot()
    imsrc1 = ac.imread(r'C:\Users\machunpo\Desktop\myimages\funtoutiao.png') # 原始图像
    rult=ac.find_template(imsrc1, imsch2)#原始图像  ，   待查找的图像
    #print(rult)
    if(rult):
        if rult['confidence']>0.9 :
            check(360,1000)#点击按钮看视频（关闭界面）
            time.sleep(3)
            print(rult)
        else:
            print('相似度有点低啊！')
    else:
        print('没有找到看视频按钮！')

def jrtt_kxs():   #头条看小说
    time.sleep(5)
    os.system('adb shell input swipe 600 410 220 410 100')  #//从 600 410 经历0.1秒滑动到 220 410  手指向左滑
    time.sleep(5)
    os.system('adb shell input swipe 600 410 220 410 100')  #//从 600 410 经历0.1秒滑动到 220 410  手指向左滑
    time.sleep(5)
    #点击封面
    check(107,714)
    time.sleep(5)
    #点击看小说的循环
    for i in range(25):
        for j in range(15):
            check(690,80)#点击进行翻页
            time.sleep(2)
        bjtx()

        
'''        check(360,1000)#解决额外奖励的问题
        time.sleep(15)
        os.system('adb shell input keyevent BACK') 
        time.sleep(5)
'''
def get_out():
    os.system('adb shell input keyevent BACK') 

if __name__ == '__main__':
    init()
    jrtt_kxs()

    get_out()
    os.system('adb shell input keyevent BACK') 
    #可以正常使用了  