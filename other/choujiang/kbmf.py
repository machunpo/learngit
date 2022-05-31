import pyautogui as pyauto
import time
import pyperclip
import random

sj=['你好','很高兴认识你','我要中奖','今天天气真好','不错不错','great','好的真的很不错','为你点赞!']


while(1):
    pyperclip.copy(random(sj))
    pyauto.hotkey('ctrl', 'v')

    time.sleep(3)
    pyauto.hotkey('ctrl', 'enter')

    time.sleep(10)