# coding=utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random

pages = set()


def get_url(url):
    global pages
    html = urlopen("https://baike.baidu.com{}".format(url))
    bs = BeautifulSoup(html.read(), "html.parser")
    head = bs.find("h1")
    print(head.get_text())
    targets = bs.findAll("a", href=re.compile("^(/item/.*)"))
    return targets


links = get_url("/item/%E5%88%98%E5%BE%B7%E5%8D%8E/114923")
while len(links) > 0:
    new = links[random.randint(6, len(links)-1)].attrs["href"]
    print(new)
    pages.add(new)
    links = get_url(new)

# random.randint(6, len(links)-1)
