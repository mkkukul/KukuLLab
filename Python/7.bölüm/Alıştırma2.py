tel_rehberi = dict()

def tel_no_ekle(x):
    print("numara ekleme")
    numara_no_al = input("lütfen kayıt isim:")
    numara_no_al = input("lütfen telefon numarası giriniz:")
    x = tel_rehberi.setdefault(numara_isim_al,numara_no_al)