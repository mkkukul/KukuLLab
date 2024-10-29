import instaloader
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def get_user_info(username):
    try:
        bot = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(bot.context, username)
    
        user_info = {
            "Username": profile.username,
            "Followers": profile.followers,
            "Followees": profile.followees,
            "Post Count": profile.mediacount,
            "Last Post Date": get_last_post_date(profile)
        }
    
        return user_info
    
    except Exception as e:
        return f"Hata: {str(e)}"

def get_last_post_date(profile):
    last_post = None
    for post in profile.get_posts():
        if not last_post or post.date_utc > last_post.date_utc:
            last_post = post
    return last_post.date_utc.strftime("%Y-%m-%d %H:%M:%S") if last_post else "Gönderi Yok"

def show_user():
    username = entry_username.get()
    user_info = get_user_info(username)
    if isinstance(user_info, dict):
        for widget in tree.get_children():
            tree.delete(widget)
        tree.insert("", "end", values=(
            user_info["Username"],
            user_info["Followers"],
            user_info["Followees"],
            user_info["Post Count"],
            user_info["Last Post Date"]
        ))
    else:
        messagebox.showerror("Hata", user_info)

root = tk.Tk()
root.title("Instagram Kullanıcı Bilgi Görüntüleyicisi")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label = tk.Label(root, text="Kullanıcı adı:")
label.grid(row=0, column=0, padx=5, pady=5)

entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=5, pady=5)

search_button = tk.Button(frame, text="Bilgileri Görüntüle", command=show_user)
search_button.grid(row=0, column=2, padx=5, pady=5)

tree = ttk.Treeview(root, columns=("Username", "Followers", "Followees", "Post Count", "Last Post Date"))
tree.heading("Username", text="Kullanıcı adı:")
tree.heading("Followers", text="Takipçiler:")
tree.heading("Followees", text="Takip Edilenler:")
tree.heading("Post Count", text="Gönderi Sayısı:")
tree.heading("Last Post Date", text="Son Gönderi Tarihi:")
tree.pack(padx=20, pady=20)

root.mainloop()
