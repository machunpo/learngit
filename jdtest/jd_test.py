import pyautogui as pyauto #这个库不支持中文目录和文件名
import time
import os
import random

loop_time=80                        #运行的次数
pyauto.PAUSE=0.5                    #每次pyauto的延时
pic_path='jdtest/pic/'

def setup():
    print('屏幕分辨率：',pyauto.size())                # 当前屏幕的分辨率
    print('当前目录  ：',os.getcwd() )

def run():

    print(pyauto.locateOnScreen( pic_path + 'sqsy.png' ))





if __name__ == '__main__':
    setup()
    run()



#下一步图片更改成英文名字