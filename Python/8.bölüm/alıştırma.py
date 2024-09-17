import random

kullanıcılar = list()
def kullanıcı_ekle(x):
    print("-"*30)
    print("Kulllanıcı Ekleme Ekranı:")
    ekle = input("Lütfen Eklenecek Kullanıcıyı Yazınız:")
    kullanıcılar.append(ekle)

kullanıcı_ekle(kullanıcılar)
# for i in kullanıcılar
# print(i)

def kullanıcı_gör(x):
    say = 1
    print("-"*30)
    for i in x
        print(str(say+"-Kullanıcı Adı:",i))
        say+=1
    print("-"*30)
    
    