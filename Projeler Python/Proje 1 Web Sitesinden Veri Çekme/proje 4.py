import requests
from bs4 import BeautifulSoup
url = requests.get("")
if url.status_code ==200:
    print("Siteden Veri Çekilebilir")
else:
    print("Siteden Veri Çekilmez")