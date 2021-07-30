from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://s.weibo.com/top/summary")
bs = BeautifulSoup(html.read(), "html.parser").tbody
target = bs.findAll("a")
n = 1
for i in target:
    print(n, end="、")
    print(i.get_text())
    n += 1
