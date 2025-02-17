import tkinter as tk
from tkinter import ttk
import sqlite3

class StokTakipUygulaması:
    def __init__(self,root):
        self.root = root
        self.root.title("Stok Takip Uygulaması")

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
        self.adet_entry = tk.Entry(root)  # Düzeltme: 'adet_entry' olarak tanımlandı
        self.adet_entry.grid(row=2, column=1)

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

        self.temizle_button = tk.Button(root, text="Temizle", command=self.girisleri_temizle)  # Düzeltme: 'Temizler' yazımı 'Temizle' olarak değiştirildi
        self.temizle_button.grid(row=4, column=3, columnspan=1)

        self.arama_label = tk.Label(root, text="Ara")
        self.arama_label.grid(row=5, column=0)
        self.arama_entry = tk.Entry(root)
        self.arama_entry.grid(row=5, column=1)

        self.arama_entry.bind("<KeyRelease>", self.arama)  # Düzeltme: 'arama_yap' yerine 'arama' işleviyle bağlandı

        self.tablo = ttk.Treeview(root, columns=("ID", "Ürün Adı", "Adet", "Birim Fiyat"), show="headings")
        self.tablo.heading("ID", text="ID")
        self.tablo.heading("Ürün Adı", text="Ürün Adı")  # Düzeltme: Doğru başlık ismi kullanıldı
        self.tablo.heading("Adet", text="Adet")          # Düzeltme: Doğru başlık ismi kullanıldı
        self.tablo.heading("Birim Fiyat", text="Birim Fiyat")
        self.tablo.grid(row=6, column=0, columnspan=4)
        self.tablo.bind("<ButtonRelease-1>", self.satir_sec)
        self.verileri_yukle()

    def ekle(self):
        id = self.id_entry.get()
        urun_adi = self.urun_adi_entry.get()
        adet = float(self.adet_entry.get())  # Düzeltme: 'adet_label' yerine 'adet_entry' kullanıldı
        birim_fiyati = float(self.birim_fiyat_entry.get())
        toplam_deger = adet * birim_fiyati

        self.cursor.execute("INSERT INTO stoklar (urun_adi, stok_miktari, fiyat) VALUES (?,?,?)", (urun_adi, adet, birim_fiyati))
        self.conn.commit()

        self.tablo.insert("", "end", values=(id, urun_adi, adet, birim_fiyati, toplam_deger))
        self.girisleri_temizle()

    def girisleri_temizle(self):
        self.id_entry.delete(0, tk.END)
        self.urun_adi_entry.delete(0, tk.END)
        self.adet_entry.delete(0, tk.END)  # Düzeltme: 'adet_label' yerine 'adet_entry' kullanıldı
        self.birim_fiyat_entry.delete(0, tk.END)

    def arama(self, event):
        arama_metni = self.arama_entry.get().lower()
        for item in self.tablo.get_children():
            values = self.tablo.item(item)["values"]
            if (arama_metni in str(values[0]).lower() or
                arama_metni in str(values[1]).lower() or
                arama_metni in str(values[2]).lower() or
                arama_metni in str(values[3]).lower()):
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
            self.adet_entry.delete(0, tk.END)  # Düzeltme: 'adet_label' yerine 'adet_entry' kullanıldı
            self.adet_entry.insert(0, values[2])
            self.birim_fiyat_entry.delete(0, tk.END)
            self.birim_fiyat_entry.insert(0, values[3])

    def duzelt(self):
        secili = self.tablo.selection()
        if secili:
            id = self.id_entry.get()
            urun_adi = self.urun_adi_entry.get()
            adet = float(self.adet_entry.get())  # Düzeltme: 'adet_label' yerine 'adet_entry' kullanıldı
            birim_fiyati = float(self.birim_fiyat_entry.get())
            toplam_deger = adet * birim_fiyati

            self.cursor.execute("UPDATE stoklar SET urun_adi=?, stok_miktari=?, fiyat=? WHERE id=?", (urun_adi, adet, birim_fiyati, id))
            self.conn.commit()

            self.tablo.item(secili, values=(id, urun_adi, adet, birim_fiyati, toplam_deger))
            self.girisleri_temizle()

    def sil(self):
        secili = self.tablo.selection()
        if secili:
            id = self.tablo.item(secili)['values'][0]
            self.cursor.execute("DELETE FROM stoklar WHERE id=?", (id,))
            self.conn.commit()
            self.tablo.delete(secili)
            self.girisleri_temizle()

    def verileri_yukle(self):
        for row in self.cursor.execute("SELECT * FROM stoklar"):
            self.tablo.insert("", "end", values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = StokTakipUygulaması(root)
    root.mainloop()
