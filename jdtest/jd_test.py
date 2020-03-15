import pyautogui as pyauto #这个库不支持中文目录
import time
import os
import random

loop_time=80                        #运行的次数
pyauto.PAUSE=0.5                    #每次pyauto的延时


def setup():
    print('屏幕分辨率：',pyauto.size())                # 当前屏幕的分辨率
    print('当前目录  ：',os.getcwd() )

def run():

    print(pyauto.locateOnScreen('jdtest\pic\A.png'))





if __name__ == '__main__':
    setup()
    run()



#解决相对路径的问题