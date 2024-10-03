import requests
url = requests.get("https://www.imdb.com/chart/top/")
# print(url)
# a = url.status_code
# print(a)
if url.status_code == 200:
    print("Siteden Veri Çekilebilir")
else:
   print("Siteden Veri Çekilmez") 