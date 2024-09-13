while True:
    print ("hoşgeldiniz")
    print ("seçim yapınız")
    secimYap = int(input("1-Ekle\n2-Sil\n3-Rehberi Gör\n"))
    
    if secimYap == 1:
        telNo(telRehberi)
    elif secimYap ==2:
        noSil(telRehberi)
    elif secimYap == 3:
        telRehber(telRehberi)
    else:
        print("Geçersiz Seçim")