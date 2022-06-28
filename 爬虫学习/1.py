from urllib.request import urlopen
from bs4 import BeautifulSoup

head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36 2345Explorer/10.24.0.21754"}


html = urlopen("https://tianqi.2345.com/today-70445.htm")
bsObj = BeautifulSoup(html,"lxml")


print(bsObj.head)

nameList = bsObj.findAll("span", {"class": "green"})
for name in nameList:
    print(name.get_text())

# User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36 2345Explorer/10.24.0.21754
