import tkinter as tk
from tkinter import messagebox
import requests
import pyperclip


def shorten_url():
    long_url = entry.get
    responce = requests.get(f'http://tinyurl.com/api-create.php?url={long_url}')
    short_url = responce