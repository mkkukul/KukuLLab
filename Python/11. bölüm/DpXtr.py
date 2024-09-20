import sqlite3

# Veritabanı bağlantısı oluşturuluyor
db = sqlite3.connect("kitaplar.db")
yetki = db.cursor()
kitap_adı = input("Kitabının Asını Giriniz:")
kitap_sayfaNosu = input("Kitabın SayfaNosu Giriniz:")
kitap_Yılı = input("Kitabın Yılını Giriniz")
# Tablo oluşturuluyor
yetki.execute("""
CREATE TABLE IF NOT EXISTS kitaplar (
    isim TEXT,
    sayfasayisi INTEGER,
    kitapyili INTEGER
)
""")

# Veri ekleniyor
yetki.execute('INSERT INTO kitaplar VALUES (f"{kitap_adı}", "{kitap_sayfaNosu}","{kitap_Yılı}" )')
# yetki.execute('INSERT INTO kitaplar VALUES ("Savaş ve Barış", 500, 2010)')

# Değişiklikleri kaydedip bağlantıyı kapatıyoruz
db.commit()
db.close()
