import requests

url = "https://pythonscraping.com/pages/files/form.html"
get_html = requests.get(url)
print(get_html.text)
params = {"firstname": "a", "lastname": "b"}
url2 = "https://pythonscraping.com/pages/files/processing.php"
post_html = requests.post(url2, params)
print(post_html.text)
