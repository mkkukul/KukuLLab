import sqlite3

db = sqlite3.connect("kitaplar.dp")

yetki = db.cursor()

yetki.execute("CREATE TABLE IF NOT EXISTS arteta (isim,sayfasayısı,kitapyılı)")
yetki.execute('INSERT INTO arteta VALUES("Çalıkuşu","359","1978")')
yetki.execute('INSERT INTO arteta VALUES("Savaş ve Barış", "500", "2010")')
db.commit()
db.close()