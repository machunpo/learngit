
import os
import time

import aircv as ac

#点击坐标x，y
def check(x,y):
    os.system('adb shell input tap '+str(x)+' '+str(y)) 

#截屏并发送到电脑
def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/funtoutiao.png')
    os.system(r'adb pull /sdcard/funtoutiao.png  C:\Users\machunpo\Desktop\myimages')

def init():   #初始化
    time.sleep(5)
    check(437,126)   #点击今日头条的图标启动app
    time.sleep(20)



def jrtt_kxs():   #头条看小说
    imsch2 = ac.imread(r'C:\Users\machunpo\Desktop\myimages\$.png') # 带查找的部分
#点击小说
    check(458,193)
    time.sleep(5)
#点击封面
    check(107,714)
    time.sleep(5)
#点击看小说的循环
    for i in range(25):
        for j in range(15):
            check(609,1125)#点击进行翻页
            time.sleep(2)

        pull_screenshot()
        imsrc1 = ac.imread(r'C:\Users\machunpo\Desktop\myimages\funtoutiao.png') # 原始图像
        rult=ac.find_template(imsrc1, imsch2)
        #print(rult)
        if(rult):
            if rult['confidence']>0.99 :
                #check(rult['result'][0],rult['result'][1])
                check(360,1000)#点击按钮看视频（关闭界面）
                time.sleep(3)
                #time.sleep(30)
                #print('看视频！')
                #os.system('adb shell input keyevent BACK') #这个地方要修改为那个关闭的东西

            else:
                print('相似度有点低啊！')
        else:
            print('没有找到看视频按钮！')
        
'''        check(360,1000)#解决额外奖励的问题
        time.sleep(15)
        os.system('adb shell input keyevent BACK') 
        time.sleep(5)
'''
if __name__ == '__main__':
    init()
    jrtt_kxs()

    #把检测变成函数
    #相似度有点低啊！