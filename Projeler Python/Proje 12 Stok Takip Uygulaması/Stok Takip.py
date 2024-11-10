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
        
        self.tablo = ttk.Treeview(root, columns= ("ID", "Ürün Adı", "Adet", "Birim Fiyat"), show="headings")
        self.tablo.heading("ID", text="ID")
        self.tablo.heading("ürün Adı", text="ürün Adı")
        self.tablo.heading("Adet", text="Ade")
        self.tablo.heading("Birim Fiyat", text="Birim Fiyat")
        self.tablo.heading("Toplam Değer", text="Toplam Değer")
        self.tablo.grid(row=6, column=0, columnspan=4)
        self.tablo.bind("<ButtonRelease-1>", self.satir_sec)
        self.verileri_yukle()

    def ekle(self):
        id = self.id_entry.get()
        urun_adi = self.urun_adi_entry.get()
        adet = float(self.adet_label.get())
        birim_fiyati = float(self.birim_fiyat_entry.get())
        toplam_deger = adet * birim_fiyati
    
        self.cursor.execute("INSERT INTO stoklar (urun_adi, stok_miktari, fiyat) VALUES (?,?,?)", (id, urun_adi, adet, birim_fiyati, toplam_deger))
        self.conn.commit()
    
    
        self.tablo.insert("", "end", values=(id, urun_adi, adet, birim_fiyati, toplam_deger))
        self.girisleri_temizle()
    def girisleri_temizle(self):
        self.id_entry.delete(0,tk.END)
        self.urun_adi_entry.delete(0, tk.END)
        self.adet_label.delete(0, tk.END)
        self.birim_fiyat_entry.delete(0, tk.END)
    def arama(self,event):
        arama_metni = self.arama_entry.get().lower()
        for item in self.tablo.get_children():
        values = self.tablo.item(item)["values"]
        if arama_metni in values[0].lower() or arama_metni in values[1].lower() or arama_metni in values[2].lower() or arama_metni in values[3].lower():
            self.tablo.selection_set(item)
            self.tablo.see(item)
        else:
            self.tablo.selection_remove(item)
    def satir_sec(self, event):
        secili = self.tablo.selection()
        if secili:
            item = self.tablo.item(secili)
            values = item["values"]
            self.id_entry.delete(0, tk.END)
        self.id_entry.insert(0, values[0])
        self.urun_adi_entry.delete(0, tk.END)
        self.urun_adi_entry.insert(0, values[1])
        self.adet_label.delete(0, tk.END)
        self.adet_label.insert(0, values[2])
        self.birim_fiyat_entry.delete(0, tk.END)
        self.birim_fiyat_entry.insert(0, values[3])
        
    
    
            

        
        
        
        

if __name__ == "__main__":
    root = tk.Tk()
    app = StokTakipUygulaması(root)
    root.mainloop()
        