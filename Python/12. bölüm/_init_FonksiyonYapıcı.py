class okul:
    def __init__(self, şube, öğretmen, bölüm, mevcut):
        self.şube = şube
        self.öğretmen = öğretmen
        self.bölüm = bölüm
        self.mevcut = mevcut
    
    
    def bilgileri_göster(self):
        print("*"*45)
        print("Şube:{}Öğretmen:{}Bölüm{}Sınıf Mevcudu:{}".format(self.şube,self.öğretmen,self.bölüm,self.mevcut))
        print("*"*45)
    
birinci_sınıf = okul("11C ","Ali Çeliker ", "Sporcu ", "28")
birinci_sınıf.bilgileri_göster()    
ikinci_sınıf = okul("9C ","Mahmut Çeliker ", "Beden Eğitimi ", "22")
ikinci_sınıf.bilgileri_göster()    
# sınıf_oluştur = okul()
# sınıf_oluştur.bilgileri_göster()
