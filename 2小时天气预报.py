#!/usr/bin/python3
# -*- coding: utf-8 -*-
import urllib.request

#使用的是常州站的数据
url_pic='http://products.weather.com.cn/product/radar/index/procode/JC_RADAR_AZ9519_JB.shtml'




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


response = urllib.request.urlopen(url_pic)
content = response.read().decode('gbk', 'ignore')#打开要抓取的网页

print(content)

#extract(content,'begin','end')