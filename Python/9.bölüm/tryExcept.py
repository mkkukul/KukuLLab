
# sayı1 = int(input("Sayı 1"))
# sayı2  = int(input("Sayı 2"))

# toplam = sayı1/sayı2
# print(toplam)
try:
    sayı1 = int(input("Sayı 1"))
    sayı2  = int(input("Sayı 2"))
    toplam = sayı1/sayı2
    print(toplam)
# except ZeroDivisionError:
#     print("Bir Sayı sıfıra Bölünemez")
# except ValueError:
#     print("Lütfen Sayı Giriniz")
except(ZeroDivisionError,ValueError):
    print("hata var")