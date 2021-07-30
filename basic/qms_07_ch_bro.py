from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html, "html.parser")
for child in bs.find("table", {"id": "giftList"}).children:
    print(child)
print("*" * 50)
for sibling in bs.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)
print("*" * 50)
print(bs.find("img",
              {"src": "../img/gifts/img1.jpg"})
      .parent.previous_sibling.get_text())
