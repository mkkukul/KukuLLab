import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.bilgisayarhocam.com/")
if url.status_code == 200:
    print("Siteden Veri Çekilebilir")
else:
    print("Siteden Veri Çekilmez")
    
soup = BeautifulSoup(url.content, "html.parser")
div_çek = soup.find_all("div", {"class": "post-content"})

print(div_çek)