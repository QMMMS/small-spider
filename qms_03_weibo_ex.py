import requests
url = "https://s.weibo.com/top/summary"
response = requests.get(url)
print(response)
resp = response.text
print(resp)
