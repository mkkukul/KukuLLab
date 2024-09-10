for i in range(3):
    sifre = input("Lütfen Şifre belirleyiniz")
    if not sifre:
        print("şifre belirtilmedi")
    elif len(sifre) in range(3,8):
        print("şifre belirlendi",sifre)
        break
    elif i == 2:
        print("şifre belirleme hakkınız bitti, Lütfen 15 dakkika bekleyiniz")

    else:
        print("şifre 3-8 karakter arasında olmalı")   