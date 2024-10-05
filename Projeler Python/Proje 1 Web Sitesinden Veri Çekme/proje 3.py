import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.bilgisayarhocam.com/")
if url.status_code == 200:
    print("Siteden Veri Çekilebilir")
else:
    print("Siteden Veri Çekilmez")
    
soup = BeautifulSoup(url.content, "html.parser")

div_çek = soup.find_all("img", {"class": "font-bold"}).a
print(div_çek.get("href"))
# for i in div_çek:
#     print(i.text)

# print(div_çek)