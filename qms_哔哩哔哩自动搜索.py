from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import xlwt
import os
import time

"""
b = webdriver.PhantomJS(executable_path=r"C:\Program Files\phantomjs-2.1.1-windows\bin\phantomjs")
warning:Selenium support for PhantomJS has been deprecated, please use headless chrome
PhantomJS 可以对应安装 pip install selenium==2.48.0
PhantomJS 似乎比 chrome 速度慢



from selenium.webdriver.chrome.options import Options
chrome_options = Options()
# 设置chrome浏览器无界面模式
chrome_options.add_argument('--headless')
b = webdriver.Chrome(options=chrome_options)
我遇到了一个问题
chrome headlss 可以运行
但打不开网页
请解决问题的大佬联系我！
"""

b = webdriver.Chrome()
WAIT = WebDriverWait(b, 10)
b.set_window_size(800, 800)
n = 1


def search(to_search):
    b.get('https://www.bilibili.com')
    input0 = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#nav_searchform > input")))
    submit = WAIT.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div/div[2]/div/form/div/button')))
    input0.send_keys(to_search)
    submit.click()
    all_h = b.window_handles  # Returns the handles of all windows within the current session.
    b.switch_to.window(all_h[1])
    get_source()
    total_page_num = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                "#all-list > div.flow-loader > div.page-wrap >"
                                                                " div > ul > li.page-item.last > button")))
    return int(total_page_num.text)


def get_source():
    WAIT.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#all-list > div.flow-loader > div.filter-wrap')))
    html = b.page_source
    soup = BeautifulSoup(html, 'html.parser')
    save_to_excel(soup)


def next_page(page_num):
    try:
        next_btn = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                          '#all-list > div.flow-loader > div.page-wrap >'
                                                          ' div > ul > li.page-item.next > button')))
        next_btn.click()
        WAIT.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                                     '#all-list > div.flow-loader > div.page-wrap >'
                                                     ' div > ul > li.page-item.active > button'),
                                                    str(page_num)))
    except TimeoutException:
        b.refresh()
        next_page(page_num)
    finally:
        get_source()


def save_to_excel(soup):
    items = soup.find(class_='video-list clearfix').find_all(class_='video-item matrix')
    for item in items:
        item_title = item.find('a').get('title')
        item_link = item.find('a').get('href')
        item_dec = item.find(class_='des hide').text
        item_view = item.find(class_='so-icon watch-num').text
        item_biu = item.find(class_='so-icon hide').text
        item_date = item.find(class_='so-icon time').text
        global n
        sheet.write(n, 0, item_title)
        sheet.write(n, 1, item_link)
        sheet.write(n, 2, item_dec)
        sheet.write(n, 3, item_view)
        sheet.write(n, 4, item_biu)
        sheet.write(n, 5, item_date)
        book.save(path)
        print("写入第" + str(n) + "条信息！")
        n += 1


if __name__ == '__main__':
    print("哔哩哔哩自动搜索程序启动！")
    user_search = input("请输入您想搜索的内容：")
    root = "E:/data/"
    if not os.path.exists(root):
        os.mkdir(root)
    path = root + "哔哩哔哩搜索" + user_search + '.xls'
    if not os.path.exists(path):
        print("最多写入1000条，请您暂时不要进行任何操作...")
        time.sleep(1)
        book = xlwt.Workbook(encoding='utf-8', style_compression=0)
        sheet = book.add_sheet(user_search, cell_overwrite_ok=True)
        sheet.write(0, 0, '名称')
        sheet.write(0, 1, '地址')
        sheet.write(0, 2, '描述')
        sheet.write(0, 3, '观看次数')
        sheet.write(0, 4, '弹幕数')
        sheet.write(0, 5, '发布时间')
        total_num = search(user_search)
        for i in range(2, int(total_num + 1)):
            next_page(i)
        book.save(path)
        print("写入完毕！")
    else:
        print("文件已存在！")
    print("请查看" + path)
    b.quit()
