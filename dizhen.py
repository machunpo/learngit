import urllib.request
import time
from my_def_lib import extract,quxhu_extract

re_msg='北京时间:2019-06-09 01:36:28,辽宁朝阳市建平县 发生了3.2级地震'

headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'cookie':'Hm_lvt_e0025cd5d352165f8a646ccea5beb27d=1543211803; Hm_lpvt_e0025cd5d352165f8a646ccea5beb27d=1543211803',
    }
 
while True:
    try:
        url = f'http://news.ceic.ac.cn/index.html?time={int(time.time())}'
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

        msg = f'北京时间:{发震时刻[0]},{参考位置[0]} 发生了{震级[0]}级地震，经度{经纬深度[0]}，纬度{经纬深度[1]}，深度{经纬深度[2]}千米'

        if msg==re_msg :
            pass
        else:
            re_msg=msg
            print(msg)

        print(int(time.time()))

        time.sleep(300)

    except:
        time.sleep(60)



        
        
        
 
 

		
		






