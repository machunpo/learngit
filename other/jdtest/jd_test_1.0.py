import pyautogui as pyauto          #这个库不支持中文目录和文件名
import time
import os
import random

loop_time=100                        #运行的次数
pyauto.PAUSE=1                      #每次pyauto的延时
pic_path='jdtest/pic/'              #图片的目录

flash_times=0                        #刷新的次数
kill=0

flash_2times=1



def setup():  
    print('屏幕分辨率：',pyauto.size())                                    # 当前屏幕的分辨率
    print('当前目录  ：',os.getcwd() )
    print('loop time =',loop_time)
    print('pyauto.PAUSE =',pyauto.PAUSE)
    time.sleep(5)                                                         # 延时5秒，用来等待页面

def quxiao_guanzhu():

    if (pyauto.locateOnScreen( pic_path + 'wdjd.png' )):                  # 看看顶栏在不在

        pyauto.moveTo(880,110)              #移动到我的京东 停留两秒
        time.sleep(2)
        pyauto.click(1015,165)         #点击我的关注
        time.sleep(2)

        pyauto.click(482,256)   #点击我关注的店铺

        for i in range(8):
            time.sleep(6)  # 延时6秒 用于开始的操作he刷新

            pyauto.click(1380,370)#批量操作  1380  370
            pyauto.click(1210,375)#全选      1210  375
            pyauto.click(1300,375)#取消关注  1300  375
            pyauto.click(780,600)#确定     780   600
        
        pyauto.hotkey('ctrl','w')                                      # 关闭标签



    else:                                                     # 不在就刷新
        pyauto.hotkey('f5')




def end():
    
    pyauto.moveTo(500,800)
    print('程序结束')

def run():
    
    time.sleep(2)

    if (pyauto.locateOnScreen( pic_path + 'tstx.png' )):                  # 申请试用
        pyauto.moveTo(pyauto.locateOnScreen( pic_path + 'tstx.png' ))
        pyauto.click()
        pyauto.moveTo(10,10)                                              #移走10

    time.sleep(2)

    if (pyauto.locateOnScreen( pic_path + 'gzbsq.png' )):                 # 关注并申请
        pyauto.moveTo(pyauto.locateOnScreen( pic_path + 'gzbsq.png' ))
        pyauto.click()
        pyauto.moveTo(10,150)                                             #移走150

    time.sleep(2)

    if (pyauto.locateOnScreen( pic_path + 'sqcg.png' )):               # 申请成功

        pyauto.hotkey('ctrl','w')                                      # 关闭标签


    elif (pyauto.locateOnScreen( pic_path + 'genduoshiyong.png' )):    # 查看更多试用
        pyauto.hotkey('ctrl','w')                                      # 关闭标签
        print('查看更多试用')

    elif (pyauto.locateOnScreen( pic_path + 'kthy.png' )):             # 要求开通会员
        pyauto.hotkey('ctrl','w')
        print('要求开通会员')
    elif (pyauto.locateOnScreen( pic_path + 'app.png' )):              # 需要app进行申请
        pyauto.hotkey('ctrl','w')
        print('需要app进行申请')

    elif (pyauto.locateOnScreen( pic_path + 'zcg.png' )):              # 需要zcg进行申请
        pyauto.hotkey('ctrl','w')
        print('需要zcg进行申请')

    elif (pyauto.locateOnScreen( pic_path + 'sqsy.png' )):              # 特殊图形处理
        pyauto.moveTo(pyauto.locateOnScreen( pic_path + 'sqsy.png' ))
        pyauto.click()
        print('特殊图形处理')
        pyauto.moveTo(1000,810)

    elif (pyauto.locateOnScreen( pic_path + 'gzcglsx.png' )):              #关注超过了上限
        print('关注超过了上限')
        pyauto.hotkey('f5')
        quxiao_guanzhu()


    elif (pyauto.locateOnScreen( pic_path + 'weiguanzhu.png' )):              # 未关注

        pyauto.hotkey('f5')
        global flash_2times
        flash_2times=flash_2times+1
        print(flash_2times)
        if flash_2times > 3 :
            pyauto.hotkey('ctrl','w')
            print('刷了五次未关注')
            flash_2times=1

    else:
        pyauto.hotkey('f5')
        global flash_times
        flash_times=flash_times+1





if __name__ == '__main__':
    
    setup()

    print('setup is over！')
    for i in range(loop_time): 

            
        run()
        if flash_times > 5 :
            print('flash_times=', flash_times)
            flash_times=0
            print('刷新超过了5次，break')
            break


    end()

    #当前用户未关注

