import PyPDF2
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog

def pdfMetniCikart(pdfYolu):
    metin = ""
    pdfOkuyucu=