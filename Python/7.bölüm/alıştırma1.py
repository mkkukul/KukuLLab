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