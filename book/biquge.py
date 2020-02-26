from bs4 import BeautifulSoup
from urllib.request import urlopen



url='http://www.xbiquge.la/xiaoshuodaquan/' #笔趣阁全部书
print('笔趣阁全部书:',url)
html=urlopen(url)

import gzip
html = gzip.decompress(html.read())

print(html.decode("utf-8"))

#第一步 把所有的小说名字和目录页地址down下来，格式为【（名字，地址）】





'''
在某个网页看到这么一句话：“大多数网站都对支持gzip压缩的浏览器做了gzip的压缩，在python中可以通过gzip包处理gzip压缩过的网页”

所以问题就是内容有压缩过，直接decode不行，需要用gzip来解压。然后再decode。

import gzip
...
html = gzip.decompress(response)
html = html.decode('gbk')
'''