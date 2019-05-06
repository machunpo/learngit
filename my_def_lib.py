
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
        except :
                pass

    return string_arry[:-1] #有个bug，最后一个数组元素内存溢出


#函数功能：对输入的身份证号码进行校验(根据身份证编码规律的国家标准进行)
#输入参数：包含星号的身份证号码（暂时只支持18位的中华人民共和国的大陆居民身份证）
#输出参数：错误代码 
'''
错误代码：-1：默认值，表示没有问题
          0：输入的身份证号码不是十八位
          1：输入了非法的字符（0~9，*，x）以外的字符

           '''
def id_num_check(id_num):

    err_code=-1                    #定义err_code为错误类型的代码，默认值为-1，表示没有问题

    


    if len(id_num) != 18 :
        err_code = 0
        return err_code             #如果输入的身份证号码不是十八位，则返回错误代码err_code,的值为0  

    else:
        
        for i in id_num:
            if (i=='1') | (i=='2')| (i=='3')| (i=='4')| (i=='5')| (i=='6')| (i=='7')| (i=='8')| (i=='9')| (i=='0')| (i=='*') | (i=='x')  :
                pass
            else:
                #print(i)
                err_code=1                      #这里懒得写注释了，但愿n年后我还知道这写的是啥，但是最大的可能是这个代码用不到那个时候

        if err_code < 0 :
 	        
            shenfen=(id_num[0:2])
            if '*' in shenfen :
                pass
            else:
                pass

            chenshi=(id_num[2:4])
            if '*' in chenshi:
                pass
            else:
                pass

            quxian=(id_num[4:6])
            if '*' in quxian :
                pass
            else:
                pass
#以上三项进行合并
            year=(id_num[6:10])
             if '*' in year :
                pass
            else:
                pass
            mon=(id_num[10:12])
             if '*' in mon :
                pass
            else:
                pass
            day=(id_num[12:14])
             if '*' in day :
                pass
            else:
                pass
            szdpcs=(id_num[14:16])
             if '*' in szdpcs :
                pass
            else:
                pass
            xinbie=(id_num[16:17])
             if '*' in xinbie :
                pass
            else:
                pass
            jiaoyanma=(id_num[17])
             if '*' in jiaoyanma :
                pass
            else:
                pass
 		       
    return err_code


'''
 	+    身份证号码的意义
 	+
 	+　　①前1、2位数字表示：所在省份的代码，河南的省份代码是41哦!
 	+
 	+　　②第3、4位数字表示：所在城市的代码;
 	+
 	+　　③第5、6位数字表示：所在区县的代码;
 	+
 	+　　④第7~14位数字表示：出生年、月、日;
 	+
 	+　　⑤第15、16位数字表示：所在地的派出所的代码;
 	+
 	+　　⑥第17位数字表示性别：奇数表示男性，偶数表示女性;
 	 	  
 	+　　⑦第18位数字是校检码：也有的说是个人信息码，一般是随计算机随机产生，用来检验身份证的正确性。校检码可以是0~9的数字，有时也用x表示。
 	+   
     
 '''




if __name__ == '__main__':

    print('errcode is:',id_num_check('321082197112113010'))


    #print(extract("1234567890","123",'890'))
    #getip()
   
    #print('num = ',checkTime(10))
    #print('num-1 = ',checkTime(9))
