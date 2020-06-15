
import os
import time

import aircv as ac

imsch2 = ac.imread(r'C:\Users\machunpo\Desktop\myimages\$.png')  # 带查找的部分

# 点击坐标x，y


def check(x, y):
    os.system('adb shell input tap ' + str(x) + ' ' + str(y))

# 截屏并发送到电脑


def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/funtoutiao.png')
    os.system(r'adb pull /sdcard/funtoutiao.png  C:\Users\machunpo\Desktop\myimages')


def init():  # 初始化
    time.sleep(5)
    check(450, 720)  # 点击今日头条的图标启动app
    time.sleep(20)
    print('初始化已经完成。')


def bjtx():

    pull_screenshot()
    imsrc1 = ac.imread(r'C:\Users\machunpo\Desktop\myimages\funtoutiao.png')  # 原始图像
    rult = ac.find_template(imsrc1, imsch2)  # 原始图像  ，   待查找的图像
    # print(rult)
    if(rult):
        if rult['confidence'] > 0.9:
            # check(360,1000)#点击按钮看视频（关闭界面）
            time.sleep(3)
            # os.system(r'adb pull /sdcard/funtoutiao.png  C:\Users\machunpo\Desktop')#把图片发到桌面，临时处理
            check(350, 780)  # 点击**看视频再领金币
            time.sleep(40)
            os.system('adb shell input keyevent BACK')
            print(rult)
        else:
            print('相似度有点低啊！')
    else:
        print('没有找到看视频按钮！')

def jrtt_kxs():  # 头条看小说
    time.sleep(5)
    print('开始头条看小说')

    check(657,1224) #点击我的
    time.sleep(15)
    check(100,973)# 点击封面
    time.sleep(15)
    print('中间点一下。')
    check(360, 650)  # 中间点一下
    time.sleep(2)
    # 点击看小说的循环
    for i in range(25):
        for j in range(15):
            check(690, 80)  # 点击进行翻页
            time.sleep(2)
        bjtx()


def get_out():
    os.system('adb shell input keyevent BACK')


# 函数功能：检查一个图片中是否包含另外一个图片
# 输入参数：img_arry  需要图片的列表 ['qtoutiao\img\pic1.png','qtoutiao\img\pic2.png']
# img_scr  原始图像
# 输出参数：一个列表 [None, {'result': (240.0, 446.0), 'rectangle': ((0, 332), (0, 560), (480, 332), (480, 560)), 'confidence': 1.0}]
#[{'result': (186.5, 917.5), 'rectangle': ((76, 880), (76, 955), (297, 880), (297, 955)), 'confidence': 0.6675431728363037}, {'result': (250.0, 425.0), 'rectangle': ((10, 311), (10, 539), (490, 311), (490, 539)), 'confidence': 0.519646167755127}]
def img_cheak(img_scr, img_arry):

    result_arry = []
    imgsrc = ac.imread(img_scr)  # 原始图像
    for i in img_arry:
        imgtort = ac.imread(i)
        rult = ac.find_template(imgsrc, imgtort)
        result_arry.append(rult)
        # print(ac.find_sift(img_scr,imgtort))

    return(result_arry)



def kai_baoxiang():

    time.sleep(10)
    # check(,)

    # 检测是不是第一次打开  图片检测
    pull_screenshot()
    '''img_arry=img_cheak(img_scr,img_arry);print(img_arry)
        if img_arry[0]:#这里做只有一个来考虑
            if img_arry[0]['confidence']>0.9:
                pass



'''

    time.sleep(10)
    # check(,)
    time.sleep(40)
    os.system('adb shell input keyevent BACK')

if __name__ == '__main__':

    init()  # 初始化

    # kai_baoxiang()#进行开宝箱的操作

    jrtt_kxs()

    get_out()
    os.system('adb shell input keyevent BACK')

    # kai_baoxiang()#进行开宝箱的操作

    # 下面开始开宝箱
    # 开头有个问题
    # 今日头条的常用坐标

    #桌面图标的坐标  (450,720)
    #
