#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
import urllib.request
import requests


def get_xiaoshuo_page(url):
     response = urllib.request.urlopen(url)
     content = response.read().decode('gbk', 'ignore')
     print(content)
     soup=BeautifulSoup(content,'lxml')
     print('test-h1:',soup.h1)
     print('test-div:',soup.find('div',id="content"))

url=r'http://www.xbiquge.la/1/1690/1267600.html'
page = requests.get(url)
page.encoding = 'utf-8'
#print(page.text)
soup = BeautifulSoup(page.text,'lxml')
#print(soup)
biaoti=(soup.h1)
print(biaoti)
zhenwen=(soup.find('div',id="content"))
print(zhenwen)
zhenwen=str(zhenwen).replace(r'<br/>',r' ')
print(zhenwen)

#创建beautifulsoup对象
#也可以用打开�??地的html文件来创建beautifulsoup对象，例�??:
#######soup = BeautifulSoup(open(r"c:/myfile/learngit/test/qinyunian.html"),'lxml')
#soup = BeautifulSoup(html)
#soup = bs4.BeautifulSoup(html,'lxml')
#bs4.BeautifulSoup.get_text()
#print(soup.prettify())
#print(biaoti)
#print(soup.find(<div id="content">))
#zhenwen=(soup.find('div',id="content"))
#zhenwen=str(zhenwen).replace(r'<br/>',r' ')
#print(zhenwen.replace(r'<p><a href="http://koubei.baidu.com/s/xbiquge.la" target="_blank">�??,点击进去,给个好评�??,分数越高更新越快,�??说给新笔趣阁打满分的最后都找到了漂�??的老婆�??!</a> 手机站全新改版升级地址：http://m.xbiquge.la，数�??和书签与电脑站同步，无广告清新阅读！</p>',''))

#下一步网来到的文�??
#get_xiaoshuo_page('http://www.xbiquge.la/1/1690/1267600.html')

