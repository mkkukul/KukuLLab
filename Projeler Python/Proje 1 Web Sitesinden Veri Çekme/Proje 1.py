import requests
url = requests.get("https://www.imdb.com/chart/top/")
# print(url)
a = url.status_code
print(a)