import instaloader
import tkinter as tk
from tkinter import messagebox


def dowload_post():
    username = entry_username.get()
    
    try: 
        bot = instaloader.Instaloader()
        
        profile = instaloader.Profile.from_username(bot.context,username)
        posts = profile.get_posts()
        
        
        for index, post in enumerate (posts,1):
            bot.download_post(post, target=f"{profile.username}_{index}")
        
        messagebox.showinfo("Başarılı","Gönderiler İndirildi")
    except Exception as e:
        messagebox.showerror("Hata", str(e))
        
root = tk.Tk()
root.title("Instgram Gönderi İndirici")
root.geometry("300x200")

label = tk.Label(root, text="Kulladınıcı Adı:")
label.pack(padx=10)
entry_username = tk.Entry(root)
entry_username.pack()
dowload_button = tk.Button(root, text="Bilgileri İndir", command=dowload_post)
dowload_button.pack(pady=10) 



root.mainloop()       