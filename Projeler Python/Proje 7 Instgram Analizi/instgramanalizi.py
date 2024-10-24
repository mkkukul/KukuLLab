import instaloader
import tkinter as tk
from tkinter import tkk, messagebox

def get_user_info(username):
    try:
        bot = instaloader.instaloader()
        profile = instaloader.Profile.from_username(bot.context,username)
    
        user_info = {
            "Username": profile.username,
            "Followers": profile.followers,
            "Followees": profile.followees,
        "Post Count": profile.mediacount,
        "Last Post Date" : get_last_post_date(profile)
        
    }
    
    return user_info