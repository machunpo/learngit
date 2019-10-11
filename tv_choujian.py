import pyautogui as pyauto
import time
import os
import pyperclip


next_page_Coordinates = (1065, 429)  # 下一页的坐标
count_Operation = 100
my_txt = '高手在当贝啊！学习了'

time.sleep(3)                       # 延时3秒 用于开始的操作
print(pyauto.size())                # 当前屏幕的分辨率
is_next_page = True
current_directory = os.getcwd()  # 获取当前目录
print(current_directory)
images_directory = '\\images\\'  # 定义图片目录
# 定义识别的图片的路径
path_pic_A = current_directory+images_directory+'下一页.png'
path_pic_B = current_directory+images_directory+'回复定位.png'
print('pathB:',path_pic_B)
'''
path_pic_C=current_directory+images_directory+pic_C
path_pic_D=current_directory+images_directory+pic_D
path_pic_E=current_directory+images_directory+pic_E
'''

for i in range(count_Operation):
    # 1.输入文本
    pyperclip.copy(my_txt)
    pyauto.hotkey('ctrl', 'v')
    time.sleep(2)
    # 2.Ctrl+enter
    pyauto.hotkey('ctrl', 'enter')
    time.sleep(2)
    # 这里可能要加一个tab和home
    pyauto.press('tab')
    time.sleep(2)
    pyauto.press('home')
    time.sleep(2)
    # 3.寻找下一页。png：没找到就延时和刷新
    while is_next_page:
        A = pyauto.locateOnScreen(path_pic_A)
        if A:
            is_next_page = False
            pyauto.moveTo(pyauto.center(A))
            time.sleep(1)
            pyauto.click(next_page_Coordinates)# 4.点击最后一个按钮下一页的坐标
            time.sleep(1)
        else:
            # print('f5')
            pyauto.hotkey('f5')
            time.sleep(10)
    
    time.sleep(1)
    pyauto.press('end')
    time.sleep(1)  # ;print('end')
    pyauto.press('tab')
    # 5.end
    '''
    try:
        B = pyauto.locateOnScreen(path_pic_B)高手在当贝啊！学习了
        
        pyauto.click(B)
        time.sleep(1)
    except:
        pyauto.move(10, 10)
    '''
    # 6.点击输入框高手在当贝啊！学习了


    # 下一步制造循环   呵呵呵
