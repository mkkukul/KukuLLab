telRehberi = dict()

def telNo(x):
    print("Numara Ekleme Ekranına Hoşgeldiniz")
    nIsimAl = input("Lütfen Kayıt Edilecek Kişinin Adını Yazınız: ")
    nNoAl = input("Lütfen Telefon Numarasını Giriniz: ")
    
    telRehberi[nIsimAl] = nNoAl  # Kayıt doğrudan rehbere ekleniyor
    print(f"{nIsimAl} adlı kişinin kaydı başarılı.")

def telRehber(x):
    print("Rehbere Hoşgeldiniz")
    for i, j in x.items():
        print(f"{i} : {j}")

def noSil(x):
    print("Kişi Silme Ekranına Hoşgeldiniz")
    sKisi = input("Silinecek Kişiyi Yazınız: ")
    if sKisi in telRehberi:
        telRehberi.pop(sKisi)
        print(f"{sKisi} adlı kişi rehberden silindi.")
    else:
        print(f"{sKisi} adlı kişi rehberde bulunamadı.")

# Ana Döngü
while True:
    print("\nHoşgeldiniz!")
    print("Seçim yapınız:")
    
    secimYap = input("1-Ekle\n2-Sil\n3-Rehberi Gör\n4-Çıkış\n")

    # Girdi doğrulama
    if secimYap == "1":
        telNo(telRehberi)
    elif secimYap == "2":
        noSil(telRehberi)
    elif secimYap == "3":
        telRehber(telRehberi)
    elif secimYap == "4":
        print("Programdan çıkılıyor...")
        break  # Döngüden çık
    else:
        print("Geçersiz Seçim! Lütfen 1, 2, 3 veya 4 giriniz.")
