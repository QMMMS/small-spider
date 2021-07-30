from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random


# html = urlopen("https://baike.baidu.com/")


def get_links(article_url):
    html = urlopen("https://chi.jinzhao.wiki{}".format(article_url))
    bs = BeautifulSoup(html.read(), "html.parser")
    bs1 = bs.p
    print(bs1.get_text())
    return bs1.find_all("a", href=re.compile("^(/wiki/.*)"
                                             "((?!en.wikipedia.org).)*$"))


links = get_links("/wiki/%E5%9F%83%E9%87%8C%E5%85%8B%C2%B7%E8%89%BE%E5%BE%B7%E5%B0%94")
while len(links) > 0:
    new_art = links[random.randint(0, len(links)-1)].attrs["href"]
    print(new_art)
    links = get_links(new_art)
# targets = bs.findAll("p")
# for target in targets:
#     print(target.get_text())
# ^(/wiki/.*)((?!en.wikipedia.org).)*$
# /wiki/+.*
