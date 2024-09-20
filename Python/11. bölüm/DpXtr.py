import sqlite3

# Veritabanı bağlantısı oluşturuluyor
dp = sqlite3.connect("kitaplar.db")
yetki = dp.cursor()

# Tablo oluşturuluyor
yetki.execute("""
CREATE TABLE IF NOT EXISTS kitaplar (
    isim TEXT,
    sayfa_sayisi INTEGER,
    kitap_yili INTEGER
)
""")

# Veri ekleniyor
yetki.execute('INSERT INTO kitaplar VALUES ("Çalıkuşu", 359, 1978)')

# Değişiklikleri kaydedip bağlantıyı kapatıyoruz
dp.commit()
dp.close()
