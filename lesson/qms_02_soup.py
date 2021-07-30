from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://baidu.com")
bs = BeautifulSoup(html.read(), "html.parser")
print(bs.title.string)
print(bs.a.attrs["class"])
print(bs.a.string)
print(type(bs.a.string))
print(bs.head.contents[1])
# .parents .parent .previous_sibling .next_sibling .previous_element(s) .next_element(s) .has_attr


def name_exist(tag):
    # 和bs.findAll连用，查找属性
    return tag.has_attr("name")


def use():
    t_list = bs.findAll(name_exist)
    print(t_list)


# t2_list = bs.findAll(id="head")
# 定向搜索属性内容
# t2_list = bs.findAll(href=True)
# 只要有属性（类似于name_exist）
# t2_list = bs.findAll(text=["地图", "贴吧"], limit=3)
# 获取多少个limit
# 属性筛选可以以列表传入多个匹配定对象
# t2_list = bs.findAll(text=re.compile("\w"))
t2_list = bs.select("title")
# .mnav #u1 a[class='bri'] "head > title" .mnav ~ .bri
for t2 in t2_list:
    print(t2)
