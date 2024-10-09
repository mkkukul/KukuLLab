from tkinter import Label, Tk
import time

# Uygulama penceresini oluştur
app_windows = Tk()
app_windows.title("Dijital Saat")
app_windows.geometry("500x500")
app_windows.resizable(1, 1)
app_windows.configure(bg="black")

# Yazı tipi ve renk ayarları
text_font = ("Boulder", 68, 'bold')
background = "black"
foreground = "white"
border_width = 20

# Saat etiketi
time_label = Label(app_windows, font=text_font, bg=background, fg=foreground, bd=border_width)
time_label.grid(row=0, column=1, padx=10, pady=10)

# Tarih etiketi
date_label = Label(app_windows, font=("Boulder", 18), bg=background, fg=foreground)
date_label.grid(row=1, column=1, padx=10, pady=10)

def digital_clock():
    current_time = time.strftime("%H:%M:%S")
    label.confing(text=current_time)
    date_info = time.strftime("%d %B %Y")
    date_label.confing
    