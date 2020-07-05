import os
import time

import jrttkxs1

import aircv as ac
import win32com.client as win
from PIL import Image

#增加语音播报的模块
speak = win.Dispatch("SAPI.SpVoice")  
speak.Rate=-1 
#定义循环的次数
loop_time_xiaoshiping = 8
loop_time_video       = 8
loop_time_toutiao     = 7



loop_time_news=int(input('请输入要运行的次数：'))


def pull_screenshot():
        os.system('adb shell screencap -p /sdcard/funtoutiao.png')
        os.system(r'adb pull /sdcard/funtoutiao.png  C:\Users\machunpo\Desktop\myimages')

def put_page_up():
    os.system('adb shell input swipe 320 410 320 1000 500')  #//从 320 410 经历0.5秒滑动到 320 1000  手指向下滑

def put_page_down():
    os.system('adb shell input swipe 320 1000 320 410 500')  #//从 320 1000经历0.5秒滑动到 320 410   手指向上滑



#点击坐标x，y
def check(x,y):
    os.system('adb shell input tap '+str(x)+' '+str(y)) 

#获取图片的某个坐标的颜色
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

def play_video(t): #刷视频函数
    for i in range(t):
        check(216,1216)#点击视频
        time.sleep(5)
        check(359,306)#点击开始播放视频
        print('开始播放视频:',i)
        time.sleep(75)#延时75’
        check(621,1091)#点击彩蛋
        time.sleep(2)
        os.system('adb shell input keyevent BACK') 
        time.sleep(2)
    os.system('adb shell input keyevent BACK') 
    time.sleep(2)

#print and speak       
def speak_and_print(command):
    print(command)
    speak.Speak(command)

def is_frist_page():#判断是否首页 返回一个元组  就是点击的坐标
    a=get_pixel_colour(r'C:\Users\machunpo\Desktop\myimages\funtoutiao.png',115,92)  #得到一个元组 (0, 0, 0, 255)
    b=get_pixel_colour(r'C:\Users\machunpo\Desktop\myimages\funtoutiao.png',560,100)

    c=get_pixel_colour(r'C:\Users\machunpo\Desktop\myimages\funtoutiao.png',250,420)   #700
    d=get_pixel_colour(r'C:\Users\machunpo\Desktop\myimages\funtoutiao.png',470,420)   #700

    #e=get_pixel_colour(r'C:\Users\machunpo\Desktop\myimages\funtoutiao.png',240,700)   
    #f=get_pixel_colour(r'C:\Users\machunpo\Desktop\myimages\funtoutiao.png',480,700) 
    print('A B C D 的值是',a,b,c,d)
    

    if (a==(243, 247, 246, 255)) & (b==(243, 247, 246, 255)):#检测搜索栏的首页特征
        if (c==(255, 255, 255, 255)) & (d==(255, 255, 255, 255)):#检测图片中间的两条白色竖线
            #print('这是状态1')
            return (350,390)   #700

    else:
        return False

def let_us_go(a=1):
    for i in range(loop_time_news):
        print('')

        if cheak_adb_link('adb shell input swipe 320 410 320 1000 500'):
            os.system('adb kill-server')
            cmd='手机链接出问题了，重新链接了一下。'
            os.system('adb shell input keyevent BACK') 
            speak_and_print(cmd)
            time.sleep(10)
            os.system('adb shell input keyevent BACK') 

        time.sleep(5)
        check(72,1216)#点击刷新：72，1216
        time.sleep(5)#等待顶部的更新条消失
        check(72,1216)#点击刷新：72，1216
        time.sleep(7)#等待顶部的更新条消失
        pull_screenshot()     
        time.sleep(3)

        temp=is_frist_page()

        if temp:
            x,y=temp
            print('点击坐标：',x,y)
            zuobiao=True
        else:
            zuobiao=False

        if zuobiao:
            chengong_or_shibai='成功'
            check(x,y)#点击坐标
            for j in range(9):
                time.sleep(2)
                put_page_down()
                time.sleep(2)
                print(j,end=',')
            for j in range(8):
                time.sleep(2)
                put_page_up()
                time.sleep(2)
                print(j,end=',')
            check(621,1091)#这是点彩蛋吗？
            time.sleep(2)
            os.system('adb shell input keyevent BACK') 
            time.sleep(2)
            os.system('adb shell input keyevent BACK') 
            time.sleep(5)

        else:
            chengong_or_shibai='失败'
            time.sleep(1)
            os.system('adb shell input keyevent BACK') 
            time.sleep(3)
            os.system('adb shell input keyevent BACK') 
            time.sleep(1)
            put_page_up()
            time.sleep(3)

        #speak_and_print('共{}次，{}结束第{}次'.format(loop_time_news,chengong_or_shibai,i+1))
        time.sleep(5)
        os.system('adb shell input keyevent BACK')
        time.sleep(3)
        os.system('adb shell input keyevent BACK')  
        time.sleep(5)
        #################################  下面要插入寻找的代码

        pull_screenshot()
        imsrc = ac.imread(r'C:\Users\machunpo\Desktop\myimages\funtoutiao.png') # 原始图像 


        imsch2 = ac.imread(r'C:\Users\machunpo\Desktop\myimages\lingqu.png') # 带查找的部分 1 
        rult=ac.find_template(imsrc, imsch2)
        print(rult)
        if(rult):
            if rult['confidence']>0.91 :     #检测相似度  》0.91
                check(rult['result'][0],rult['result'][1])
                time.sleep(2)
                print('成功领取金币！')
            else:
                print('相似度有点低啊2！')
        else:
            print('没有找到金币！')

        speak_and_print('{}共{}次，{}结束第{}次'.format(a,loop_time_news,chengong_or_shibai,i+1))
        time.sleep(2)
        os.system('adb shell input keyevent BACK') 
        time.sleep(1)

