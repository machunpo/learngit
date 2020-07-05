import os
import time
#import math


def check(x,y):
    os.system(r'adb shell input tap '+str(x)+' '+str(y)) 



print('strat')

for i in range(120):
    check(1038,326)
    time.sleep(5)
    