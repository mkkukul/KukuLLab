import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.imdb.com/chart/top/")

if url.status_code == 403:
    print("Siteden Veri Çekilemez (403 Forbidden)")
elif url.status_code == 200:
    print("Siteden Veri Çekilebilir")
else:
    print(f"Beklenmedik bir hata: {url.status_code}")
soup = BeautifulSoup(url.content,"html.parser")
print(soup)

# print(url)
# a = url.status_code
# print(a)   
# a = url.content
# a = url.text 
# a = url.encoding
# print(a)