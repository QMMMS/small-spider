import requests
import re
import json
import os
import xlwt


def request_url(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                                 "AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/92.0.4515.107 Safari/537.36"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def get_data_txt(html):
    pattern = re.compile(r'<li>.*?list_num.*?(\d+).</div>.*?'
                         '<img src="(.*?)".*?'
                         'class="name".*?'
                         'title="(.*?)">.*?'
                         'class="star">.*?'
                         'class="tuijian">(.*?)</span>.*?'
                         'class="publisher_info">.*?'
                         'target="_blank">(.*?)</a>.*?'
                         'class="biaosheng">.*?'
                         '<span>(.*?)</span></div>.*?'
                         '<p><span.*?class="price_n">&yen;(.*?)</span>.*?'
                         '</li>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {'number': item[0],
               'image': item[1],
               'title': item[2],
               'recommend': item[3],
               'author': item[4],
               'times': item[5],
               'price': item[6]}


def get_data_xls():
    data_list = []
    for i in range(1, 26):
        basic_url = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-"
        url = basic_url + str(i)
        html = request_url(url)
        pattern = re.compile(r'<li>.*?list_num.*?(\d+).</div>.*?'
                             '<img src="(.*?)".*?'
                             'class="name".*?'
                             'title="(.*?)">.*?'
                             'class="star">.*?'
                             'class="tuijian">(.*?)</span>.*?'
                             'class="publisher_info">.*?'
                             'target="_blank">(.*?)</a>.*?'
                             'class="biaosheng">.*?'
                             '<span>(.*?)</span></div>.*?'
                             '<p><span.*?class="price_n">&yen;(.*?)</span>.*?'
                             '</li>', re.S)
        items = re.findall(pattern, html)
        for item in items:
            print("???????????????" + item[0] + "????????????")
            data_list.append(item)
    return data_list


def write_txt(item):
    print('(txt)?????????' + str(item["number"]) + '??????')
    path = "E:/data/??????top500.txt"
    with open(path, 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        f.close()


def write_xls():
    path2 = "E:/data/??????top250.xls"
    if not os.path.exists(path2):
        items = get_data_xls()
        print("????????????xls!")
        workbook = xlwt.Workbook(encoding="utf-8")
        worksheet = workbook.add_sheet("sheet1")
        name_list = ["??????", "????????????", "??????", "??????", "??????", "??????", "??????"]
        for i in range(1, 8):
            worksheet.write(0, i-1, name_list[i-1])
        for item in items:
            for i in range(1, 8):
                print("(xls)?????????" + item[0] + "??????")
                worksheet.write(int(item[0]), i-1, item[i-1])
                workbook.save("E:/data/??????top250.xls")
        print("xls???????????????")
    else:
        print("xls??????????????????")
    print("?????????E:/data/??????top500.xls")


def txt():
    path1 = "E:/data/??????top500.txt"
    if not os.path.exists(path1):
        print("????????????txt!")
        for i in range(1, 26):
            basic_url = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-"
            url = basic_url + str(i)
            html = request_url(url)
            targets = get_data_txt(html)
            for target in targets:
                write_txt(target)
        print("txt???????????????")
    else:
        print("txt??????????????????")
    print("?????????E:/data/??????top500.txt")


def get_pic():
    root = "E:/Pic/dangdang_top250/"
    if not os.path.exists(root):
        os.mkdir(root)
    baseurl = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-"
    for i in range(1, 26):
        url = baseurl + str(i)
        html = request_url(url)
        pattern = re.compile(r'<li>.*?list_num.*?.</div>.*?'
                             '<img src="(.*?)".*?'
                             '</span>.*?'
                             '</li>', re.S)
        all_img = re.findall(pattern, html)
        for img in all_img:
            path = root + img.split("/")[-1]
            if not os.path.exists(path):
                read = requests.get(img)
                with open(path, "wb") as f:
                    f.write(read.content)
                    f.close()
                    print(img.split("/")[-1] + "?????????????????????")
            else:
                print(img.split("/")[-1] + "??????????????????")
    print("????????????????????????" + root)


def menu():
    print("*" * 50)
    print("????????????????????????top500???????????????")
    print("?????????????????????????????????https://github.com/QMMMS")
    print()
    print("1.??????txt")
    print("2.??????xls")
    print("3.????????????")
    print()
    print("0.????????????")
    print("*" * 50)


if __name__ == '__main__':
    while True:
        menu()
        num = input("????????????????????????")
        if num == "1":
            txt()
        elif num == "2":
            write_xls()
        elif num == "3":
            get_pic()
        else:
            break
