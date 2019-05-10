import urllib.request
import operator
import time
import win32com.client as win #pip install pypiwin32

speak = win.Dispatch("SAPI.SpVoice")  #增加语音播报的模块

def extract(string_all,string_begin,string_end):
    m=0;n=0;string_arry=[]
    while m!=-1 or n!=-1 :
            
        m=string_all.find(string_begin,n)
        n=string_all.find(string_end,m)
        try:
            string_arry.append(string_all[m+len(string_begin):n])
        except :
                pass

    return string_arry[:-1] #有个bug，最后一个数组元素内存溢出


def 获取最新地震信息():

    url = 'http://news.ceic.ac.cn'

    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8', 'ignore')


    提取的信息=extract(content,'<td align="center" style="padding-left: 20p','></td>')

    #['3.6', '2019-05-08 04:39:51', '37.37', '95.25', '9', '<a href="http://news.ceic.ac.cn/CD20190508043952.html">青海海西州直辖区']

    #震级(M) , 发震时刻(UTC+8) , 纬度(°) , 经度(°) , 深度(千米) , 参考位置

    msg_cls=[] #存储归类好的信息

    for i in 提取的信息:
    
        msg_cls.append(extract(i,'">','</'))
    '''
    for i in msg_cls:
        for j in i:
            print(j)
    '''
    最新信息=msg_cls[0]
    return(最新信息)

if __name__ == '__main__':

    print("地震实时播报系统")
    地震信息=[]
    #地震信息=获取最新地震信息()
    i=0#计数器
    delay=60#延时的时间
    
    while 1 :

        #print(获取最新地震信息())
        #地点=地震信息[5]
        #地点=地点[地点.find('>')+1:]
        #print(地点)
        
        i=i+delay
        print('系统运行{}秒'.format(i))

        if(operator.eq(地震信息,获取最新地震信息())):
            print('未接收到地震信息')
        else: 
            地震信息=获取最新地震信息()

            地点=地震信息[5]

            地点=地点[地点.find('>')+1:]

            print(地震信息)
            播报信息='最新播报:'+地震信息[1]+'秒在'+地点+'发生'+地震信息[0]+'级地震'
            speak.Speak(播报信息)
            continue

        time.sleep(delay)
		
		
		
		
		
		
		
		
		
'''
		
import requests,time
from lxml import etree
from wxpy import *
 
# 微信登陆
bot = Bot()
# 查找好友
group = bot.groups().search('珍爱生命 远离lisp')[0]  #写自己的讨论组名称
 
with open('log.txt', 'r') as f:
    rember = f.readline()
 
headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'cookie':'Hm_lvt_e0025cd5d352165f8a646ccea5beb27d=1543211803; Hm_lpvt_e0025cd5d352165f8a646ccea5beb27d=1543211803',
    }
 
while True:
    try:
        url = f'http://news.ceic.ac.cn/index.html?time={int(time.time())}'
        # 请求数据
        res = requests.get(url,headers = headers).text.encode('ISO-8859-1').decode('utf8')
        html_ele = etree.HTML(res)
        #返回列表
        res = html_ele.xpath('//*[@id="news"]//td//text()')
 
        # 如果日志为空,发送最新的一条地震信息
        if rember == '':
            msg = f'北京时间:{res[1]},在纬度:{res[2]} ,经度{res[3]} 处发生了{res[0]}级地震,震源深度{res[4]}千米,参考位置:{res[5]}(5分钟更新一次)'
            # 发送信息
            group.send(msg)
            print('日志为空,msg:', msg)
 
        # 如果日志非空,就判断是否是最新的,发送日志之后的所有新的数据
        else:
            i = res.index(rember)
            while i > 1:
                i -= 6
                msg = f'北京时间:{res[i]},在纬度:{res[i+1]} ,经度{res[i+2]} 处发生了{res[i-1]}级地震,震源深度{res[i+3]}千米,参考位置:{res[i+4]}(5分钟更新一次)'
                # 发送信息
                group.send(msg)
                print('日志非空,msg:',msg)
 
        time.sleep(300)
        rember = res[1]
        # 更新日志(记录最新发送的地震信息)
        with open('log.txt', 'w') as f:
            f.write(res[1])
    except:
        time.sleep(60)
--------------------- 
作者：1874445373@qq.com 
来源：CSDN 
原文：https://blog.csdn.net/qq_35515661/article/details/84557042 
版权声明：本文为博主原创文章，转载请附上博文链接！
''''''
		
		
		






