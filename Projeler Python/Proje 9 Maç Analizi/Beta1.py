import requests
from bs4 import BeautifulSoup
from colorama import Fore, init
import os
init(autoreset=True)

def takim_bilgilerini_cek(takim):
    clear_screen()
    url = f"https://www.sporx.com/{takim}-fiksturu-ve-mac-sonuclari"
    response = requests.get(url)  # 'responce' yerine 'response' olarak düzeltildi
    soup = BeautifulSoup(response.content, "html.parser")
    maclar = soup.find_all("tr")
    galibiyet_sayisi = 0
    toplam_gol = 0  # 'toplan_gol' yerine 'toplam_gol' olarak değiştirildi
    son_mac_skoru = None
    for mac in maclar:
        skor_element = mac.find("a", class_="d-block rounded bg-sporx text-white fw-bolder py-1 px-1 text-nowrap")
        if skor_element:
            skor = skor_element.get_text(strip=True)
            gol_sayisi = skor.split("-")
            if len(gol_sayisi) == 2 and gol_sayisi[0].strip() and gol_sayisi[1].strip():
                try:
                    attigi_gol = int(gol_sayisi[0])
                    gol_sayisi_g2 = int(gol_sayisi[1])  # 'yedigi_gol' değişikliği yapılmadan bırakıldı
                except ValueError:
                    attigi_gol = None
                    gol_sayisi_g2 = None
                if attigi_gol is not None and gol_sayisi_g2 is not None:
                    ev_sahibi = mac.find("td", class_="text-start w-25").find("a").get_text(strip=True)
                    deplasman = mac.find("td", class_="text-start w-25").find("a").get_text(strip=True)
                    if takim.lower() == turkce_karakter_degistir(ev_sahibi).lower():
                        toplam_gol += attigi_gol
                        if attigi_gol > gol_sayisi_g2:
                            galibiyet_sayisi += 1
                        son_mac_skoru = f"Son Maç Skoru: {ev_sahibi} {skor} {deplasman}"
                    elif takim.lower() == turkce_karakter_degistir(deplasman).lower():
                        toplam_gol += gol_sayisi_g2
                        if gol_sayisi_g2 > attigi_gol:
                            galibiyet_sayisi += 1
                        son_mac_skoru = f"Son Maç Skoru: {ev_sahibi} {skor} {deplasman}"
