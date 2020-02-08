#批量操作  1380  370
#全选      1210  375
#取消关注  1300  375
#确定     780   600
# 

import pyautogui as pyauto
import time
import os
import random

loop_time=10                    #运行的次数
pyauto.PAUSE=2                  #每次pyauto的延时
#count_none=0                        #标记空运行的次数
print(pyauto.size())                # 当前屏幕的分辨率

#path_pic_A=r'C:\Users\machunpo\Desktop\images\取消关注运行结束.png'                   

for i in range(loop_time):
    time.sleep(6)  # 延时6秒 用于开始的操作he刷新
    '''
    AA=pyauto.locateOnScreen(path_pic_A)
    if AA:
        print('程序运行结束')
        pyauto.move(100,100)
        break
'''
    pyauto.click(1380,370)#批量操作  1380  370
    pyauto.click(1210,375)#全选      1210  375
    pyauto.click(1300,375)#取消关注  1300  375
    pyauto.click(780,600)#确定     780   600



input()