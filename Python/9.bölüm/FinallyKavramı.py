try:
    sayı1 = int(input("Sayı 1"))
    sayı2  = int(input("Sayı 2"))
    toplam = sayı1+sayı2
    print(toplam)
except ValueError:
    print("Lütfen Sayı Giriniz")
    
finally:
    print("Program Bitti")