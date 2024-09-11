# def suTuketim(adı, soyadı, yas, kilo):
#     print("*" * 25)
#     print(f"Adınız: {adı}\nSoyadınız: {soyadı}\nYaş: {yas}\nKilo: {kilo}\n")
#     # Su tüketimi formülü
#     gunluk_su = kilo * 0.03
#     print(f"Günlük {gunluk_su:.2f} litre su içmelisiniz.")

# Kullanıcıdan bilgileri alıyoruz
# ad = input("Lütfen adınızı giriniz: ")
# soyadı = input("Lütfen soyadınızı giriniz: ")
# yas = input("Lütfen yaşınızı giriniz: ")
# kilo = int(input("Lütfen kilonuzu giriniz: "))

# Fonksiyonu çağırıp su tüketimini hesaplıyoruz
# suTuketim(ad, soyadı, yas, kilo)
# def suHesapla(kilo):
#     erHesapla = kilo*0.04
#     kaHesapla = kilo*0.03
#     cinsiyet = input("Lütfen Cinsiyetinizi Giriniz : Kadın/Erkek")
#     if cinsiyet == "erkek":
#         print(erHesapla, "Litre Su içmelisiniz")
#     elif cinsiyet == "kadın":
#         print(kaHesapla, "Litre Su içmelisiniz")
    
# suHesapla(65)
def suHesapla(kilo):
    erHesapla = kilo * 0.04
    kaHesapla = kilo * 0.03
    cinsiyet = input("Lütfen cinsiyetinizi giriniz (Kadın/Erkek): ").lower()  # Küçük harfe çeviriyoruz
    if cinsiyet == "erkek":
        print(f"Günlük {erHesapla:.2f} litre su içmelisiniz.")
    elif cinsiyet == "kadın":
        print(f"Günlük {kaHesapla:.2f} litre su içmelisiniz.")
    else:
        print("Geçerli bir cinsiyet girmediniz. Lütfen 'Kadın' ya da 'Erkek' olarak giriniz.")

# Fonksiyonu çalıştırıyoruz
kiloAl = int(input("lütfen kilonuzu giriniz"))
suHesapla(kiloAl)