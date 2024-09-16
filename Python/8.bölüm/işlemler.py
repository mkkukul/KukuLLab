def toplama():
    x = int(input("birinci sayı :"))
    y = int(input("ikinci sayı :"))
    toplam = x + y
    print(toplam)

def çıkartma():
    x = int(input("birinci sayı :"))
    y = int(input("ikinci sayı :"))
    cıkarma = x - y
    print(cıkarma)
    
def carpma():
    x = int(input("birinci sayı :"))
    y = int(input("ikinci sayı :"))
    carp = x * y 
    print(carp)
    
def bölme():
    x = int(input("birinci sayı :"))
    y = int(input("ikinci sayı :"))
    if y == 0:
        print("Sıfıra bölme hatası!")
    else:
        böl = x / y
        print(böl)