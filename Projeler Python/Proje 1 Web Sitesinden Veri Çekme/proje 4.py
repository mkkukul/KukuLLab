import requests
from bs4 import BeautifulSoup
url = requests.get("https://covid19.saglik.gov.tr/")
if url.status_code ==200:
    print("Siteden Veri Çekilebilir")
else:
    print("Siteden Veri Çekilmez")
soup = BeautifulSoup(url.content,"html.parser")
while True:
    for i in soup.find("tbody").find_all("tr"):

# for i in soup.find("il_siralama").findAll("ilsiralama_85"):
    
#     print("************************************")
#     print(i.text)
#     print("************************************")
    
    
