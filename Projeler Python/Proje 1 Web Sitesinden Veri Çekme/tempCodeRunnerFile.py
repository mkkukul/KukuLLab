import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.imdb.com/chart/top/")

if url.status_code == 403:
    print("Siteden Veri Çekilebilir")
else:
   print("Siteden Veri Çekilmez")

soup = BeautifulSoup(url.content,"html.parser")
print(soup)