import pyautogui as pyauto
import time
import os
import random

loop_time=80                        #运行的次数
pyauto.PAUSE=0.5                      #每次pyauto的延时
count_none=0                        #标记空运行的次数
time.sleep(3)                       # 延时5秒 用于开始的操作
sleep_time=1                        #set the time of sleep
guanzhu_count=0                     #统计用户未关注店铺的次数

print(pyauto.size())                # 当前屏幕的分辨率
current_directory=os.getcwd()       #获取当前目录
print(current_directory)
myimages_directory='\\myimages\\'       #定义图片目录

pic_A='A.png'       #申请试用            #定义识别的图片
pic_B='B.png'   	#关注并申请
pic_C='C.png'       #申请成功
pic_D='D.png'       #当前用户未关注店铺
pic_E='E.png'       #操作不要太快吆
pic_F='F.png'       #您的申请已经成功提交
pic_G='G.png'       #查看更多试用
pic_H='H.png'       #京东app申请
pic_I='I.png'       #您的申请次数已超过上线


path_pic_A=current_directory+myimages_directory+pic_A
path_pic_B=current_directory+myimages_directory+pic_B
path_pic_C=current_directory+myimages_directory+pic_C
path_pic_D=current_directory+myimages_directory+pic_D
path_pic_E=current_directory+myimages_directory+pic_E
path_pic_F=current_directory+myimages_directory+pic_F
path_pic_G=current_directory+myimages_directory+pic_G
path_pic_H=current_directory+myimages_directory+pic_H
path_pic_I=current_directory+myimages_directory+pic_I



for i in range(1):

    for i in range(loop_time):
        
        random_time_sec = random.randint(1,6) #随机产生一个时间
        
        AA=pyauto.locateOnScreen(path_pic_A)#申请试用
        if AA:
            pyauto.moveTo(pyauto.center(AA))
            pyauto.click()
            time.sleep(sleep_time)
        pyauto.moveTo(10,10)
        
        BB=pyauto.locateOnScreen(path_pic_B)#关注并申请
        if BB:
            pyauto.moveTo(pyauto.center(BB))
            pyauto.click()
            time.sleep(sleep_time)
        pyauto.moveTo(10,50)
        
        CC=pyauto.locateOnScreen(path_pic_C) #申请成功
        if CC :
            time.sleep(0.5)
            pyauto.hotkey('ctrl','w')         #关闭标签
            time.sleep(2)
            pyauto.moveTo(10,100)
        else:
            if pyauto.locateOnScreen(path_pic_G):
                time.sleep(0.5)
                pyauto.hotkey('ctrl','w')
                print('查看更多试用')
            elif pyauto.locateOnScreen(path_pic_D):
                time.sleep(0.5)
                pyauto.hotkey('f5')
                guanzhu_count=guanzhu_count+1
                if guanzhu_count>3:
                    print('超过3次了超过3次了')
                    guanzhu_count=0
                    pyauto.hotkey('ctrl','w')
                print('当前用户未关注店铺')
                
            elif pyauto.locateOnScreen(path_pic_F):
                time.sleep(0.5)
                pyauto.hotkey('ctrl','w')
                print('您的申请已经成功提交,请勿重复提交！')
            elif pyauto.locateOnScreen(path_pic_H):
                time.sleep(0.5)
                pyauto.hotkey('ctrl','w')
                print('this is need 京东app申请')
            elif pyauto.locateOnScreen(path_pic_I):
                print('您的申请次数已超过上线')
                break
            elif pyauto.locateOnScreen(path_pic_E):
                time.sleep(0.5)
                pyauto.hotkey('f5')
                print('操作不要太快吆')                
            else:
                count_none=count_none+1
                
        if count_none>3:
            print('空运行超过3次了')
            break

            
        pyauto.moveTo(10,150) #回到待命位置
        time.sleep(random_time_sec)
        print('第次{}运行'.format(i))
        print('random time is:',random_time_sec)


    print('game over.')


    #下一步要进行程序的重构
