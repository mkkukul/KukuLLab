import sqlite3


dp  = sqlite3.connect("kitaplar.db")
yetki = dp.cursor()
yetki.execute("CREATE TABLE IF NOT EXISTS kitaplar (isim, saysayısı, kitapyılı)")
yetki.execute('INSERT INTO kitaplar VALUES("Çalıkuşu","359"."1978")')
dp.commit()
dp.close()