import urllib.request
import time
from my_def_lib import extract

<<<<<<< HEAD
with open('log.txt', 'r') as f:
    rember = f.readline()
 
=======
re_msg=''

>>>>>>> 70c384ed17645f6474e8ba90b5f287c73a60c657
headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'cookie':'Hm_lvt_e0025cd5d352165f8a646ccea5beb27d=1543211803; Hm_lpvt_e0025cd5d352165f8a646ccea5beb27d=1543211803',
    }
print('你好') 
while True:
    try:
<<<<<<< HEAD
        url = f'http://news.ceic.ac.cn/index.html?time={int(time.time())}'
        # 请求数据
        
=======
        url = 'http://news.ceic.ac.cn/index.html'
        # 请求数据#print(url)
>>>>>>> 70c384ed17645f6474e8ba90b5f287c73a60c657
        response = urllib.request.urlopen(url=url)
        resp=response.read().decode('utf-8', 'ignore')
        
        
        震级 = extract(resp,'<td align="center" style="padding-left: 20px">','</td>')#返回列表
        发震时刻 = extract(resp,'<td align="center" style="width: 155px;">','</td>')
        经纬深度 = extract(resp,'<td align="center">','</td>')
        参考位置 = extract(resp,'<td align="left">','</a></td>')

<<<<<<< HEAD

        # 如果日志为空,记录添加最新的一条地震信息
        if rember == '':
            for i in 震级:

                msg = f'北京时间:{发震时刻[i]},在纬度:{经纬深度[i]} ,经度{经纬深度[i+1]} 处发生了{震级[i]}级地震,震源深度{经纬深度[i+2]}千米,参考位置:{参考位置[i]}(5分钟更新一次)'
                # 保存信息信息

                print('日志为空,msg:', msg)
        else:
            i = res.index(rember)
            while i > 1:
                i -= 6
                msg = f'北京时间:{res[i]},在纬度:{res[i+1]} ,经度{res[i+2]} 处发生了{res[i-1]}级地震,震源深度{res[i+3]}千米,参考位置:{res[i+4]}(5分钟更新一次)'
                # 发送信息
                group.send(msg)
                print('日志非空,msg:',msg)

=======
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
>>>>>>> 70c384ed17645f6474e8ba90b5f287c73a60c657

        time.sleep(300)

    except:
        time.sleep(60)



        
        
        
 
 
<<<<<<< HEAD
        # 如果日志非空,就判断是否是最新的,发送日志之后的所有新的数据
        else:
            i = res.index(rember)
            while i > 1:
                i -= 6
                msg = f'北京时间:{res[i]},在纬度:{res[i+1]} ,经度{res[i+2]} 处发生了{res[i-1]}级地震,震源深度{res[i+3]}千米,参考位置:{res[i+4]}(5分钟更新一次)'
                # 发送信息
                group.send(msg)
                print('日志非空,msg:',msg)
 
        
        rember = res[1]
        # 更新日志(记录最新发送的地震信息)
        with open('log.txt', 'w') as f:
            f.write(res[1])
            '''
=======
>>>>>>> 70c384ed17645f6474e8ba90b5f287c73a60c657

		
		






