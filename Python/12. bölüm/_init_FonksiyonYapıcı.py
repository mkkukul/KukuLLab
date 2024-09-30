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
    # def öğretmen_adı(self):
    #     print("Öğretmen Adı:",self.öğretmen)
    
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
        
        # self.şube = şube
        # self.öğretmen = öğretmen
        # self.bölüm = bölüm
        # self.mevcut = mevcut
        # self.kıdem = kıdem
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
        

while True:
    seçim_yap = input("1-Öğretmen Girişi\n2-Yönetici Girişi")
    # ilkel yöntem
    if seçim_yap == "1":
        sınıf_adı = input("Lütfen Şube Numarasını giriniz")
        öğretmen_bilgisi = input("Lütfen İsminizi Giriniz:")
        bölüm_al = input("Lütfen Branşınızı Giriniz:")
        mevcut = input("Sınıf Mevcudunu Giriniz:")
        maaş_miktarı = input("Maaş Miktarını Giriniz:")
        sınıf_oluştur = input("Sınıf Oluşturunuz:")
        sınıf_oluştur = okul(sınıf_adı,öğretmen_bilgisi,bölüm_al,mevcut,maaş_miktarı)
        print("Sınıf Oluşturuldu")
        tercih_yap = input("1-Bilgileri Göster\n2-Branş Değiştir.\n3-Maaş Göster")
        if tercih_yap == "1":
            sınıf_oluştur.bilgileri_göster()
        elif tercih_yap == "2":
            sınıf_oluştur.branş_değiş()
        elif tercih_yap == "3":
            sınıf_oluştur.maaş_göster()    
            
    
    
    
   


         
# yönetici = müdür("11","Ali Ece","Yorumcu","56","Müdür Yardımcısı","4500")
# yönetici.maaş_göster()
# yönetici.zam_yap()



# öğretmen_1 = okul("11-C","Tuncay Erol","Teknoloji","49","4500")
# öğretmen_1.bilgileri_göster()
# öğretmen_1.maaş_göster()

# yönetici = müdür("11","Ömer","Kurt","45","BaşYardımcı")
# yönetici.bilgileri_göster()

# yönetici.bilgileri_göster()
# yönetici.branş_değiş()





# while True:
#     sınıf_adı = input("Lütfen Şube Numarasını giriniz")
#     öğretmen_bilgisi = input("Lütfen İsminizi Giriniz:")
#     bölüm_al = input("Lütfen Branşınızı Giriniz:")
#     mevcut = input("Sınıf Mevcudunu Giriniz:")
#     sınıf_oluştur = input("Sınıf Oluşturunuz:")
    
#     sınıf_oluştur = okul(sınıf_adı, öğretmen_bilgisi, bölüm_al, mevcut)
#     print("Hoşgeldiniz")
#     seçim = input("Branş Değiştirmek için lütfen 1 tuşuna basınız: ")
#     if seçim == "1":
#         sınıf_oluştur.branş_değiş()
#     else:
#         print("İşlem Bitti Koçero...")
#         break






        
# sınıf_1 = okul("11C ","Ali Çeliker ", "Sporcu ", "28")
# sınıf_1.bilgileri_göster()
# sınıf_1.branş_değiş()



# birinci_sınıf = okul("11C ","Ali Çeliker ", "Sporcu ", "28")
# birinci_sınıf.bilgileri_göster()    
# ikinci_sınıf = okul("9C ","Mahmut Çeliker ", "Beden Eğitimi ", "22")
# ikinci_sınıf.bilgileri_göster()
# ikinci_sınıf.öğretmen_adı()    
# sınıf_oluştur = okul()
# sınıf_oluştur.bilgileri_göster()
