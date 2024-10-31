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
    maclar  = soup.find_all("div", class_="fixture")