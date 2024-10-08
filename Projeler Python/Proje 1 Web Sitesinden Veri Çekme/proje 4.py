
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# WebDriver'ı başlat
driver = webdriver.Chrome()

# Sayfayı aç
driver.get("https://covid19.saglik.gov.tr/")

# Sayfanın yüklenmesi için bekleyin
time.sleep(5)

# Sayfanın kaynak kodunu al
html = driver.page_source

# BeautifulSoup ile işle
soup = BeautifulSoup(html, "html.parser")

# Verileri çek
for i in soup.find("div", class_="data_gunluk_il_listesi").find_all("li", class_="ilsiralama_85"):
    print("************************************")
    print(i.text)

# WebDriver'ı kapat
driver.quit()


# import requests
# from bs4 import BeautifulSoup

# # Siteye istek gönder
# url = requests.get("https://covid19.saglik.gov.tr/")
# if url.status_code == 200:
#     print("Siteden Veri Çekilebilir")
# else:
#     print("Siteden Veri Çekilemez")
#     exit()

# # HTML içeriğini al ve BeautifulSoup ile işle
# soup = BeautifulSoup(url.content, "html.parser")

# # Veri çekme işlemi
# data_list = soup.find("div", class_="data_gunluk_il_listesi")

# # Eğer data_list boş değilse (sayfa yapısına göre kontrol)
# if data_list:
#     for i in data_list.find_all("li", class_="ilsiralama_85"):
#         print("************************************")
#         print(i.text.strip())  # Boş satırları temizlemek için strip() ekledim
# else:
#     print("Veri bulunamadı ya da çekilemiyor.")



# import requests
# from bs4 import BeautifulSoup

# # Siteye istek gönder
# url = requests.get("https://covid19.saglik.gov.tr/")
# if url.status_code == 200:
#     print("Siteden Veri Çekilebilir")
# else:
#     print("Siteden Veri Çekilemez")
#     exit()

# # HTML içeriğini al ve BeautifulSoup ile işle
# soup = BeautifulSoup(url.content, "html.parser")

# # Veri çekme işlemi
# data_list = soup.find("div", class_="data_gunluk_il_listesi")

# # Eğer data_list boş değilse (sayfa yapısına göre kontrol)
# if data_list:
#     for i in data_list.find_all("li", class_="ilsiralama_85"):
#         print("************************************")
#         print(i.text.strip())  # Boş satırları temizlemek için strip() ekledim
# else:
#     print("Veri bulunamadı ya da çekilemiyor.")
    
# input("Devam Edilsin Mi")


# import requests
# from bs4 import BeautifulSoup
# url = requests.get("https://covid19.saglik.gov.tr/")
# if url.status_code ==200:
#     print("Siteden Veri Çekilebilir")
# else:
#     print("Siteden Veri Çekilmez")
# soup = BeautifulSoup(url.content,"html.parser")

# say = 1
# while True:
#     for i in soup.find("div", class_="data_gunluk_il_listesi").find_all("li", class_="ilsiralama_85"):
#         print("************************************")
#         print(i.text)
    
# input("Devam Edilsin Mi")

# for i in soup.find("il_siralama").findAll("ilsiralama_85"):
    
#     print("************************************")
#     print(i.text)
#     print("************************************")
    
    
