import time
try:
    sayı1 = int(input("Sayı 1"))
    sayı2  = int(input("Sayı 2"))
    toplam = sayı1+sayı2
    print(toplam)
except ValueError:
    print("Lütfen Sayı Giriniz")
    
finally:
    sayaç = 5
    for i in range(5):
        print("Geri Sayım", sayaç)
        sayaç -=1
        time.sleep(1)
        if sayaç == 0:
            print("işlem tamamlandı")
        # print("Program Bitti")
        
# print("Program Bitti")