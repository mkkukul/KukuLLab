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
                            attigi_gol = int(gol_sayisi[0])
                            gol_sayisi_g2 =int(gol_sayisi[1])
                        except ValueError:
                            attigi_gol = None
                            gol_sayisi_g2 = None
                        if attigi_gol is not None and gol_sayisi_g2 is not None:
                            ev_sahibi = mac.find_all("td")[1].text
                            
                            
                        #     print(f"{Fore.RED}Hatalı gol sayısı: {gol_sayisi}")
                        #     continue
                        # toplan_gol += attigi_gol + gol_sayisi_g2
                        # if attigi_gol > gol_sayisi_g2:
                        #     galibiyet_sayisi += 1
                        # son_mac_skoru = gol_sayisi[0] + " - " + gol_sayisi[1]

                            
                            
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