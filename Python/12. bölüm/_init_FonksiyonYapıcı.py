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
        print{f"{} 'adlı öğretmenin maaşı{self.maaş}"}


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

yönetici = müdür("11","Ömer","Kurt","45","BaşYardımcı")
yönetici.bilgileri_göster()

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
