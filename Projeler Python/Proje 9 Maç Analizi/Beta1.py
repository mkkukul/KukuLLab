import requests
from bs4 import BeautifulSoup
from colorama import Fore, init
import os
init(autoreset=True)
def takim_bilgilerini_cek(takim):
    clear_screen()
    url = f"https://www.sporx.com/{takim}-fiksturu-ve-mac-sonuclari"
    responce = requests.get(url)
    soup = BeautifulSoup(responce.content, "html.parser")
    maclar  = soup.find_all("tr")
    galibiyet_sayisi = 0
    toplan_gol = 0
    son_mac_skoru = None
    for mac in maclar:
                skor_element = mac.find("a", class="d-block rounded bg-sporx text-white fw-bolder py-1 px-1 text-nowrap")
                if skor_element:
                    skor = skor_element.get_text(strip=True)
                    gol_sayisi = skor.split("-")
                    if len(gol_sayisi) == 2 and gol_sayisi[0].strip() and gol_sayisi[1].strip():
                        try:
                            attigi_gol =
                            
                        # gol_sayisi = [int(i) for i in gol_sayisi]
                        # toplan_gol += sum(gol_sayisi)
                        # if gol_sayisi[0] > gol_sayisi[1]:
                        #     galibiyet_sayisi += 1
                        # son_mac_skoru = gol_sayisi
                    
        
        
        # try:
        #     skor = mac.find_all("td")[3].text
        #     skor = skor.split("-")
        #     skor = [int(i) for i in skor]
        #     toplan_gol += sum(skor)
        #     if skor[0] > skor[1]:
        #         galibiyet_sayisi += 1
        #     son_mac_skoru = skor
        # except:
        #     pass