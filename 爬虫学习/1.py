from urllib.request import urlopen
from bs4 import BeautifulSoup

#html = urlopen("http://www.baidu.com")



html = urlopen("https://tianqi.2345.com/")

bsObj = BeautifulSoup(html.read(),'lxml')
#bsObj = BeautifulSoup(html.read(),'html.parser')

banner_date=bsObj.findAll('div',{"class":"banner-right-con-list-time"})
date=bsObj.findAll('div',{"class":"date"})
weather=bsObj.findAll('div',{"class":"banner-right-con-list-status"})
temp=bsObj.findAll('div',{"class":"banner-right-con-list-temp"})

print('banner_date:',banner_date[0].get_text())
print('date:',date[0].get_text())
print('weather:',weather[0].get_text())
print('temp:',temp[0].get_text())


for i in range(len(weather)):

    print(banner_date[i].get_text(),date[i].get_text(), weather[i].get_text(),temp[i].get_text() )
print(bsObj.head.title.get_text())



#  <div class="banner-right-con-list-time">
#                  明天
#                </div>



