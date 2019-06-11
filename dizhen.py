import urllib.request
import time
from my_def_lib import extract,quxhu_extract

re_msg=''

headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'cookie':'Hm_lvt_e0025cd5d352165f8a646ccea5beb27d=1543211803; Hm_lpvt_e0025cd5d352165f8a646ccea5beb27d=1543211803',
    }
print('你好') 
while True:
    try:
        url = 'http://news.ceic.ac.cn/index.html'
        # 请求数据#print(url)
        response = urllib.request.urlopen(url=url)
        resp=response.read().decode('utf-8', 'ignore')
        
        震级 = extract(resp,'<td align="center" style="padding-left: 20px">','</td>')#返回列表
        发震时刻 = extract(resp,'<td align="center" style="width: 155px;">','</td>')
        经纬深度 = extract(resp,'<td align="center">','</td>')
        参考位置 = extract(resp,'<td align="left">','</a></td>')

        #此处需要对参考位置进行处理  对其中的超链接进行清理
        参考位置 = [quxhu_extract(i,'<a href=','.html">') for i in 参考位置]
        
        #print(参考位置)

        msg = '北京时间:{},{} 发生了{}级地震，经度{}，纬度{}，深度{}千米'.format(发震时刻[0],参考位置[0],震级[0],经纬深度[0],经纬深度[1],经纬深度[2])
       

        if msg==re_msg :
            pass
        else:
            re_msg=msg
            print(msg)

        print(int(time.time()))

        time.sleep(300)

    except:
        time.sleep(60)



        
        
        
 
 

		
		






