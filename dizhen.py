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






