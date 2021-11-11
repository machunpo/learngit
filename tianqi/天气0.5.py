# -*- coding:utf-8 -*-
import datetime
import json
import os
# import test.tts
import time
import urllib.request
from math import asin, cos, radians, sin, sqrt

import  sxtwl
lunar = sxtwl.Lunar()  #实例化日历库
#下面可以使用lunar做些日历的操作

import win32com.client as win  # pip install pypiwin32

import _thread
from my_def_lib import extract

speak = win.Dispatch("SAPI.SpVoice")  #增加语音播报的模块
speak.Rate=-1      #说话速度 -10到10

weekchn=['星期一','星期二','星期三','星期四','星期五','星期六','星期日','星期一','星期二','星期三','星期四','星期五','星期六','星期日','星期一','星期二','星期三','星期四','星期五','星期六','星期天']
url = 'https://tianqi.2345.com/haian/70445.htm'
al="，，，，，，，，"

#WANGZHIQIANZUI="http://www.mxnzp.com/api/holiday/single/"

ymc = ["十一", "腊", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十" ]
rmc = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十", "二十一", "二十二", "二十三", "二十四", "二十五", "二十六", "二十七", "二十八", "二十九", "三十", "卅一"]

def two_hour():

    back_up_url='https://api.caiyunapp.com/v2/96Ly7wgKGq6FhllM/120.4769,32.5131/weather.jsonp?hourlysteps=120'        #这是彩云天气的短时间预报
    jizhunshuju='这是用来比较是否更新的基础数据'
    i=1


    while(1):
        time.sleep(50)
        response = urllib.request.urlopen(back_up_url)
        content = response.read().decode('unicode_escape')#打开要抓取的网页

        new_dict = json.loads(content)
        tianqiyubao=new_dict["result"]["forecast_keypoint"]


        if tianqiyubao != jizhunshuju:
            h=time.gmtime()#取现在的时间 标准格林时间 0
            #test.tts.hahaha(tianqiyubao) #测试百度云tts
            #print('现在时间：',h)  #time.struct_time(tm_year=2019, tm_mon=12, tm_mday=17, tm_hour=6, tm_min=37, tm_sec=41, tm_wday=1, tm_yday=351, tm_isdst=0)
            if 3<h[3]<6 :
                #print('现在是免打扰时间。')
                pass
            else: 
                #print(tianqiyubao)   
                speak_and_print(tianqiyubao)
                print(str(datetime.datetime.now())[:19])
                #print('小时=',h[3])	
				
            
            jizhunshuju=tianqiyubao
        else:

            print(i,end=".")
			
			

        i=i+1
        time.sleep(300)#延时函数，多少秒进行一次查询



try:
   _thread.start_new_thread(two_hour,())
   # _thread.start_new_thread(dizhena, ())
except TypeError as e:
    print (e)

two_hour()