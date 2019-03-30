
#函数功能：输入一个月份或者日期，如果小于10，则在其前面补齐0，用于月份或者日期的对齐
#输入参数：i 整形变量
#输出参数：l 字符串
def  checkTime(i):
    if (i < 10):
        l = "0" + str(i)  
    else:
        l=str(i)
    return l


import json
import urllib.request


#函数功能：通过彩云app获得本机IP地址（互联网）经纬度坐标，城市，返回状态等
#输入参数：无
#输出参数：无
def getip():
    url="https://caiyunapp.com/fcgi-bin/v1/geoip.py"
    response = urllib.request.urlopen(url)
    content = response.read().decode('gbk', 'ignore')
    new_dict = json.loads(content)
    #print(new_dict)
    
    status=new_dict['status']
    center=new_dict['center']
    city=new_dict['city']
    ip=new_dict['ip']

    print('status:',status)
    print('ip:',ip)
    print('center:',center)
    print('city:',city)


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
        except expression as identifier:
                pass

    return string_arry[:-1] #有个bug，最后一个数组元素内存溢出


#函数功能：对输入的身份证号码进行校验(根据身份证编码规律的国家标准进行)
#输入参数：包含星号的身份证号码（暂时只支持18位的中华人民共和国的大陆居民身份证）
#输出参数：错误代码 
'''
错误代码：-1：默认值，表示没有问题
          0：输入的身份证号码不是十八位
          1：

           '''
def id_num_check(id_num):
    err_code=-1                    #定义err_code为错误类型的代码，默认值为-1，表示没有问题
    if len(id_num) != 18 :
        err_code = 0
        return err_code             #如果输入的身份证号码不是十八位，则返回错误代码err_code,的值为0

    else:
        return err_code
    





if __name__ == '__main__':

    print('errcode is:',id_num_check('320123****56251235'))

    #print(extract("1234567890","123",'890'))
    #getip()
   
    print('num = ',checkTime(10))
    print('num-1 = ',checkTime(9))
