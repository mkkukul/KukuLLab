dbka = "admin"
dbps = 1234
while True:
    kullanıciadi= input(" Kullanıcı adını giriniz")
    kullanıcips = int(input("şifre giriniz:"))
    if (dbka == kullanıciadi and dbps == kullanıcips):
        print("Giriş başarılı")
        break
    elif (dbka != kullanıciadi and dbps == kullanıcips):
        print("Kullanıcı Adı Hatalı")
    elif (dbka == kullanıciadi and dbps != kullanıcips):
        print("Kullanıcı Şifre Hatalı")
        print("şifre değiştirilsin mi? E/H")
        cevap = input()
        if cevap == "E":
            print("şifreniz Değiştiriliyor")
            yenipass = int(input("Yeni şifre giriniz:"))