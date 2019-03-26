
import json
import urllib.request

#函数功能：输入一个月份或者日期，如果小于10，则在其前面补齐0，用于月份或者日期的对齐
#输入参数：i 整形变量
#输出参数：l 字符串
def  checkTime(i):
    if (i < 10):
        l = "0" + str(i)  
    else:
        l=str(i)
    return l
    
#函数功能：通过彩云app获得本机IP地址（互联网）
#输入参数：无
#输出参数：无
def getip():
    url="https://caiyunapp.com/fcgi-bin/v1/geoip.py"
    response = urllib.request.urlopen(url)
    content = response.read().decode('gbk', 'ignore')
    new_dict = json.loads(content)
    print(new_dict)
    status=new_dict['status']
    ip=new_dict['ip']
    print(ip)


if __name__ == '__main__':
    getip()
    #num=10
    #print('num = ',checkTime(num))
    #print('num-1 = ',checkTime(num-1))
