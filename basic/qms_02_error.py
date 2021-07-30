from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
# try:
#     # 注意，下一行网页故意留了一个错误（URL error）
#     html = urlopen("http://www.ythonscraping.com/pages/page.html")
#     bs = BeautifulSoup(html, "html.parser")
#     print(bs.html.body.h1)
# except HTTPError:
#     print(HTTPError)
# except URLError:
#     print(URLError)
# else:
#     pass
# try:
#     # 注意，下一行网页故意留了一个错误（HTTP error）
#     html = urlopen("http://www.pythonscraping.com/pages/page.html")
#     bs = BeautifulSoup(html, "html.parser")
#     print(bs.html.body.h1)
# except HTTPError:
#     print(HTTPError)
# except URLError:
#     print(URLError)
# else:
#     pass
# html = urlopen("http://www.pythonscraping.com/pages/page1.html")
# bs = BeautifulSoup(html, "html.parser")
# print(bs.html.body.h1)


def get_title(web):
    try:
        target_html = urlopen(web)
    except HTTPError:
        print(HTTPError)
        return None
    except URLError:
        print(URLError)
        return None
    else:
        pass
    try:
        target_bs = BeautifulSoup(target_html.read(), "html.parser")
        title = target_bs.body.h1
    except AttributeError:
        print(AttributeError)
        return None
    return title


print(get_title("http://www.ythonscraping.com/pages/page.html"))
print(get_title("http://www.pythonscraping.com/pages/page.html"))
print(get_title("http://www.pythonscraping.com/pages/page1.html"))
print(get_title("http://www.pythonscraping.com/pages/warandpeace.html"))
