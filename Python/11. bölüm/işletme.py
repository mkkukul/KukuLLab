import sqlite3

db = sqlite3.connect("veresiye.db")
yetki = db.cursor()
yetki.execute("CREATE TABLE IF NOT EXISITS kisiler(isim,borç)")


while True:
    print("***VERESİYE DEFTERİNE HOŞGELDİNİZ***")
    sor = input("1-BORÇLU EKLE:\n2-BORÇLULARI GÖR\n")
    if sor == "1":
        borçlu_isim = input("Lütfen Borçlunun İsim Giriniz: ")
        borç_miktarı = int(input("Borç giriniz: "))
        yetki.execute("INSERT INTO kisiler VALUES(?,?)", (isim, borç))
        db.commit()