import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

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