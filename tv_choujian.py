import pyautogui as pyauto
import time
import os
is_next_page=True

count_zhixin=100

time.sleep(3)                       # 延时3秒 用于开始的操作

print(pyauto.size())                # 当前屏幕的分辨率

current_directory = os.getcwd()  # 获取当前目录
print(current_directory)
images_directory = '\\images\\'  # 定义图片目录

# 定义识别的图片的路径
path_pic_A=current_directory+images_directory+'下一页.png'
'''
path_pic_A=current_directory+images_directory+pic_A
path_pic_B=current_directory+images_directory+pic_B
path_pic_C=current_directory+images_directory+pic_C
path_pic_D=current_directory+images_directory+pic_D
path_pic_E=current_directory+images_directory+pic_E
pyautogui
'''
pyauto.hotkey('ctrl','v');time.sleep(2)
#1.输入文本
pyauto.hotkey('ctrl','enter');time.sleep(2)
#2.Ctrl+enter
pyauto.press('tab');time.sleep(2)
pyauto.press('home');time.sleep(2)
#这里可能要加一个tab和home
while is_next_page:
    A=pyauto.locateOnScreen(path_pic_A)#,grayscale=True???
    if A:
        is_next_page=False
        pyauto.moveTo(pyauto.center(A))
        time.sleep(1)
        pyauto.click()
        time.sleep(1)
    else:
        pyauto.hotkey('f5')
        time.sleep(10)
#3.寻找下一页。png：没找到就延时和刷新
pyauto.click()
#4.点击最后一个按钮
pyauto.press('end');time.sleep(2)
#5.end
pyauto.click()
#6.点击输入框