#打算使用和风天气api来实现
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'machunpo'

import requests
import time


mykey = '&key=ff4823599d******ed07fbbea3'
url_api = 'https://devapi.qweather.com/v7/weather/'
url_api_v2 = 'https://geoapi.qweather.com/v2/city/'

# 城市相关 api 调用 
def get_location(city):
    #url_v2 = 'https://geoapi.qweather.com/v2/city/lookup?location=101010100&key=cbe7ec6******************01d0d20'
    url_v2 = url_api_v2 +'lookup?location=' + city + mykey
    return requests.get(url_v2).json()

# 天气相关 api 调用
def get(api_type):
    # url = 'https://devapi.qweather.com/v7/weather/7d?location=101190502&key=cbe7ec6******************01d0d20'
    url = url_api + api_type + '?location=101190502'+ mykey
    #print(url)
    return requests.get(url).json()


weather_date = get('3d')

#print(weather_date['code'])
#print(weather_date['daily'])


for i in range(3):
    print(weather_date['daily'][i]['fxDate'] , weather_date['daily'][i]['tempMax'] , weather_date['daily'][i]['tempMin'] ,weather_date['daily'][i]['textDay'],weather_date['daily'][i]['windDirDay'] ,weather_date['daily'][i]['windScaleDay'])

