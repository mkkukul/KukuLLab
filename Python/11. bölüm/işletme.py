import sqlite3

db = sqlite3.connect("veresiye.db")
yetki = db.cursor()
yetki.execute("CREATE TABLE IF NOT EXISTS kisiler(isim,borç)")


while True:
    print("***VERESİYE DEFTERİNE HOŞGELDİNİZ***")
    sor = input("1-BORÇLU EKLE:\n2-BORÇLULARI GÖR:\n")
    if sor == "1":
        borçlu_isim = input("Lütfen Borçlunun İsim Giriniz: ")
        borç_miktarı = input("Lütfen Borç Miktarını Giriniz: ")
        yetki.execute(f"INSERT INTO kisiler VALUES('{borçlu_isim}','{borç_miktarı}')")
        db.commit()
        print(f"İşlem Tamamlandı, Borçlu Kişinin Adı:{borçlu_isim}")
    elif sor == "2":
        yetki.execute("SELECT *FROM kisiler")
        yazdır = yetki.fetchall()
        say = 1
        for i in yazdır:
            print("******************************BORÇLU BİLGİSİ******************************")
            print(f"{say}- Borçlu:{i[0]}\nBorç:{i[1]}\n")
            say+=1
        input("Devam Edilsin mi ?")
        
        
        # for i in yetki:
        #     print(f"Borçlu:{i[0]} Borç:{i[1]}")
       