import tkinter as tk
from tkinter import messagebox
import requests
import pyperclip

def shorten_url():
    long_url = entry.get()
    response = requests.get(f'http://tinyurl.com/api-create.php?url={long_url}')  # "responce" yerine "response"
    short_url = response.text
    result_label.config(text=f'Kısaltılmış Link:{short_url}')
    copy_button.config(state=tk.NORMAL)

def copy_to_clipboard():
    shortened_url = result_label.cget("text")[17:]  # "Kısaltılmış Link:" kısmını atlamak için
    pyperclip.copy(shortened_url)
    messagebox.showinfo("Kopyalandı", "Kısaltılmış URL kopyalandı.")

app = tk.Tk()
app.title("URL Kısaltıcı")

label = tk.Label(app, text="URL'yi girin:")
label.pack(pady=10)

entry = tk.Entry(app, width=40)
entry.pack()

shorten_button = tk.Button(app, text="Kısalt", command=shorten_url)
shorten_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

copy_button = tk.Button(app, text="Kopyala", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack(pady=5)

app.mainloop()
