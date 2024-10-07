import requests
from bs4 import BeautifulSoup
url = requests.get("https://covid19.saglik.gov.tr/")
if url.status_code ==200:
    print("Siteden Veri Çekilebilir")
else:
    print("Siteden Veri Çekilmez")
soup = BeautifulSoup(url.content,"html.parser")

for i in soup.find("ilsiralama_85").findAll("tr"):
    
    print("************************************")
    print(i.text)
    print("************************************")
