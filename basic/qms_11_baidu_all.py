from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()


def get_links(url):
    global pages
    html = urlopen("https://baike.baidu.com{}".format(url))
    bs = BeautifulSoup(html.read(), "html.parser")
    if bs.find("h1") is not None:
        print(bs.find("h1").get_text())
    targets = bs.findAll("a", {"class": "sub"}, href=re.compile("^(/item/.*)"))
    for target in targets:
        if target not in pages:
            new = target.attrs["href"]
            print(new)
            pages.add(new)
            get_links(new)


get_links(" ")
