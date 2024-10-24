import instaloader
import tkinter as tk
from tkinter import tkk, messagebox

def get_user_info(username):
    bot = instaloader.instaloader()
    profile = instaloader.Profile.from_username(bot.context,username)
    user_info = {
        "Username": profile.username,
        "Followers": profile.followers,
        "Followees": profile.followees,
        "Post Count"
    }