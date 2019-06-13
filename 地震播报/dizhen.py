#函数功能：提取一段特征文本中间的数据
#输入参数：string_all,string_begin,string_end整段文本，前后的关键词
#输出参数：string_arry 数组

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

#函数功能：去除一段特征文本中间的数据
#输入参数：string_all,string_begin,string_end整段文本，前后的关键词
#输出参数：一段文本

def quxhu_extract(string_all,string_begin,string_end):

    m = 0; n = 0
    m = string_all.find(string_begin)
    n = string_all.find(string_end)

    return string_all[:m]+string_all[n+len(string_end):]



import urllib.request
import time
import win32com.client as win #pip install pypiwin32

speak = win.Dispatch("SAPI.SpVoice")  #增加语音播报的模块
speak.Rate=-1      #说话速度 -10到10

#用于比较的变量
re_msg=''
 
headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'cookie':'Hm_lvt_e0025cd5d352165f8a646ccea5beb27d=1543211803; Hm_lpvt_e0025cd5d352165f8a646ccea5beb27d=1543211803',
    }

print('你好，欢迎使用地震播报系统。') 

while True:
    try:
        url = r'http://news.ceic.ac.cn/index.html'
        # 请求数据#print(url)
        response = urllib.request.urlopen(url=url)
        resp=response.read().decode('utf-8', 'ignore')
        
        #print(url)
        #print(resp)

        震级 = extract(resp,'<td align="center" style="padding-left: 20px">','</td>')#返回列表
        发震时刻 = extract(resp,'<td align="center" style="width: 155px;">','</td>')
        经纬深度 = extract(resp,'<td align="center">','</td>')
        参考位置 = extract(resp,'<td align="left">','</a></td>')

        #此处需要对参考位置进行处理  对其中的超链接进行清理
        参考位置 = [quxhu_extract(i,'<a href=','.html">') for i in 参考位置]
        
        #print(经纬深度)
        #print(参考位置)
        #兼容3.5版本
        msg = '北京时间:{}秒,{} 发生了{}级地震，经度{}，纬度{}，深度{}千米'.format(经纬深度[0],参考位置[0],震级[0],经纬深度[1],经纬深度[2],经纬深度[3])


        if msg==re_msg :
            pass
        else:
            re_msg=msg
            print(msg)
            speak.Speak(msg)

        print(int(time.time()))

        time.sleep(300)

    except:
        print('err form except')
        time.sleep(60)



        
        
        
 
 

		
		






