import instaloader
import tkinter as tk
from tkinter import messagebox


def dowload_post():
    username = entry_username.get()
    
    try: 
        bot = instaloader