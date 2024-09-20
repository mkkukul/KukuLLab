import sqlite3

# Veritabanı bağlantısı oluşturuluyor
dp = sqlite3.connect("kitaplar.db")
yetki = dp.cursor()

# Tablo oluşturuluyor (isimleri düzeltildi)
yetki.execute("""
CREATE TABLE IF NOT EXISTS kitaplar (
    isim TEXT,
    sayfa_sayisi INTEGER,
    kitap_yili INTEGER
)
""")

# Veri ekleniyor (virgül ve nokta hatası düzeltildi)
yetki.execute('INSERT INTO kitaplar VALUES ("Çalıkuşu", 359, 1978)')

# Değişiklikleri kaydedip bağlantıyı kapatıyoruz
dp.commit()  # commit yapılmazsa veri kalıcı olmaz
dp.close()
