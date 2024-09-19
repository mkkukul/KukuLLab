import codecs
dosya_oluştur = input("Lütfen Dosya Adını Giriniz:")
dosya_NEW = dosya_oluştur + ".txt"
veri_gir = input(f"Lütfen{dosya_NEW} Dosyasına Yazılacak Veriyi Giriniz: ")

with codecs.open(dosya_NEW,"w", encoding="utf-8") as dosya:
    dosya.write(veri_gir)
    soru_sor = input("Dosyasına Yazıldı. Ekleme yapmak ister Misiniz? (E/H):").upper()
    if soru_sor == "E":
        open(dosya_NEW,"a")
        yeni_veri = input("Lütfen Eklemek istiğiniz veriyi yazınız: ")
        yeni_veri = "\n" + yeni_veri
        dosya.write(yeni_veri)
        print("Verileriniz Güncellendi")