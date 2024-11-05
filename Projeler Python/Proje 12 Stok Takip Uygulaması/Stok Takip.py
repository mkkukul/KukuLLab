import tkinter as tk
from tkinter import ttk
import sqlite3

class StokTakipUygulaması:
    def __init__(self,root):
        self.root = root
        self.root.title("Stok Takip Uygulaması")
        # self.root.geometry("800x600")
        # self.root.configure(bg="#f0f0f0")

        self.conn = sqlite3.connect("stok_takip.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS stoklar (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                urun_adi TEXT,
                stok_miktari INTEGER,
                fiyat REAL
            )
        """)

        self.conn.commit()

        self.urun_adi_var = tk.StringVar()
        self.stok_miktari_var = tk.IntVar()
        self.fiyat_var = tk.DoubleVar()

        self.urun_adi_var.set("")
        self.stok_miktari_var.set(0)
        self.fiyat_var.set(0.0)

        self.stoklar = []

        self.ana_kisim()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = StokTakipUygulaması(root)
    root.mainloop()
        