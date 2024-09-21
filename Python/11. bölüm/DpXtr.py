import sqlite3

# Veritabanı bağlantısı oluşturuluyor
db = sqlite3.connect("kitaplar.db")
yetki = db.cursor()

# Kullanıcıdan girdiler alınıyor
kitap_adı = input("Kitabının Adını Giriniz: ")
kitap_sayfaNosu = input("Kitabın Sayfa Sayısını Giriniz: ")
kitap_Yılı = input("Kitabın Yılını Giriniz: ")

# Tablo oluşturuluyor (eğer yoksa)
yetki.execute("""
CREATE TABLE IF NOT EXISTS kitaplar (
    isim TEXT,
    sayfasayisi INTEGER,
    kitapyili INTEGER
)
""")

# Veri ekleniyor (parametreler kullanılarak)
yetki.execute('INSERT INTO kitaplar VALUES (?, ?, ?)', (kitap_adı, kitap_sayfaNosu, kitap_Yılı))
yetki.execute("SELECT *FROM ")

# yetki.execute.fetchall()

# Değişiklikleri kaydedip bağlantıyı kapatıyoruz
db.commit()
db.close()