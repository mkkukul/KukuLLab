import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


# fonksiyon üret
def open_file():
   file_path = filedialog.askopenfilename()
   if file_path:
       img = cv2.imread(file_path)
       gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, minSize=(30, 30))

       
       for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y), (x+w, y+h), (255,0,0),2)
            cv2.putText(img,"insan", (x , y+h+20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),2)

       img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
       img = Image.fromarray(img)
       img = img.resize((600,400), Image.LANCZOS)   
       img = ImageTk.PhotoImage(img)
       
       canvas.img = img
       canvas.create_image(0,0, anchor = tk.NW, image=img)

face_cascade = cv2.CascadeClassifier('face_detector.xml')

# arayüz
root = tk.Tk()
root.title("Yüz Tanıma")

canvas = tk. Canvas(root, width=600, height=400)
canvas.pack()
open_button = tk.Button(root, text="Dosya Seç", command = open_file)
open_button.pack()
root.mainloop()        
            