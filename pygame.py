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
pic_F=r'你的申请已成功提交'

path_pic_A=current_directory+images_directory+pic_A
path_pic_B=current_directory+images_directory+pic_B
path_pic_C=current_directory+images_directory+pic_C
path_pic_D=current_directory+images_directory+pic_D

for i in range(100):

    A=pyauto.locateOnScreen(path_pic_A)#申请试用
    if A:
        pyauto.moveTo(pyauto.center(A))
        time.sleep(2)
        pyauto.click()

    time.sleep(2)
      
    B=pyauto.locateOnScreen(path_pic_B)#关注并申请
    if B:
        pyauto.moveTo(pyauto.center(B))
        time.sleep(2)
        pyauto.click()

    time.sleep(2)


    C=pyauto.locateOnScreen(path_pic_C)#申请成功
    if C:
       
        time.sleep(2)
        pyauto.hotkey('ctrl','w')

    time.sleep(2)

    D=pyauto.locateOnScreen(path_pic_D)#当前用户未关注店铺
    if D:
       
        time.sleep(3)
        pyauto.hotkey('f5')

    time.sleep(2)

    pyauto.moveTo(10,10) #回到待命位置
    time.sleep(2)
    print('回到初始点')


