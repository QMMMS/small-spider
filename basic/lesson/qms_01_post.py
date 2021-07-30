from urllib.request import urlopen
from urllib.parse import urlencode
import urllib.error


def post():
    data = bytes(urlencode({"hello": "world"}), encoding="utf-8")
    response = urlopen("http://httpbin.org/post", data=data)
    # post 方法规范(真实登录)
    print(response.read().decode())


def get():
    try:
        response = urlopen("http://httpbin.org/get", timeout=1)
        print(response.read().decode())
        print("status:", response.status)
        print(response.getheaders())
        print(response.getheader("Date"))
    except urllib.error.URLError or urllib.error.HTTPError:
        print("time out!")


get()
