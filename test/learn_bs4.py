from bs4 import BeautifulSoup


soup = BeautifulSoup('<b class="boldest">Extremely bold</b>',features="lxml")

print(soup.prettify())
