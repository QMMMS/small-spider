from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html.read(), "html.parser")
name_list = bs.findAll("span", {"class": "green"})
for name in name_list:
    print(name.get_text())
