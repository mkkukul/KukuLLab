import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

# Yüz tanıma için kullanılan cascade sınıfını yükle
face_cascade = cv2.CascadeClassifier(r"E:/Git HubX/KukuLLab/Projeler Python/Proje 5 Yüz tanıma/face_detector.xml")

# Fonksiyon: Dosya seç ve yüz tanı
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
    
    if file_path:
        # Seçilen resmin varlığını kontrol et
        if not os.path.exists(file_path):
            print(f"Resim dosyası mevcut değil: {file_path}")
            return
        
        img = cv2.imread(file_path)
        
        if img is None:
            print(f"Dosya açılamadı: {file_path}. Dosya yolunu kontrol edin.")
            return
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Yüz tanıma
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, minSize=(30, 30))
        
        # Yüzlerin etrafına dikdörtgen çiz ve etiket ekle
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(img, "İnsan", (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        
        # Görüntüyü Tkinter ile göstermek için düzenle
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = img.resize((600, 400), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        
        canvas.img = img
        canvas.create_image(0, 0, anchor=tk.NW, image=img)

# Tkinter arayüzü oluşturma
root = tk.Tk()
root.title("Yüz Tanıma Uygulaması")

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

open_button = tk.Button(root, text="Dosya Seç", command=open_file)
open_button.pack()

root.mainloop()
