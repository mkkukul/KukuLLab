import PyPDF2
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog

def pdfMetniCikart(pdfYolu):
    metin = ""
    pdfOkuyucu = PyPDF2.PdfReader(open(pdfYolu, 'rb'))
    for sayfa in range(len(pdfOkuyucu.pages)):
        metin += pdfOkuyucu.pages[sayfa].extract_text()
    return metin

def metniSeseCevir(metin, dil):
    ses = gTTS(text=metin, lang = 'tr')
    ses.save(ciktiDosyasi)
    # ses.save("ses.mp3")
    # os.system("start ses.mp3")

# dosya seçme fonksiyonu

def   dosya_sec():
    dosyaYolu = filedialog.askopenfilename(filetypes=[("Pdf Dosyaları", "pdf")])
    if dosyaYolu:
        pdf_metin = pdfMetniCikart(dosyaYolu)
        metniSeseCevir(pdf_metin,"kaydet.mp3")
        os.system("start kaydet.mp3")


# tkinter arayüzü
app = tk.Tk()
app.title("Metin Okuyucu")


app.mainloop()