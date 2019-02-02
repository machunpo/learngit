# -*- coding:utf-8 -*-
#本程序 输入2345天气预报的城市网址，输出该城市十五天的天气预报
import urllib.request
import datetime


weekchn=['星期一','星期二','星期三','星期四','星期五','星期六','星期日','星期一','星期二','星期三','星期四','星期五','星期六','星期日','星期一','星期二','星期三','星期四','星期五','星期六','星期天']
print()
#ldkkdj=datetime.datetime.now()

print()
url = 'https://tianqi.2345.com/haian/70445.htm'
#url = 'http://tianqi.2345.com/nantong/58259.htm'

while (True):

    s=datetime.date.today()
    #print (s)
    d=datetime.date.weekday(s)         #添加星期几的功能
    #print(d)
    #print(weekchn[d])

    ldkkdj=datetime.datetime.now()
    ldkkdj=str(ldkkdj)[:19]
    print()
    response = urllib.request.urlopen(url)
    content = response.read().decode('gbk', 'ignore')
    print(ldkkdj)
    b=content.find('<title>')
    e=content.find('一周')

    title=content[b+len('<title>'):e]

    def extract(string_all,string_begin,string_end):
        m=0;n=0;string_arry=[]
        while m!=-1 or n!=-1 :
            
            m=string_all.find(string_begin,n)
            n=string_all.find(string_end,m)
            try:
                string_arry.append(string_all[m+len(string_begin):n])
            except expression as identifier:
                pass

        return string_arry

    content = str(extract(content,'<!-- /city_t -->','<!-- /有热词 begin -->'))

    riqi=extract(content,'<strong>','(')
    tianqi=extract(content,'<b>','</b>')
    low=extract(content,'<font class="blue">','</font>～')
    high=extract(content,'～<font class="red">','</font>')
    fenli=extract(content,'<br>','</i>')


    print('\n',title,'\n')
    for x in range(15):
        s=str(fenli[x])
        s = s.strip('<script type="text/javascript"></script>')
        s=s.strip(r"\n")
        qiwen=low[x]+'~'+high[x]
        #print(riqi[x].ljust(10),tianqi[x].ljust(15-len(tianqi[x])),qiwen.ljust(10),s.ljust(10))
        print(riqi[x].ljust(10), weekchn[d],'    ',tianqi[x].ljust(7,('　')),qiwen.ljust(10),s.ljust(10))
        d=d+1
    print('.'*40)
    al=input()
