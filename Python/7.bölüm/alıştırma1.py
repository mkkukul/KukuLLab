telRehberi = dict()
def telNo(x):
    print("Numara Ekleme Ekranına Hoşgeldiniz")
    nİsinAl = input("Lütfen Kayıt Edilecek Kişini Adını Yazınız:")
    nNoAl = input("Lütfen Telefon Numarısını Giriniz:")
    
    x = telRehberi.setdefault(nİsinAl,nNoAl)
    print(f"{nİsinAl}'adlı kişinin kayıttı başarılı")
    
    
# telNo(telRehberi)
def telRehber(x):
    print("Rehbere Hoşgeldiniz")
    for i,j in x.items():
        print(f"{i} : {j}")
        
telNo(telRehberi)       
telRehber(telRehberi)

def noSil(x):
    print("Kişi Silme Ekranına Hoşgeldiniz")
    sKisi= input("Silinecek Kişiyi Yaızınız: ")
    x = telRehberi.pop(noSil)
    
while True:
    print ("hoşgeldiniz")
    print ("seçim yapınız")
    secimYap = int(input("1-Ekle\n2-Sil\n3-Rehberi Gör\n"))
    
    if secimYap == 1:
        telNo(telRehberi)
    elif secimYap ==2
        noSil(telRehberi)
    elif secimYap == 3:
        telRehber(telRehberi)
    else:
        print("Geçersiz Seçim")