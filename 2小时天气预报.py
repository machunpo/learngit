#!/usr/bin/python3
# -*- coding: utf-8 -*-
import urllib.request
import json
import time
from my_def_lib import extract

def two_hour():

    back_up_url='https://api.caiyunapp.com/v2/96Ly7wgKGq6FhllM/120.4769,32.5131/weather.jsonp?hourlysteps=120'        #这是彩云天气的短时间预报
    jizhunshuju='这是用来比较是否更新的基础数据'
    i=1
    #使用的是常州站的数据
    #url_of_pic='http://products.weather.com.cn/product/radar/index/procode/JC_RADAR_AZ9519_JB.shtml'

    while(1):

        response = urllib.request.urlopen(back_up_url)
        content = response.read().decode('unicode_escape')#打开要抓取的网页

        new_dict = json.loads(content)
        tianqiyubao=new_dict["result"]["forecast_keypoint"]

        if tianqiyubao != jizhunshuju:
            print(tianqiyubao)
            jizhunshuju=tianqiyubao
        else:
            pass
        
        print(i)
        #print(new_dict["result"]["minutely"]["description"])
        #import sys
        #print('目前系统的编码为：',sys.getdefaultencoding())
        #print('\\u672a\\u676524\\u5c0f\\u65f6\\u591a\\u4e91'.encode('latin-1').decode('unicode_escape'))
        i=i+1
        time.sleep(10)

if __name__ == '__main__':
    two_hour()