import pyautogui as pyauto
import time
import os
import pyperclip

count_Operation = 3       #脚本运行的次数
my_txt = '高手在当贝啊！学习了'
how_sec_run_one_time=10   #多少秒运行一次
pyperclip.copy(my_txt)

next_page_Coordinates = (1065,429)  # 下一页的坐标
pyauto.PAUSE=2.5                    #每次进行操作后延时2.5秒
time.sleep(3)                       # 延时3秒 用于开始的操作
print(pyauto.size())                # 当前屏幕的分辨率

current_directory = os.getcwd()  # 获取当前目录
print(current_directory)
images_directory = '\\images\\'  # 定义图片目录
# 定义识别的图片的路径
path_pic_A = current_directory+images_directory+'下一页.png'

'''
path_pic_C=current_directory+images_directory+pic_C
path_pic_D=current_directory+images_directory+pic_D
path_pic_E=current_directory+images_directory+pic_E
'''

for i in range(count_Operation):

    is_next_page = True
    # 1.输入文本
    pyauto.hotkey('ctrl', 'v')
    pyauto.hotkey('enter')

    # 2.Ctrl+enter
    pyauto.hotkey('ctrl', 'enter')
    pyauto.hotkey('enter')

    # 这里可能要加一个tab和home
    pyauto.press('tab')
    pyauto.press('home')

    # 3.寻找下一页。png：没找到就延时和刷新
    while is_next_page:
        A = pyauto.locateOnScreen(path_pic_A)
        if A:
            is_next_page = False
            #pyauto.moveTo(pyauto.center(A))
            pyauto.click(next_page_Coordinates)# 4.点击最后一个按钮下一页的坐标
        else:
            pyauto.hotkey('f5')
            time.sleep(10)
    


    pyauto.hotkey('tab')



print('game over')    



