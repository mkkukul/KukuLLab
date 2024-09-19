import codecs
dosya_oluştur = input("Lütfen Dosya Adını Giriniz:")
dosya_NEW = dosya_oluştur + ".txt"
veri_gir = input(f"Lütfen{dosya_NEW} Dosyasına Yazılacak Veriyi Giriniz:")

with codecs.open(dosya_NEW,"w", encoding="utf-8") as dosya:
    dosya.write(veri_gir)