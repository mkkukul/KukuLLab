from tkinter import label, Tk
import time
app_windows = Tk()
# app_windows.mainloop()
app_windows.title("Dijital Saat")
app_windows.geometry("500x500")
app_windows.resizable(1,1)
app_windows.configure(bg="black")

text_font = ("Boulder", 68, 'bold')
background = "black"
foreground = "white"
border_widht = 20
# SAat Etiketleri
label = label(app_windows, font=text_font, bg=background, fg=foreground, bd=border_widht)
label.grid(row=0,column=1,padx=10,pady=10)
# tarih etiketi
date_label = label
