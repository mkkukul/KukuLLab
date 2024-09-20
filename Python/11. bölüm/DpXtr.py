import sqlite3

# Veritabanı bağlantısı oluşturuluyor
db = sqlite3.connect("kitaplar.db")
yetki = db.cursor()

# Kullanıcıdan veri alınıyor
kitap_adı = input("Kitabın Adını Giriniz: ")
kitap_sayfaNosu = int(input("Kitabın Sayfa Sayısını Giriniz: "))
kitap_Yılı = int(input("Kitabın Yılını Giriniz: "))

# Tablo oluşturuluyor
yetki.execute("""
CREATE TABLE IF NOT EXISTS kitaplar (
    isim TEXT,
    sayfasayisi INTEGER,
    kitapyili INTEGER
)
""")

# Veri ekleniyor (parametreli sorgu kullanıyoruz)
yetki.execute('INSERT INTO kitaplar (isim, sayfasayisi, kitapyili) VALUES (?, ?, ?)', (kitap_adı, kitap_sayfaNosu, kitap_Yılı))

# Değişiklikleri kaydedip bağlantıyı kapatıyoruz
db.commit()
db.close()
