class okul:
    şube = "11-C"
    öğretmen = "Ali"
    bölüm = "Bilişim Teknolojileri"
    mevcut = "34"
    
    def bilgileri_göster(self):
        print()
       print("Şube:{}Öğretmen:{}Bölüm{}Sınıf Mevcudu:{}".format(self.şube,self.öğretmen,self.bölüm,self.mevcut))
    
    
    
sınıf_oluştur = okul("*"*45)
sınıf_oluştur.bilgileri_göster()
