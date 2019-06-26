
import json
import urllib.request

#函数功能：去除一段文本中的HTML标记
#输入参数：text_all 整段文本
#输出参数：去除HTML标记后的文本
def quchu_heml(html_text):
    s = html_text.find("<")
    while s != -1:
        s = html_text.find("<")
        e = html_text.find(">")
        html_text = html_text.replace(html_text[s:e + 1], "")
    return(html_text)
    
        


#函数功能：输入一个月份或者日期，如果小于10，则在其前面补齐0，用于月份或者日期的对齐
#输入参数：i 整形变量
#输出参数：l 字符串
def  checkTime(i):
    if (i < 10):
        l = "0" + str(i)  
    else:
        l=str(i)
    return l




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


if __name__ == '__main__':

    hi=quchu_heml('jdsajfklsad<li>this  is <a><test>hahah')

    print(hi)
    
    #print(quxhu_extract('参考位置:<a href="http://news.ceic.ac.cn/CD20190601000131.html">新疆喀什地区塔什库尔干县(5分钟更新一次)','<a href','html">'))
    #这个的输出为    ‘参考位置:新疆喀什地区塔什库尔干县(5分钟更新一次)’

    #getip()
    #print(checkTime(2))
    #print(extract('123456789123654789','123','789'))

