import os
import time
import aircv as ac


def check(zb):
    os.system('adb shell input tap ' + str(zb[0]) + ' ' + str(zb[1]))


class kan_xiao_shuo:
    '今日头条看小说'

    tu_biao    = (450, 720)   # 今日头条的图标 de坐标
    wo_de      = (657, 1224)  # 我的 de 坐标
    fen_mian   = (100, 973)   # 小说的封面 de坐标
    zhong_jian = (360, 650)   # 屏幕 de中间
    fan_ye     = (690, 80)    # 进行翻页 de的坐标
    ksp_ljb    = (350, 780)   #看视频再领金币  de的坐标
    imsch2     = ac.imread(r'qtoutiao\img\$.png')  # 带查找的部分

    def __init__(self): #构造函数
        pass

    def init(self):  # 初始化
        time.sleep(5)
        check(kan_xiao_shuo.tu_biao)  # 点击今日头条的图标启动app
        time.sleep(20)
        print('初始化已经完成。')

#############################################################################################################
    def jljc(self):#奖励检测

        os.system('adb shell screencap -p /sdcard/jinbi.png')
        os.system(r'adb pull /sdcard/jinbi.png  qtoutiao\img\ ') #下面要测试这条指令

        imsrc1 = ac.imread(r'qtoutiao\img\jinbi.png')  # 原始图像
        rult = ac.find_template(imsrc1, self.imsch2)  # 原始图像  ，   待查找的图像  
        if(rult):
            if rult['confidence'] > 0.9:
                time.sleep(3)
                check(self.ksp_ljb)  # 点击**看视频再领金币
                time.sleep(40)
                os.system('adb shell input keyevent BACK')
                print(rult)
            else:
                print('相似度有点低啊！')
        else:
            print('没有找到看视频按钮！')
######################################################################################################            

    def jrtt_kxs(self):  # 头条看小说

        time.sleep(5)
        print('开始头条看小说')
        check(kan_xiao_shuo.wo_de)  # 点击我的
        time.sleep(15)

        check(kan_xiao_shuo.fen_mian)  # 点击封面
        time.sleep(15)

        print('中间点一下。')
        check(kan_xiao_shuo.zhong_jian)  # 中间点一下
        time.sleep(2)

        # 点击看小说的循环
        for i in range(25):
            for j in range(15):
                check(kan_xiao_shuo.fan_ye)  # 点击进行翻页
                time.sleep(2)
            self.jljc()
            


if __name__ == "__main__":
    
    kaishikanxiaoshuo=kan_xiao_shuo()

    kaishikanxiaoshuo.init()
    kaishikanxiaoshuo.jrtt_kxs()

    #下一步是检测开头的升级提示  或者把手机上的升级给关了。