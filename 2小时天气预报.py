#!/usr/bin/python3
# -*- coding: utf-8 -*-
import urllib.request
back_up_url='http://caiyunapp.com/map/#120.4768,32.5131'        #这是彩云天气的短时间预报

#使用的是常州站的数据
url_of_pic='http://products.weather.com.cn/product/radar/index/procode/JC_RADAR_AZ9519_JB.shtml'




def extract(string_all,string_begin,string_end):  #提取数据的函数
    m=0;n=0;string_arry=[]
    while m!=-1 or n!=-1 :
        m=string_all.find(string_begin,n)
        n=string_all.find(string_end,m)
        try:
            string_arry.append(string_all[m+len(string_begin):n])
        except expression as identifier:
            pass
    return string_arry


response = urllib.request.urlopen(back_up_url)
content = response.read()#.decode('gbk', 'ignore')#打开要抓取的网页

print(content.decode('utf-8'))
print(back_up_url)
#extract(content,'begin','end')


#   问题：  为什么爬取的内容和查看源代码的内容不一样？  js加载的原因吗？