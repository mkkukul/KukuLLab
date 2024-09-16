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
        print(i, ":" , j)
    input("devam edilsin mi")     

def no_sil(x):
    print("kişi sdilme ekrenına Hoşgeldiniz")
    silinicek_kişi = input("silinecek kişiyi yazınız:")
    x = tel_rehberi.pop(silinicek_kişi)
    input("devam edilsin mi")

 
while True:
    print("HoşT")
    print("SeçimYapınız")
    seçim_yap = int(input("1-Ekle\n2-Sil\n3-Rehberi GörX\n"))
    if seçim_yap == 1:
        tel_no_ekle(tel_rehberi)
    elif seçim_yap == 2:
        no_sil(tel_rehberi)
    elif seçim_yap == 3:
        tel_rehber_göster(tel_rehberi)
    else:
        print("yanlış seçim yaptınız")
