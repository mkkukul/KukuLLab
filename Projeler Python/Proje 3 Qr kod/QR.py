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
uygulama_pencere = tk.Tk()
uygulama_pencere.title("QR Kod Oluşturucu")
etiket = tk.Label(uygulama_pencere,text="Url'yi Girin:")
url_girdi = tk.Entry(uygulama_pencere,width=40)
qr_kodu_olustur_butonu = tk.Button(uygulama_pencere,text="QR Kodu Oluştur",command=qr_kodu_olustur)
durum_etiketi = tk.Label(uygulama_pencere,text="")
# etiket.pack()
# qr_kodu_olustur_butonu.pack()
etiket.grid(row=0,column=0,padx=10,pady=10)
url_girdi.grid(row=0,column=1,padx=10,pady=10)
qr_kodu_olustur_butonu.grid(row=1,column=0,columnspan=2,padx=10,)

uygulama_pencere.mainloop()