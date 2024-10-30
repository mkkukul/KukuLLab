import tkinter as tk
from tkinter import messagebox
import requests
import pyperclip


def shorten_url():
    long_url = entry.get
    responce = requests.get(f'http://tinyurl.com/api-create.php?url={long_url}')
    short_url = responce.text
    copy_button.confing(state=tk.NORMAL)
    
def copy_to_clipboard():
    shorten_url = result_label.cget("text")[11:]
    pyperclip.copy(shorten_url)
    messagebox.showinfo("Kopyalandı", "Kısaltılmış URL kopyalandı.")
    
app = tk.Tk()
app.title("URL Kısaltıcı")
label = tk.Label(app, text="URL'yi girin:")
label.pack(pack=10)
entry = tk.Entry(app, width=40)
shorten_button = tk.Button(app, text="Kısalt", command=shorten_url)