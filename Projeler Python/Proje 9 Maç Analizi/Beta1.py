import requests
from bs4 import BeautifulSoup
from colorama import Fore, init
import os
init(autoreset=True)
def takim_bilgilerini_cek(takim):
    clear_screen()
    url = f"https://www.sporx.com/{takim}-fiksturu-ve-mac-sonuclari"
    responce = requests.get(url)