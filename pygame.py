import pyautogui as pyauto
import time
import os

time.sleep(5)                       # 延时5秒 用于开始的操作

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

path_pic_A=current_directory+images_directory+pic_A
path_pic_B=current_directory+images_directory+pic_B
path_pic_C=current_directory+images_directory+pic_C
path_pic_D=current_directory+images_directory+pic_D
path_pic_E=current_directory+images_directory+pic_E
path_pic_F=current_directory+images_directory+pic_F

for i in range(100):

    A=pyauto.locateOnScreen(path_pic_A)#申请试用
    
    if A:
        pyauto.moveTo(pyauto.center(A))
        time.sleep(2)
        pyauto.click()
    elif pyauto.locateOnScreen(path_pic_B):#关注并申请
        pyauto.moveTo(pyauto.center(pyauto.locateOnScreen(path_pic_B)))
        time.sleep(2)
        pyauto.click()
    else:
        if pyauto.locateOnScreen(path_pic_C): #申请成功
            time.sleep(2)
            pyauto.hotkey('ctrl','w')
        else:
             if pyauto.locateOnScreen(path_pic_D):#当前用户未关注店铺
                time.sleep(2)
                pyauto.hotkey('f5')
             else:              
                if pyauto.locateOnScreen(path_pic_E):#操作不要太快吆
                    time.sleep(2)
                    pyauto.hotkey('f5')
                elif pyauto.locateOnScreen(path_pic_F):#你的申请已成功提交
                    time.sleep(2)
                    pyauto.hotkey('ctrl','w')

       


    time.sleep(2)
    pyauto.moveTo(10,10) #回到待命位置
    time.sleep(2)
    
#下一步是要重构 1.改成列表 2.写成函数，根据输入的参数来进行操作

