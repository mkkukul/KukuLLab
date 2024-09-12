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
lig = {"GS":"51P","FB":"53P","BJK":"57P","TS":"61P"}
lig.pop("GS")
print(lig)