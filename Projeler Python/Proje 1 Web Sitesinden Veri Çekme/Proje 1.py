import requests
from bs4 import BeautifulSoup

# Ek başlıklar ekleyerek daha gerçekçi bir tarayıcı isteği simüle etme
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com/",
    "DNT": "1",  # Do Not Track request header
    "Connection": "keep-alive"
}

# İsteği başlıklarla birlikte gönderme
url = requests.get("https://www.imdb.com/chart/top/", headers=headers)

# Durum kodunu kontrol etme
if url.status_code == 403:
    print("Siteden Veri Çekilemez (403 Forbidden)")
elif url.status_code == 200:
    print("Siteden Veri Çekilebilir")
else:
    print(f"Beklenmedik bir hata: {url.status_code}")

# Sayfa içeriğini işleme
soup = BeautifulSoup(url.content, "html.parser")
print(soup.prettify())  # Daha okunabilir HTML çıktısı


# print(url)
# a = url.status_code
# print(a)   
# a = url.content
# a = url.text 
# a = url.encoding
# print(a)