import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


# fonksiyon üret
def open_file():
   file_path = filedialog.askopenfilename()
   if file_path