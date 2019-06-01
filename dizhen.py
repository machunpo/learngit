import urllib.request
import time
from my_def_lib import extract

with open('log.txt', 'a+') as f:  #	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    f.seek(0, 0)   #指针移动到文件的开头
    rember = f.readline()



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

        # 如果日志为空,记录添加最新的一条地震信息
        if rember == '':
            
            for i in range(len(震级))  :
                
                msg = f'北京时间:{发震时刻[-i-1]},在纬度:{经纬深度[-i-1]} ,经度{经纬深度[-i-2]} 处发生了{震级[-i-1]}级地震,震源深度{经纬深度[-i-3]}千米,参考位置:{参考位置[-i-1]}(5分钟更新一次)'
                # 保存信息信息
                
                with open('log.txt', 'a+') as f:
                    f.write(msg+'\n')
                print('日志为空,msg:', msg)
        else:

            #已经有文件存在会进入这里
            '''
            i = res.index(rember)
            while i > 1:
                i -= 6
                msg = f'北京时间:{res[i]},在纬度:{res[i+1]} ,经度{res[i+2]} 处发生了{res[i-1]}级地震,震源深度{res[i+3]}千米,参考位置:{res[i+4]}(5分钟更新一次)'
                # 发送信息
                
                print('日志非空,msg:',msg) '''
            

        time.sleep(300)

    except:
        time.sleep(60)

'''

        
        
        
 
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
 
        
        rember = res[1]

            '''

		
		






