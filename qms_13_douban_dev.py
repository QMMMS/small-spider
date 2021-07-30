import urllib.request
import bs4
import os
import requests


def get_url(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                                 "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
        req = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(req)
        return response.read().decode("utf-8")
    except:
        return "fail!"


def get_pic(baseurl):
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html1 = get_url(url)
        soup = bs4.BeautifulSoup(html1, "html.parser")
        all_img = soup.find("ol").findAll("img")
        for img in all_img:
            src = img["src"]
            print(src)
            root = "E:/Pic/"
            path = root + src.split("/")[-1]
            print(path)
            try:
                if not os.path.exists(root):
                    os.mkdir(root)
                if not os.path.exists(path):
                    read = requests.get(src)
                    with open(path, "wb") as f:
                        f.write(read.content)
                        f.close()
                        print("succeeded!")
                else:
                    print("file has been recorded!")
            except:
                print("fail!")


def get_data(baseurl):
    data_list = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html1 = get_url(url)
        bs = bs4.BeautifulSoup(html1, "html.parser").ol
        targets1 = bs.findAll("span", {"class": "title"})
        for target in targets1:
            print(target.get_text())
    return data_list


if __name__ == '__main__':
    target_url = "https://movie.douban.com/top250?start="
    get_pic(target_url)
    get_data(target_url)
