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