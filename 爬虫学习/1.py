from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.baidu.com")



html = urlopen("http://pythonscraping.com/pages/page1.html")

bsObj = BeautifulSoup(html.read(),'lxml')
#bsObj = BeautifulSoup(html.read(),'html.parser')



print(bsObj.h1.get_text())

