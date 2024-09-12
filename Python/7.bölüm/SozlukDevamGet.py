lig = {"GS":"51P","FB":"53P","BJK":"57P","TS":"61P"}
takim = input("Lütfen Puanını Öğrenmek istediğiniz Takımı Yazınız:").upper()
# .capitalize
# print(takim,lig[takim])
# if takim not in lig:
#     print("Seçtiğiniz Takım Listemizde Bulunmuyor")
# else:
# print(takim,":"lig[takim])

print(takim,":",lig.get(takim,"Seçtiğiniz Takım Listemizde Bulunmuyor"))