def qiandao():#签到  点击任务图标
    check(505,1216)
    print('签到了')
    time.sleep(3)
    os.system('adb shell input keyevent BACK')
    

def shuaxiaoshiping(i):#刷小视频
    for j in range(i):
        check(300,1216)
        time.sleep(45)
        print('刷小视频的次数：',j)
    print('刷小视频')
    os.system('adb shell input keyevent BACK')
    



def jin_ri_tou_tiao():
    for i in range(loop_time_toutiao):
        check(73,1235)#点击首页进行刷新
        time.sleep(7)
        check(505,1235)#点击任务
        time.sleep(3)
        check(608,1141)#点击开宝箱得金币
        time.sleep(3)
        check(331,858)#点击看视频
        time.sleep(100)
        check(614,80)#点击关闭广告
        time.sleep(500)
        print('刷金币的次数：',i)
        check(73,1235)#点击首页进行刷新
        time.sleep(7)

def jrtt_kxs():   #头条看小说

    time.sleep(5)
    check(437,126)   #点击今日头条的图标启动app
    time.sleep(20)

    check(73,1235)#点击首页进行刷新
    time.sleep(5)
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



if __name__ == '__main__':

    os.system('adb devices')
    os.system('adb version')
    time.sleep(1)
    check(110,720)#点击图标
    time.sleep(60)#等待60秒

    qiandao()#签到
    time.sleep(2)
    #put_page_up()#添加一个下拉
    time.sleep(2)
    let_us_go()
    time.sleep(2)
    
    play_video(loop_time_video)#播放视频10分钟

    shuaxiaoshiping(loop_time_xiaoshiping)#刷小视频

    time.sleep(5)
    #check(648,1216) #点击我的图标
    time.sleep(5)






    time.sleep(2)
    os.system('adb shell input keyevent 3') #点击home键
    time.sleep(5)




    time.sleep(15)#增加两个程序切换之间的时间。
    check(270,720)#点击图标
    time.sleep(60)
    qiandao()#签到
    time.sleep(2)
    let_us_go(2)

    play_video(loop_time_video)

    shuaxiaoshiping(loop_time_xiaoshiping)#刷小视频

    time.sleep(5)

    


    time.sleep(2)
    os.system('adb shell input keyevent 3') #点击home键
    time.sleep(5)


    #今日头条刷金币

    kaishikanxiaoshuo=jrttkxs1.kan_xiao_shuo()

    kaishikanxiaoshuo.init()
    kaishikanxiaoshuo.jrtt_kxs()
    print('over please press enter')
    input()


    #time.sleep(2)
    #os.system('adb shell input keyevent 3') #点击home键
    #time.sleep(5)




#常用adb命令：
#adb shell input swipe 320 410 320 1000 500  #滑动
#adb shell input tap 100 200 #点击坐标

#adb shell input keyevent BACK   #后退键

#adb shell input keyevent 3    #模拟home按键 
# or adb shell input keyevent HOME

#adb shell input keyevent 82   #菜单键


#截屏并且传输到电脑
#adb shell screencap -p /sdcard/funtoutiao.png
#adb pull /sdcard/funtoutiao.png  C:\Users\machunpo\Desktop\myimages

#刷新：72，1216
#视频：216，1216
#小视频：360，1216
#任务：505，1216
#我的：648，1216

#不是竖条：102，100（变了）
#底色：560，100

#第二页的悬浮球：621，1091        这个位置是可以变化的


#在桌面上的位置 图标   y=720      x=110，270，450，？600

#白条的取点的位置     (250,420)     (470,420)




