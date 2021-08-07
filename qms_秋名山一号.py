from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import os
from concurrent.futures import ThreadPoolExecutor
import concurrent
import datetime
import time

# options = webdriver.ChromeOptions()
# options.add_argument("--proxy-server=***************")
# br = webdriver.Chrome(options=options)

front_url = "http://aa.6666yes.com/"
indexes = ["/oumeisetu/",
           "/zipaitoupai/",
           "/yazhousetu/",
           "/meituisiwa/",
           "/mingxingyinluan/",
           "/katongdongman/",
           "/shaofushunv/"]
proxy_pool_url = 'http://127.0.0.1:5555/random'
basic_page_number = 50


def make_basic_dir():
    root_1 = "E:/Pic/"
    root0 = "E:/Pic/study_pic/"
    if not os.path.exists(root_1):
        os.mkdir(root_1)
    if not os.path.exists(root0):
        os.mkdir(root0)


def get_basic_url(url):
    b.get(url)
    button = WAIT.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/ul/h1/li/a')))
    button.click()
    front_html = get_html(b.current_url)
    soup = BeautifulSoup(front_html, 'html.parser')
    basic_url0 = soup.find("a", class_="speed-url").attrs["href"]
    return basic_url0


def get_random_proxy(proxy_pool_url0):
    return requests.get(proxy_pool_url0).text.strip()


def get_html_by_requests(url, proxy0):
    try:
        headers = {
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/92.0.4515.107 Safari/537.36 "
        }
        proxies = {'http': 'http://' + proxy0}
        return requests.get(url, proxies=proxies, headers=headers, timeout=1)
    except TimeoutException:
        return None


def get_html(url):
    # 输入url 返回页面源代码
    try:
        b.get(url)
        return b.page_source
    except TimeoutException:
        b.refresh()
        get_html(url)


def get_page_number(html):
    soup = BeautifulSoup(html, "html.parser")
    page_info_soup = soup.find("div", id="page")
    page_num = page_info_soup.findAll("a")[2].get_text()
    return page_num


def get_into_urls(html):
    # 找到进一步url
    into_urls0 = []
    soup = BeautifulSoup(html, 'html.parser')
    ol_target = soup.findAll("ul")[1]
    li_targets = ol_target.findAll("li")
    for li_target in li_targets:
        # print(li_target.find("a").text)
        into_url = basic_url + li_target.find('a').get('href')
        # print(into_url)
        into_urls0.append(into_url)
    # print(into_urls0)
    return into_urls0


def get_pic_url_and_name(into_url):
    pic_urls = []
    into_html = get_html(into_url)
    # pic_html = get_html_by_requests(into_url, get_random_proxy())
    into_soup = BeautifulSoup(into_html, 'html.parser')
    name = into_soup.find("h1").text
    p_targets = into_soup.findAll("p")
    for p_target in p_targets:
        pic_url = p_target.find("img").get("src")
        pic_urls.append(pic_url)
    return pic_urls, name


def download_pic(src, name, proxy0):
    # print(src)
    root = "E:/Pic/study_pic/%s/" % name
    path = root + src.split("/")[-1]
    if not os.path.exists(root):
        os.mkdir(root)
    read = get_html_by_requests(src, proxy0)
    print(datetime.datetime.now(), end=":")
    if read is not None:
        if not os.path.exists(path):
            with open(path, "wb") as f:
                f.write(read.content)
                f.close()
                print(path + "图片保存成功!")
        else:
            print(path + "图片已存在!")
    else:
        print(path + "好像无法加载，自动跳过....")
        pass


if __name__ == '__main__':
    make_basic_dir()

    options = webdriver.ChromeOptions()
    options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) '
                         'Gecko/20100101 Firefox/6.0"')
    b = webdriver.Chrome(options=options)
    WAIT = WebDriverWait(b, 10)
    b.set_window_size(800, 800)

    basic_url = get_basic_url(front_url)
    for index in indexes:
        tool_html = get_html(basic_url + index)
        if index == "/shaofushunv/":
            page_number = get_page_number(tool_html)
        else:
            page_number = basic_page_number

        for i in range(1, int(page_number) + 1):
            origin_html = get_html(basic_url + index + "list_" + str(i) + ".html")
            # print(basic_url + index + "list_" + str(i) + ".html")
            img_urls = get_into_urls(origin_html)
            for img_url in img_urls:
                targets = get_pic_url_and_name(img_url)
                png_urls = targets[0]
                png_name = targets[1]
                time.sleep(1)
                proxy = get_random_proxy(proxy_pool_url)
                with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
                    for png_url in png_urls:
                        executor.submit(download_pic, png_url, png_name, proxy)
    b.quit()
