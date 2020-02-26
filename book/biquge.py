from bs4 import BeautifulSoup
from urllib.request import urlopen

url='http://www.xbiquge.la/xiaoshuodaquan/' #笔趣阁全部书

print('笔趣阁全部书:',url)

html=urlopen(url)

print(html.read().decode('utf-8'))
#第一步 把所有的小说名字和目录页地址down下来，格式为【（名字，地址）】