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
        
        messagebox.showinfo("Başarılı",)
        