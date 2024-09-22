import sqlite3

db = sqlite3.connect("veresiye.db")
yetki = db.cursor()
yetki.execute("CREATE TABLE IF NOT EXISITS kisiler(isim,borç)")


while True:
    print("***VERESİYE DEFTERİNE HOŞGELDİNİZ***")
    sor = input("1-BORÇLU EKLE:\n2-BORÇLULARI GÖR\n")
    if sor == "1":
        borçlu_isim = input("Lütfen Borçlunun İsim Giriniz: ")
        borç_miktarı = int(input("Lütfen Borç Miktarını Giriniz: "))
        yetki.execute(f"INSERT INTO kisiler VALUES('{borçlu_isim}','{borç_miktarı}')")
        db.commit()
        print("")