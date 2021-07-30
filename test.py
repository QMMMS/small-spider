from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random

html = urlopen("https://baike.baidu.com/item/%E9%83%91%E5%B7%9E%E6%88%90%E8%BF%"
               "9C%E5%BD%B1%E8%A7%86%E5%8C%96%E5%A6%86%E5%9F%B9%E8%AE%AD%E5%AD%A6%E6%A0%A1/9883398")
bs = BeautifulSoup(html.read(), "html.parser")
targets = bs.findAll("a")
for target in targets:
    print(target)
