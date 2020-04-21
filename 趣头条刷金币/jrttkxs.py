
import os
import time

#点击坐标x，y
def check(x,y):
    os.system('adb shell input tap '+str(x)+' '+str(y)) 


def init():   #初始化
    time.sleep(5)
    check(437,126)   #点击今日头条的图标启动app
    time.sleep(20)


def jrtt_kxs():   #头条看小说

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
    init()
    jrtt_kxs()

    #解决额外奖励影响运行的问题