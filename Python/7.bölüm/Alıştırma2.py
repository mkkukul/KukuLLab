tel_rehberi = dict()

def tel_no_ekle(x):
    print("numara ekleme")
    numara_isim_al = input("lütfen kayıt isim:")
    numara_no_al = input("lütfen telefon numarası giriniz:")
    x = tel_rehberi.setdefault(numara_isim_al,numara_no_al)
    print(f"{numara_isim_al}' adlı kişi telefon listesine eklendi ...")
    
def tel_rehber_göster(x):
    print  ("rehbere Hoşgeldiniz")
    for i,j in x.items():
        print(i ":" j)

def no_sil(x):
    print("kişi sdilme ekrenına Hoşgeldiniz")
    silinicek_kişi = input("silinecek kişiyi yazınız:")
    x = tel_rehberi.pop(silinicek_kişi)