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
        self.id_label = tk.Label(self.root, text="ID:")
        self.id_label.grid(row=0, column=0)
        self.id_entry = tk.Entry(self.root)
        self.id_entry.grid(row=0, column=1)
        
        
        self.urun_adi_label = tk.Label(root, text="Ürün Adı:")
        self.urun_adi_label.grid(row=1, column=0)
        self.urun_adi_entry = tk.Entry(root)
        self.urun_adi_entry.grid(row=1, column=1)
        
        self.adet_label = tk.Label(root, text="Adet:")
        self.adet_label.grid(row=2, column=0)
        self.adet_label = tk.Entry(root)
        self.adet_label.grid(row=2, column=1)
        
        
        self.birim_fiyat_label = tk.Label(root, text="Birim Fiyat:")
        self.birim_fiyat_label.grid(row=3, column=0)
        self.birim_fiyat_entry = tk.Entry(root)
        self.birim_fiyat_entry.grid(row=3, column=1)
        
        self.ekle_button = tk.Button(root, text="Ekle", command=self.ekle)
        self.ekle_button.grid(row=4, column=0)
        
        self.duzelt_button = tk.Button(root, text="Düzelt", command=self.duzelt)
        self.duzelt_button.grid(row=4, column=1, columnspan=1) 
        
        self.sil_button = tk.Button(root, text="Sil", command=self.sil)
        self.sil_button.grid(row=4, column=2, columnspan=1)
        
        self.temizle_button = tk.Button(root, text = "Temizler", command=self.girisleri_temizle)
        self.temizle_button.grid(row=4, column=3, columnspan=1)
        
        self.arama_label = tk.Label(root, text="Ara")
        self.arama_label.grid(row=5, column=0)
        self.arama_entry = tk.Entry(root)
        self.arama_entry.grid(row=5, column=1)
        
        self.arama_entry.bind("<KeyRelease>", self.arama_yap)
        
        self.tablo = ttk.Treeview
        
        
        
        
        
        
        
        
        
        # self.urun_adi_var = tk.StringVar()
        # self.stok_miktari_var = tk.IntVar()
        # self.fiyat_var = tk.DoubleVar()

        # self.urun_adi_var.set("")
        # self.stok_miktari_var.set(0)
        # self.fiyat_var.set(0.0)

        # self.stoklar = []

        # self.ana_kisim()
        
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = StokTakipUygulaması(root)
#     root.mainloop()
        