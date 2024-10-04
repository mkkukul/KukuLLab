import requests
# from bs4 import BeautifulSoup

url = requests.get("https://www.imdb.com/chart/top/")

# if url.status_code == 403:
#     print("Siteden Veri Çekilebilir")
# else:
#    print("Siteden Veri Çekilmez")

# bez = BeautifulSoup(url.content,"html.parser")
# print(bez)

print(url)
# a = url.status_code
# print(a)   
# a = url.content
# a = url.text 
# a = url.encoding
# print(a)