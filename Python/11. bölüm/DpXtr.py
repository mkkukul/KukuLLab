import sqlite3


dp  = sqlite3.connect("kitaplar.db")
yetki = dp.cursor()
yetki.execute("CREATE TABLE IF NOT EXISTS kitaplar (kitap_adi TEXT, yazar_adi TEXT, yayin_evi TEXT, sayfa_sayisi INT)")
yetki.execute("INSERT INTO KİTAPL")