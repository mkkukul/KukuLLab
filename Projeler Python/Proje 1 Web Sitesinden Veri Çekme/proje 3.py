import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.bilgisayarhocam.com/")
if url.status_code == 200:
    print("Siteden Veri Çekilebilir")
else:
    