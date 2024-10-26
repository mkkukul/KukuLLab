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

def get_last_post_date(profile)
    last_post = None
    for post in profile.get_posts():
        if not last_post or post.date_utc > last_post.date_utc:
            lost_post = post
    return last_post.date_utc.strftime("%Y-%m-%d %H:%M:%S")

def show_user():
    username = entry_username.get()
    user_info = get_user_info() 
            
            