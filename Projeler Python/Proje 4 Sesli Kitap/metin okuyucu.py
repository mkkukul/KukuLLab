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

def
    