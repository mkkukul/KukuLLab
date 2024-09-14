tel_rehberi = dict()

def tel_no_ekle(x):
    print("numara ekleme")
    numara_isim_al = input("lütfen kayıt isim:")
    numara_no_al = input("lütfen telefon numarası giriniz:")
    x = tel_rehberi.setdefault(numara_isim_al,numara_no_al)
    print(f"{numara_isim_al}' adlı kişi telefon listesine eklendi ...")
    
def tel_rehber_göster(x):