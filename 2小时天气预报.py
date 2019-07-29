#!/usr/bin/python3
# -*- coding: utf-8 -*-
import urllib.request
from my_def_lib import extract
back_up_url='https://api.caiyunapp.com/v2/96Ly7wgKGq6FhllM/120.4769,32.5131/weather.jsonp?hourlysteps=120'        #这是彩云天气的短时间预报

#使用的是常州站的数据
#url_of_pic='http://products.weather.com.cn/product/radar/index/procode/JC_RADAR_AZ9519_JB.shtml'

response = urllib.request.urlopen(back_up_url)
content = response.read()#打开要抓取的网页


print (content)


slashUStr = b"\\u0063\\u0072\\u0069\\u0066\\u0061\\u006E\\u0020\\u5728\\u8DEF\\u4E0A";    #crifan 在路上 

#decodedUniChars = slashUStr.decode("unicode-escape") 

print ("decodedUniChars=",slashUStr)   #decodedUniChars= crifan 在路上

#print (str1.decode('unicode-escape').encode('utf-8'))
#print (content.decode('raw_unicode-escape').encode('utf-8'))

#print(content)
#print(back_up_url)
#extract(content,'begin','end')


#   问题：  为什么爬取的内容和查看源代码的内容不一样？  js加载的原因吗？




import sys
print('目前系统的编码为：',sys.getdefaultencoding())
name='小明'
print(type(name))#首先我们来打印下转码前的name类型，因为它是str，所以可以通过encode来进行编码
name1=name.encode('utf-8')
print(name1)

input()
