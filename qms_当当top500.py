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
            print("正在读取第" + item[0] + "条数据！")
            data_list.append(item)
    return data_list


def write_txt(item):
    print('(txt)写入第' + str(item["number"]) + '条！')
    path = "E:/data/当当top500.txt"
    with open(path, 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        f.close()


def write_xls():
    path2 = "E:/data/当当top250.xls"
    if not os.path.exists(path2):
        items = get_data_xls()
        print("正在写入xls!")
        workbook = xlwt.Workbook(encoding="utf-8")
        worksheet = workbook.add_sheet("sheet1")
        name_list = ["排名", "图片地址", "标题", "推荐", "作者", "次数", "价格"]
        for i in range(1, 8):
            worksheet.write(0, i-1, name_list[i-1])
        for item in items:
            for i in range(1, 8):
                print("(xls)写入第" + item[0] + "条！")
                worksheet.write(int(item[0]), i-1, item[i-1])
                workbook.save("E:/data/当当top250.xls")
        print("xls写入完毕！")
    else:
        print("xls文件已存在！")
    print("请查看E:/data/当当top500.xls")


def txt():
    path1 = "E:/data/当当top500.txt"
    if not os.path.exists(path1):
        print("正在写入txt!")
        for i in range(1, 26):
            basic_url = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-"
            url = basic_url + str(i)
            html = request_url(url)
            targets = get_data_txt(html)
            for target in targets:
                write_txt(target)
        print("txt写入完毕！")
    else:
        print("txt文件已存在！")
    print("请查看E:/data/当当top500.txt")


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
                    print(img.split("/")[-1] + "图片保存成功！")
            else:
                print(img.split("/")[-1] + "图片已存在！")
    print("进程结束！请查看" + root)


def menu():
    print("*" * 50)
    print("欢迎使用当当图书top500爬取程序！")
    print("更多有趣小程序，请关注https://github.com/QMMMS")
    print()
    print("1.写入txt")
    print("2.写入xls")
    print("3.保存图片")
    print()
    print("0.退出系统")
    print("*" * 50)


if __name__ == '__main__':
    while True:
        menu()
        num = input("请选择操作功能：")
        if num == "1":
            txt()
        elif num == "2":
            write_xls()
        elif num == "3":
            get_pic()
        else:
            break
