#!/usr/bin/python3
# -*- coding: utf-8 -*-
import urllib.request
from my_def_lib import extract
back_up_url='http://caiyunapp.com/map/#120.4768,32.5131'        #这是彩云天气的短时间预报

#使用的是常州站的数据
url_of_pic='http://products.weather.com.cn/product/radar/index/procode/JC_RADAR_AZ9519_JB.shtml'

response = urllib.request.urlopen(back_up_url)
content = response.read()#.decode('gbk', 'ignore')#打开要抓取的网页

print(content.decode('utf-8'))
print(back_up_url)
#extract(content,'begin','end')


#   问题：  为什么爬取的内容和查看源代码的内容不一样？  js加载的原因吗？