from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def get_url(url):
    html = urlopen("https://baike.baidu.com{}".format(url))
    bs = BeautifulSoup(html.read(), "html.parser")
    head = bs.find("h1")
    print(head.get_text())
    targets = bs.findAll("a", href=re.compile("^(/item/.*)"))
    for target in targets:
        if "href" in target.attrs:
            print(target.attrs["href"])


def find_url(url):
    html = urlopen(url)
    bs = BeautifulSoup(html.read(), "html.parser")
    targets = bs.findAll("a")
    for target in targets:
        print(target)


def decode(url):
    html = urlopen(url)
    print(html.read().decode("utf-8"))


# get_url("/item/%E5%88%98%E5%BE%B7%E5%8D%8E/114923")
# find_url("https://baike.baidu.com/item/%E9%83%91%E5%B7%9E%E6%88%90%E8%BF%9C%E5%BD%B1%E8%A7%86%E5%8C%96%E5%A6%86%E5%9F%B9%E8%AE%AD%E5%AD%A6%E6%A0%A1/9883398")
decode("http://baijiahao.baidu.com/s?id=1706353629679812820")
