import tkinter as tk
from tkinter import filedialog
import pyqrcode
from pyqrcode import QRCode

def qr_kodu_olustur():
    url = qr_url.get()
    
    if url:
        qr_url = pyqrcode.create(url)
        dosya_yolu = filedialog.asksaveasfile(defaultextension=".svg")

