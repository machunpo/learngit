from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.baidu.com")



html = urlopen("https://tianqi.2345.com/")

bsObj = BeautifulSoup(html.read(),'lxml')
#bsObj = BeautifulSoup(html.read(),'html.parser')



print(bsObj.head.title)


print(bsObj.head.title.get_text())



