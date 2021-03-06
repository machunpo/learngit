import urllib.request
import requests

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

def get_page_txt(url): #获取指定页面‘url’的文本内容
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf8', 'ignore')
    book_type=extract(content,'<title>','</title>')
    novel_text=extract(content,'<div id="content">','</div>')
    
    return(book_type,novel_text)






def get_the_chapters_of_book(url):
    page = requests.get(url)
    page.encoding = 'utf-8'
    chapters_list=extract(page.text,'<dd>','</a></dd>')
    return chapters_list
    #["<a href='/1/1690/1267524.html' >楔子 一块黑布", "<a href='/1/1690/1267525.html' >第一章 故事会"]





if __name__ == '__main__':
    
    my_list=get_the_chapters_of_book('http://www.xbiquge.la/1/1690/')
    for i in my_list:
        j=i.replace("<a href='","")
        print(j[0:20])
        print(j[23:])
