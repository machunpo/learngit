import pyautogui as pyauto #这个库不支持中文目录和文件名
import time
import os
import random

loop_time=80                        #运行的次数
pyauto.PAUSE=1                      #每次pyauto的延时
pic_path='jdtest/pic/'              #图片的目录
flash_times=5                       #刷新的次数

def setup():
    print('屏幕分辨率：',pyauto.size())                                # 当前屏幕的分辨率
    print('当前目录  ：',os.getcwd() )

def run():
    if (pyauto.locateOnScreen( pic_path + 'sqsy.png' )):               # 申请试用
        pyauto.moveTo(pyauto.locateOnScreen( pic_path + 'sqsy.png' ))
        pyauto.click()
        pyauto.moveTo(10,10)                                           #移走150
    elif (pyauto.locateOnScreen( pic_path + 'bottom_null.png' )):      # button null
        for i in range(flash_times):
            pyauto.hotkey('f5')
            time.sleep(3)# 延时3秒，用来等待刷新页面
            if (pyauto.locateOnScreen( pic_path + 'sqsy.png' )):               # 申请试用
                pyauto.moveTo(pyauto.locateOnScreen( pic_path + 'sqsy.png' ))
                pyauto.click()
                pyauto.moveTo(10,10)
                break
            else:
                pass # pyauto.hotkey('ctrl','w')
        print('botton null')
        
    elif (pyauto.locateOnScreen( pic_path + 'genduoshiyong.png' )):    # 查看更多试用
        pyauto.hotkey('ctrl','w')                                      # 关闭标签
        print('查看更多试用')
    else:
        pass

    if (pyauto.locateOnScreen( pic_path + 'gzbsq.png' )):              # 关注并申请
        pyauto.moveTo(pyauto.locateOnScreen( pic_path + 'gzbsq.png' ))
        pyauto.click()
        pyauto.moveTo(10,150)
    else:
        pass

    if (pyauto.locateOnScreen( pic_path + 'sqcg.png' )):               # 申请成功
        pyauto.hotkey('ctrl','w')                                      # 关闭标签
    elif (pyauto.locateOnScreen( pic_path + 'wlwtsqsb.png' )):         # 网络问题申请失败
        pyauto.hotkey('ctrl','w')
        print('网络问题申请失败')
    elif (pyauto.locateOnScreen( pic_path + 'fwycqshzs.png' )):         # 服务异常请稍后再试
        pyauto.hotkey('ctrl','w')
        print('服务异常请稍后再试')
    else:
        pass#下一步  处理首页按钮显示不出来

    time.sleep(5)

if __name__ == '__main__':
    time.sleep(5)                  # 延时5秒，用来等待页面
    setup()
    for i in range(20):            # 循环执行20个页面
        run()



#下一步  处理首页按钮显示不出来   刷新3-4遍应该有效  也有可能一直刷不出来