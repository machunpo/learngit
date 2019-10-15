from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html"),'lxml')

print(soup.prettify())
