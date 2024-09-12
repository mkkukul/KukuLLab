# lig = {"GS":"51P","FB":"53P","BJK":"57P","TS":"61P"}
# lig.setdefault{"BSK","16P"}

# print(lig)
# ************************************************
# lig = {"GS":"51P","FB":"53P","BJK":"57P","TS":"61P"}
# takimEkle = input("Takım Giriniz")
# puanEkle = input("Puan Giriniz")
# # lig[takimEkle] = puanEkle 1 yöntem
# lig.setdefault(takimEkle,puanEkle)

# print(lig)

# ************************************************

# lig = {"GS":"51P","FB":"53P","BJK":"57P","TS":"61P"}
# takimEkle = input("Takım Giriniz")
# puanEkle = input("Puan Giriniz")
# lig.setdefault(takimEkle,puanEkle)
# for i, d in lig.items():
#     print(i,d)
# ************************************************

# ************************************************ Veri Silme
# lig = {"GS":"51P","FB":"53P","BJK":"57P","TS":"61P"}
# lig.pop("GS")
# print(lig)
# takimEkle = input("Takım Giriniz")
# # puanEkle = input("Puan Giriniz")


# ************************************************ Veri Silme

lig = {"GS":"51P","FB":"53P","BJK":"57P","TS":"61P"}

while True:
    takimEkle = input("Takım Giriniz: ")
    puanEkle = input("Puan Giriniz: ")
    lig.setdefault(takimEkle,puanEkle)
    
    for i,j in lig.items():
        print(i,j)
    
    secim = input("Çıkmak İstermisiniz E/H").upper()
    if secim == "E":
        print("Bedel Ödendi")
        break
    else:
        pass

