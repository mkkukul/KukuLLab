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
       faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05,minNeighbor=5, minSize=(30,30))
       
       for(x,y,w,h) in faces:
           cv2.rectangle(img,(x,y), (x+w, y+h), (255,0,0),2)
           cv2.putText(img,"İnsan")
            