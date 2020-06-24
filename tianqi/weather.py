# -*- coding:utf-8 -*-
import json
import time
import datetime
import urllib.request
import _thread
from my_def_lib import *
import win32com.client as win  # pip install pypiwin32
import  sxtwl
lunar = sxtwl.Lunar()  #实例化日历库

speak = win.Dispatch("SAPI.SpVoice")  #增加语音播报的模块
speak.Rate=-1      #说话速度 -10到10
url='https://tianqi.2345.com/haian/70445.htm'
ymc = ["十一", "腊", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十" ]
rmc = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十", "二十一", "二十二", "二十三", "二十四", "二十五", "二十六", "二十七", "二十八", "二十九", "三十", "卅一"]
weekchn=['星期一','星期二','星期三','星期四','星期五','星期六','星期日','星期一','星期二','星期三','星期四','星期五','星期六','星期日','星期一','星期二','星期三','星期四','星期五','星期六','星期天']

def weather_report():

    d=datetime.date.weekday(datetime.date.today())         #添加星期几的功能

    #print(d)

    hahhhh=weekchn[d]
    ldkkdj=datetime.datetime.now()
    ldkkdj=str(ldkkdj)[:19]   #  ldkkdj的实例化：2019-03-14  10:05:18
    year=ldkkdj[0:4];mon=ldkkdj[5:7];day=ldkkdj[8:10]
    this_day = lunar.getDayBySolar(int(year),int(mon),int(day))  # 查询2018年10月20日

    print("公历:", this_day.y, "年", this_day.m, "月", this_day.d, "日")

    if this_day.Lleap:
        longli="润"+ymc[this_day.Lmc]+"月"+rmc[this_day.Ldi]+"日"
        print('农历：',longli)
        new_longli=("润"+ymc[this_day.Lmc]+"月"+rmc[this_day.Ldi]+"日")
    else:
        longli=ymc[this_day.Lmc]+ "月"+ rmc[this_day.Ldi]+ "日"
        print('农历：',longli)
        new_longli=(ymc[this_day.Lmc]+"月"+rmc[this_day.Ldi]+"日")

    print(hahhhh)   #星期几




    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    #print(content)

    content=extract(content,'<a class="five-days-item work-bg" href="javascript:void(0)" >','<div class="ad-box">')
    #         #<a class="five-days-item work-bg" href="javascript:void(0)" > , <div class="ad-box">
    content=content[0]
    #print(content) 
    riqi=extract(content,r'<span class="day-date">','<em')
    tianqi=extract(content,'<em class="how-day">','</em>')
    wendu=extract(content,'<span class="tem-show">','</span>')
    fenli=extract(content,'<span class="home-day">','</span>')
    kongqizhilian=extract(content,'<span class="status wea','</span>')

    print('');print('');print('')

    for i in range(16):
        print(riqi[i],end="      ")
        print(weekchn[d-1],end="      ");d=d+1
        print(tianqi[i].ljust(16-len(tianqi[i])),end=" ")
        print(wendu[i].ljust(15),end=" ")
        print(fenli[i].ljust(18-len(fenli[i])),end=" ")

        if(kongqizhilian[i][-1:]=='度'):
            print(kongqizhilian[i][-2:]+'污染')
            
        else:
            print(kongqizhilian[i][-1:])
            

    if(kongqizhilian[1][-1:]=='度'):
        print12=(kongqizhilian[1][-2:]+'污染')        
    else:
        print12=(kongqizhilian[1][-1:])

    yuyinbobao='今天是'+str(riqi[1].replace('/','月'))+'日'+'。。'+hahhhh+'。。'+'农历：'+longli+'。。'+'天气' + str(tianqi[1]) +'。。  '+fenli[1]+'。。  '+'气温'+str(wendu[1].replace('~','到'))+'。。  '+'空气质量'+print12
    #print(yuyinbobao)
    speak.Speak(yuyinbobao)

    al=input()+"，，，，，，，，"
    if al=='debug'+"，，，，，，，，":
        print("debug")
        
    #if al=='exit'+"，，，，，，，，":
        #break



def two_hour():

    back_up_url='https://api.caiyunapp.com/v2/96Ly7wgKGq6FhllM/120.4769,32.5131/weather.jsonp?hourlysteps=120'        #这是彩云天气的短时间预报
    jizhunshuju='这是用来比较是否更新的基础数据'

    while(1):
        time.sleep(50)

        response = urllib.request.urlopen(back_up_url)
        content = response.read().decode('unicode_escape')#打开要抓取的网页
        new_dict = json.loads(content)
        tianqiyubao=new_dict["result"]["forecast_keypoint"]

        if tianqiyubao != jizhunshuju:
            h=time.gmtime()#取现在的时间 标准格林时间 0
            if 3<h[3]<6 :
                pass
            else: 
                print('')  
                speak.Speak(tianqiyubao)
                print(tianqiyubao)
                print(str(datetime.datetime.now())[:19])	

            jizhunshuju=tianqiyubao
        else:

            print('~',end=".")

        time.sleep(300)#延时函数，多少秒进行一次查询





if __name__ == '__main__':

    try:
        _thread.start_new_thread(two_hour,())

    except TypeError as e:
        print (e)    
   # _thread.start_new_thread(dizhena, ())
    while 1:

        weather_report()

    '''
    try:
        _thread.start_new_thread(weather_report)
    except:
        print ("Error: 无法启动线程")
        '''