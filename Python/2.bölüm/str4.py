buyukHarfler  = "NE MUTLU TÜRKÜM DİYENE".lower()
kucukHarfler = "ne mutlu turkum diyene".upper()
sadeceBasHarfliBuyuk = "ne mutlu".capitalize()
tamTersi = "kardesim".swapcase()
tamTersi = " KARDESİM"
tamTersi = tamTersi.swapcase()
sil = "+++gulyabini+++".strip("+")
print("tuncay","erol", sep=":") 
# sep burada virgülü siler
# sep yerine end eklersek sonu ekler
adi = "turkan"
soyadi = "kaya"
yasi = 30

# print("Kişinin adı", adi, "Soyadı", soyadi, "Kişinin Yaşı", yasi)
print("Kişinin Adı:{}\nKişinin Soyadı:{}\nKişinin Yaşı{}".format(adi,soyadi,yasi))