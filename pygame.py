import pyautogui as pyauto
import time

time.sleep(5)  #   延时5秒 用于开始的操作
print(pyauto.size())

path_pic=r'C:\Users\zyf\Desktop\新建文件夹\申请试用.png'


o=pyauto.locateOnScreen(path_pic)
if o:
    print(o)

    x,y=pyauto.center(o)

    print(x,y)
    pyauto.moveTo(x,y)
    time.sleep(3)
    pyauto.click()

time.sleep(3)

#对流程进行规划

