import pyautogui as pyauto
import time
import os
import pyperclip

is_next_page = True
next_page_Coordinates=(1071, 429)#下一页的坐标
count_Operation = 100
my_txt = '高手在当贝啊！学习了'

time.sleep(3)                       # 延时3秒 用于开始的操作

print(pyauto.size())                # 当前屏幕的分辨率

current_directory = os.getcwd()  # 获取当前目录
print(current_directory)
images_directory = '\\images\\'  # 定义图片目录

# 定义识别的图片的路径
path_pic_A = current_directory+images_directory+'下一页.png'
path_pic_B = current_directory+images_directory+'回复定位.png'
'''
path_pic_A=current_directory+images_directory+pic_A
path_pic_B=current_directory+images_directory+pic_B
path_pic_C=current_directory+images_directory+pic_C
path_pic_D=current_directory+images_directory+pic_D
path_pic_E=current_directory+images_directory+pic_E

'''
pyperclip.copy(my_txt)
pyauto.hotkey('ctrl', 'v')
time.sleep(2)
# 1.输入文本
pyauto.hotkey('ctrl', 'enter')
time.sleep(2)
# 2.Ctrl+enter
pyauto.press('tab')
time.sleep(2)
pyauto.press('home')
time.sleep(2)
# 这里可能要加一个tab和home
while is_next_page:
    A = pyauto.locateOnScreen(path_pic_A)  # ,grayscale=True???
    if A:
        is_next_page = False
        pyauto.moveTo(pyauto.center(A))
        time.sleep(1)
        pyauto.click(next_page_Coordinates)
        time.sleep(1)
    else:
        pyauto.hotkey('f5')
        time.sleep(10)
# 3.寻找下一页。png：没找到就延时和刷新
time.sleep(1)
# 4.点击最后一个按钮
pyauto.press('end')
time.sleep(1)  # ;print('end')
# 5.end
try:
    B = pyauto.locateOnScreen(path_pic_B)
    pyauto.click(B)
    time.sleep(1)
except:
    pyauto.move(10, 10)

# 6.点击输入框


# 下一步制造循环   呵呵呵
