import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.bilgisayarhocam.com/")
if url.status_code == 200:
    print("Siteden Veri Çekilebilir")
else:
    print("Siteden Veri Çekilmez")
    
soup = BeautifulSoup(url.content, "html.parser")
# yazdır = soup.html
# yazdır = soup.head.title.text
# yazdır = soup.find("p").text
yazdır = soup.find_all("h2")
for i in yazdır:
    print(i.text)

