class okul:
    def __init__(self,şube,öğretmen,bölüm,mevcut,maaş):
        self.şube = şube
        self.öğretmen = öğretmen
        self.bölüm = bölüm
        self.mevcut = mevcut
        self.maaş = maaş
    
    
    def bilgileri_göster(self):
        print("*"*45)
        print("\nŞube:{}\nÖğretmen: {}\nBölüm: {}\nSınıf Mevcudu: {}\n".format(self.şube,self.öğretmen,self.bölüm,self.mevcut))
        print("*"*45)

    
    def branş_değiş(self):
        yeni_branş = input("Lütfen Yeni Branşınızı Giriniz:")
        print("****Eski Branş***", self.bölüm)
        self.bölüm = yeni_branş
        print("*"*45)
        print("\nŞube: {}\nÖğretmen: {}\nBölüm: {}\nSınıf Mevcudu: {}\n".format(self.şube,self.öğretmen,self.bölüm,self.mevcut))
        print("*"*45)
    
    def maaş_göster(self):
        print(f"{self.öğretmen}'adlı öğretmenin maaşı {self.maaş}")


class müdür(okul):
    print("Yönetici Paneli")
    def __init__(self, şube, öğretmen, bölüm, mevcut,kıdem, maaş):
        super().__init__(şube,öğretmen,bölüm,mevcut,maaş)
        self.kıdem = kıdem  # ekstra özellik: kıdem
        
    def bilgileri_göster(self):
        print("*"*45)
        print("Yönetici Paneli")
        print("\nŞube:{}\nÖğretmen: {}\nBölüm: {}\nSınıf Mevcudu: {}\nKıdem: {}".format(self.şube,self.öğretmen,self.bölüm,self.mevcut,self.kıdem))
        print("*"*45)
    
    def zam_yap(self):
        print(f"Zam Ekranına Hoşgeldiniz Sayın: {self.öğretmen}")
        zam_miktarı = int(input("Lütfen Maaş Miktarını TL cinsinden yazınız: "))
        self.maaş = int(self.maaş) + zam_miktarı
        print(f"{self.öğretmen}'adlı öğretmenin maaşına {zam_miktarı}'zam yapıldı")
        print(f"{self.öğretmen}'adlı öğretmenin güncel maaşı: {self.maaş}'tldir.")



sınıf_adı = input("Lütfen Şube Numarasını giriniz")
öğretmen_bilgisi = input("Lütfen İsminizi Giriniz:")
bölüm_al = input("Lütfen Branşınızı Giriniz:")
mevcut = input("Sınıf Mevcudunu Giriniz:")
maaş_miktarı = int(input("Maaş Miktarını Giriniz:"))
print("BU ALANI SADECE YÖNETİCİ İSENİZ DOLDURUNUZ")
kıdem_al = input("Lütfen Kıdem Seviyenizi Giriniz: ")
if not kıdem_al:
    print("Öğretmen Modundasınız")

sınıf_oluştur = input("Sınıf Oluşturunuz:")

while True:
   if not kıdem_al:
       sınıf_oluştur = okul(sınıf_adı,öğretmen_bilgisi,bölüm_al,mevcut,maaş_miktarı)
       soru_sor = input("1-Bilgileri Göster\n2-Maaşı Göster\n3-Branşı Değiştir\n")
       if soru_sor == "1":
           sınıf_oluştur.bilgileri_göster()
       elif soru_sor =="2":
            sınıf_oluştur.maaş_göster()
       elif soru_sor == "3":
          sınıf_oluştur.branş_değiş()
       else:
           print("Lütfen Geçerli Bir Seçim Yapınız")
    else:
        sınıf_oluştur 