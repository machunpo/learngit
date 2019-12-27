#-*-coding:utf-8-*-
import requests
import random 
import time
user_agent = [ 
	"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)", 
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)", 
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)", 
	"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)", 
	"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)", 
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)", 
	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)", 
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)", 
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)", 
	"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6", 
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1", 
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0", 
	"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5", 
	"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6", 
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11", 
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20", 
	"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"
] 

HEADER = { 
'User-Agent': random.choice(user_agent),  # 浏览器头部
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', # 客户端能够接收的内容类型
'Accept-Language': 'en-US,en;q=0.5', # 浏览器可接受的语言
'Connection': 'keep-alive', # 表示是否需要持久连接
} 

#函数功能：去除一段特征文本中间的数据
#输入参数：string_all,string_begin,string_end整段文本，前后的关键词
#输出参数：一段文本

def quxhu_extract(string_all,string_begin,string_end):

    m = 0; n = 0
    m = string_all.find(string_begin)
    n = string_all.find(string_end)

    return string_all[:m]+string_all[n+len(string_end):]

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

#函数功能：获取章节页面的标题和正文
#输入参数：章节页面的网址URL
#输出参数：包含标题和正文两个元素的元组
def get_the_biaoti_and_zhenwen(url):
    page = requests.get(url)
    page.encoding = 'utf-8'

    biaoti=extract(page.text,'<h1>','</h1>')
    biaoti=biaoti[0]
    #'文章的标题：str',
    zhenwen=extract(page.text,'<div id="content">','</div>')
    zhenwen=quxhu_extract(zhenwen[0],'<p>','</p>')
    zhenwen=quchu_heml(zhenwen).replace('&nbsp;','  ')
    zhenwen=(zhenwen).replace('\r','\n  ')
    return(biaoti,'  '+zhenwen)

#函数功能：获取每个章节URL和名称
#输入参数：book页面的网址URL
#输出参数：包含章节名称和网址的列表
def get_the_chapters_of_book(url):
    page = requests.get(url)
    page.encoding = 'utf-8'
    chapters_list=extract(page.text,'<dd>','</a></dd>')
    return chapters_list
    #["<a href='/1/1690/1267524.html' >楔子 一块黑布", "<a href='/1/1690/1267525.html' >第一章 故事会"]


if __name__ == '__main__':


    url_chapters_of_book=r'http://www.xbiquge.la/1/1690/'
    chapterslist=get_the_chapters_of_book(url_chapters_of_book)
    #print(chapterslist)
    for i in chapterslist:
        book_url=url_chapters_of_book+i[17:29]
        try:
            hi=(get_the_biaoti_and_zhenwen(book_url))
            print(hi[0])
        except:
            
            print('这个有问题'+hi[0])    

        with open('d:\\庆余年.txt','a') as f:
            f.write(hi[0]+'\n\n')
            f.write(hi[1])
            f.write('\n\n')
    time.sleep(5)



'''
    book_url=r'http://www.xbiquge.la/20/20948/10611401.html'
    hi=(get_the_biaoti_and_zhenwen(book_url))
    print(hi[1])
    with open('d:\\'+hi[0]+'.txt','a') as f:
        f.write(hi[0]+'\n')
        f.write(hi[1])
    #下一步开工

需要解决的问题
Traceback (most recent call last):
  File "c:/myfile/learngit/book/book_def_lib.py", line 108, in <module>
    hi=(get_the_biaoti_and_zhenwen(book_url))
  File "c:/myfile/learngit/book/book_def_lib.py", line 83, in get_the_biaoti_and_zhenwen
    zhenwen=quxhu_extract(zhenwen[0],'<p>','</p>')
IndexError: list index out of range

'''
