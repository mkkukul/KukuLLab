import tkinter as tk
from tkinter import filedialog
import pyqrcode
from pyqrcode import QRCode

def qr_kodu_olustur():
    url = qr_url.get()
    
    if url:
        qr_url = pyqrcode.create(url)
        dosya_yolu = filedialog.asksaveasfile(defaultextension=".svg",filetypes=[("SVG Dosyaları", "*.svg")])
        if dosya_yolu:
            qr_url.svg(dosya_yolu,scale=8)
            durum_etiketi.config(text="QR Kodu oluşturuldu ve kaydedildi")

# Tasarım
