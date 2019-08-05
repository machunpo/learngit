# -*- coding:utf-8 -*-
#本程序 输出该城市十五天的天气预报
import urllib.request
import datetime
import win32com.client as win #pip install pypiwin32
import json
from my_def_lib import extract
import time
import _thread
import test.tts
import os

speak = win.Dispatch("SAPI.SpVoice")  #增加语音播报的模块
weekchn=['星期一','星期二','星期三','星期四','星期五','星期六','星期日','星期一','星期二','星期三','星期四','星期五','星期六','星期日','星期一','星期二','星期三','星期四','星期五','星期六','星期天']
url = 'https://tianqi.2345.com/haian/70445.htm'
al="，，，，，，，，"
speak.Rate=-1      #说话速度 -10到10
WANGZHIQIANZUI="http://www.mxnzp.com/api/holiday/single/"

def two_hour():

    back_up_url='https://api.caiyunapp.com/v2/96Ly7wgKGq6FhllM/120.4769,32.5131/weather.jsonp?hourlysteps=120'        #这是彩云天气的短时间预报
    jizhunshuju='这是用来比较是否更新的基础数据'
    i=1
    #使用的是常州站的数据
    #url_of_pic='http://products.weather.com.cn/product/radar/index/procode/JC_RADAR_AZ9519_JB.shtml'

    while(1):
        time.sleep(100)
        response = urllib.request.urlopen(back_up_url)
        content = response.read().decode('unicode_escape')#打开要抓取的网页

        new_dict = json.loads(content)
        tianqiyubao=new_dict["result"]["forecast_keypoint"]

        if tianqiyubao != jizhunshuju:

            #test.tts.hahaha(tianqiyubao) #测试百度云tts

            speak.Speak(tianqiyubao)     
            print('语音播报：',tianqiyubao)
            jizhunshuju=tianqiyubao
        else:
            print(tianqiyubao)
            print(i)
        #print(new_dict["result"]["minutely"]["description"])
        #import sys
        #print('目前系统的编码为：',sys.getdefaultencoding())
        #print('\\u672a\\u676524\\u5c0f\\u65f6\\u591a\\u4e91'.encode('latin-1').decode('unicode_escape'))
        i=i+1
        time.sleep(500)#延时函数，多少秒进行一次查询

try:
   _thread.start_new_thread(two_hour,())
   #_thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except TypeError as e:
   print (e)

while (True):
   
    d=datetime.date.weekday(datetime.date.today())         #添加星期几的功能

    hahhhh=weekchn[d]

    ldkkdj=datetime.datetime.now()
    ldkkdj=str(ldkkdj)[:19]   #  ldkkdj的实例化：2019-03-14  10:05:18

    year=ldkkdj[0:4];mon=ldkkdj[5:7];day=ldkkdj[8:10]

    wangzhi_api=WANGZHIQIANZUI+year+mon+day     #生成api的网址

    
    try:
        api_url = urllib.request.urlopen(wangzhi_api)
        content_apiurl = api_url.read()#.decode('gbk', 'ignore')
        new_dict = json.loads(content_apiurl)
        longliriqi=new_dict['data']['lunarCalendar']
           
        if '廿' in longliriqi:
            longliriqi=longliriqi.replace('廿','20')
        elif '卅' in longliriqi:
            longliriqi=longliriqi.replace('卅','30')
        else :
            pass

    except :
        longliriqi='api服务器故障，农历暂时无法播报'

    

    #本段代码用来增加农历日期的功能

    print()

    response = urllib.request.urlopen(url)
    content = response.read().decode('gbk', 'ignore')
    print(ldkkdj)
    b=content.find('<title>')
    e=content.find('一周')

    title=content[b+len('<title>'):e]


    content = str(extract(content,'<!-- /city_t -->','<!-- /有热词 begin -->'))

    riqi=extract(content,'<strong>','(')
    tianqi=extract(content,'<b>','</b>')
    low=extract(content,'<font class="blue">','</font>～')
    high=extract(content,'～<font class="red">','</font>')
    fenli=extract(content,'<br>','</i>')


    print('\n',title,'\n')
    for x in range(15):
        s=(str(fenli[x])).strip(r'<script type="text/javascript"></script>')
        #s = s.strip('<script type="text/javascript"></script>')
        s=s.strip(r"\n")
        qiwen=low[x]+'~'+high[x]
        #print(riqi[x].ljust(10),tianqi[x].ljust(15-len(tianqi[x])),qiwen.ljust(10),s.ljust(10))
        print(riqi[x].ljust(10), weekchn[d],'    ',tianqi[x].ljust(7,('　')),qiwen.ljust(10),s.ljust(10))
        d=d+1
    print('.'*40)

    yuyinbobao='今天是'+str(riqi[0])+'，'+hahhhh+'。'+'农历'+longliriqi+'。'+'天气'+str(tianqi[0])+'。'+'气温'+str(low[0])+'到'+str(high[0])
   
    

    if al=="，，，，，，，，":
        #test.tts.hahaha(yuyinbobao) #测试百度云tts
        #os.system('result.mp3')
        speak.Speak(yuyinbobao)
        jia='出门，要记得带，雨衣哦。'
        yi='出门，要记得带钞票哦。'
        jia1='出门，注意防寒和保暖啊。'
        jia2='出门，要记得涂防晒霜哦'

        if ('晴' in str(tianqi[0])):
            speak.Speak(jia2)
        elif('雨' in str(tianqi[0])):
            speak.Speak(jia)   
        elif('雪' in str(tianqi[0])):
            speak.Speak(jia1)
        else:
            speak.Speak(yi)     
    
    else:
        speak.Speak(al)

   
    al=input()+"，，，，，，，，"


    if al=='debug'+"，，，，，，，，":
        print("生成的api调用网址： ",wangzhi_api)
        print("由返回的json生成的词典： ",new_dict)
        print(type(new_dict))
        print("提取的农历信息：",longliriqi)
        print("生成的预报语音：",yuyinbobao)
        print("系统时间： ",ldkkdj)
        print("语音播报的速度： ",speak.Rate)

    if al=='exit'+"，，，，，，，，":
        break