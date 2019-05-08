import urllib.request


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




url = 'http://news.ceic.ac.cn'




response = urllib.request.urlopen(url)
content = response.read().decode('utf-8', 'ignore')
#print(content)

提取的信息=extract(content,'<td align="center" style="padding-left: 20p','></td>')

print(提取的信息[0])
print(提取的信息[1])
print(提取的信息[2])