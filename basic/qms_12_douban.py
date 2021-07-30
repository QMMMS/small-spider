# coding=utf-8
import re
import urllib.request
import urllib.error
import bs4
import xlwt
import os
from bs4 import BeautifulSoup
# soup_item = str(soup_item)
# find_link = re.compile(r'<a href="(.*?)">')
# link = re.findall(find_link, soup_item)[0]
# find_img = re.compile(r'<img.*src="(.*?)"')
# find_title = re.compile(r'<span class="title">(.*?)</span>')
# find_rate = re.compile(r'<span class="title">........</span>')
# re.findall(rule,item).strip() 去空格


def test():
    baseurl = "https://movie.douban.com/top250?start=&filter="
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/92.0.4515.107 Safari/537.36"}
    req = urllib.request.Request(url=baseurl, headers=headers)
    # url data headers methods
    # 发送所有信息，模拟浏览器
    # req是一个封装的url对象
    response = urllib.request.urlopen(req)
    print(response.read().decode("utf-8"))


def main():
    baseurl = "https://movie.douban.com/top250?start=&filter="
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/92.0.4515.107 Safari/537.36"}
    req = urllib.request.Request(url=baseurl, headers=headers)
    # url data headers methods
    # 发送所有信息，模拟浏览器
    # req是一个封装的url对象
    response = urllib.request.urlopen(req)
    print(response.read().decode("utf-8"))
    data_list = get_data(baseurl)


def get_data(baseurl):
    data_list = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = ask_url(url)
        bs = BeautifulSoup(html.read(), "html.parser").ol
        targets1 = bs.findAll("span", {"class": "title"})
        for target in targets1:
            target = target.get_text()
            target = re.sub(r"\xa0/*", "", target)
            target = re.compile(r"[a-z]*").search(target).string
            data_list.append(target)
    return data_list


def save_data(data_li):
    workbook = xlwt.Workbook(encoding="utf-8")  # 创建workbook
    worksheet = workbook.add_sheet("sheet1")
    row = len(data_li)
    for i in range(0, row):
        worksheet.write(i, 0, data_li[i])
        root = "E:/data/"
        if not os.path.exists(root):
            os.mkdir(root)
        workbook.save("E:/data/豆瓣.xls")


def ask_url(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
    request = urllib.request.Request(url, headers=header)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        # html = response.read().decode("utf-8")
        # print(html)
        return response
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)


if __name__ == '__main__':
    # ask_url("https://movie.douban.com/top250?start=")
    data = get_data("https://movie.douban.com/top250?start=")
    save_data(data)

