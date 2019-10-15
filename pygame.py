import pyautogui as pyauto
import time
import os

time.sleep(3)                       # 延时3秒 用于开始的操作
pyauto.PAUSE=1

print(pyauto.size())                # 当前屏幕的分辨率

current_directory=os.getcwd()       #获取当前目录
print(current_directory)
images_directory='\\images\\'       #定义图片目录

pic_A=r'申请试用.png'                #定义识别的图片
pic_B=r'关注并申请.png'
pic_C=r'申请成功.png'
pic_D=r'当前用户未关注店铺.png'
pic_E=r'操作不要太快吆.png'
pic_F=r'你的申请已成功提交.png'
pic_G=r'申请次数超过上限.png'
pic_H=r'查看更多试用.png'


path_pic_A=current_directory+images_directory+pic_A
path_pic_B=current_directory+images_directory+pic_B
path_pic_C=current_directory+images_directory+pic_C
path_pic_D=current_directory+images_directory+pic_D
path_pic_E=current_directory+images_directory+pic_E
path_pic_F=current_directory+images_directory+pic_F
path_pic_H=current_directory+images_directory+pic_H

for i in range(200):

    
    A=pyauto.locateOnScreen(path_pic_A)#申请试用
    if A:
        pyauto.moveTo(pyauto.center(A))
        pyauto.click()
        pyauto.press('numlock')

    
    B=pyauto.locateOnScreen(path_pic_B)
    if B:#关注并申请
        pyauto.moveTo(pyauto.center(B))
        pyauto.click()
        pyauto.press('numlock')

        
    C=pyauto.locateOnScreen(path_pic_C)
    if C: #申请成功
            
        pyauto.hotkey('ctrl','w')
        pyauto.press('numlock')
    else:
        if pyauto.locateOnScreen(path_pic_D):#当前用户未关注店铺
                
            pyauto.hotkey('f5')
                
        else:              
            if pyauto.locateOnScreen(path_pic_E):#操作不要太快吆
                    
                pyauto.hotkey('f5')
                    
            elif pyauto.locateOnScreen(path_pic_F):#你的申请已成功提交
                    
                pyauto.hotkey('ctrl','w')
                    
            elif pyauto.locateOnScreen(path_pic_H):#查看更多试用
                    
                pyauto.hotkey('ctrl','w')
       


  
    pyauto.moveTo(10,10) #回到待命位置
  
    
print('game over.')

#下一步是要重构 1.改成列表 2.写成函数，根据输入的参数来进行操作

