import pyautogui as pyauto
import time
import os

time.sleep(5)                       # 延时5秒 用于开始的操作

print(pyauto.size())                # 当前屏幕的分辨率

current_directory=os.getcwd()       #获取当前目录
print(current_directory)

images_directory='\\images\\'       #定义图片目录
pic_A=r'申请试用.png'                #定义识别的图片
pic_B=r''
pic_C=r''
pic_D=r''
pic_E=r''
pic_F=r''

path_pic_A=current_directory+images_directory+pic_A
print(path_pic_A)                                                  #当前目录\images\申请试用.png

A=pyauto.locateOnScreen(path_pic_A)
if A:
    print(A)
    x,y=pyauto.center(A)
    print(x,y)
    pyauto.moveTo(x,y)
    time.sleep(3)
    pyauto.click()

time.sleep(3)

#pyauto.locateOnScreen  的返回值是多少  从第二十3行开始写

