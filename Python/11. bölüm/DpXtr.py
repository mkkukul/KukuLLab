import sqlite3

# Veritabanı bağlantısı oluşturuluyor
db = sqlite3.connect("kitaplar.db")
yetki = db.cursor()

# Tablo oluşturuluyor
yetki.execute("""
CREATE TABLE IF NOT EXISTS kitaplar (
    isim TEXT,
    sayfasayisi INTEGER,
    kitapyili INTEGER
)
""")

# Veri ekleniyor
yetki.execute('INSERT INTO kitaplar VALUES ("Çalıkuşu", 359, 1978)')
yetki.execute('INSERT INTO kitaplar VALUES ("Savaş ve Barış", 500, 2010)')

# Değişiklikleri kaydedip bağlantıyı kapatıyoruz
db.commit()
db.close()
