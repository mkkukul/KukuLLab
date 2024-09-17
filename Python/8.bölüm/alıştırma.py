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
    for i in x:
        print(str(say+"-Kullanıcı Adı:",i))
        say+=1
    print("-"*30)

def seç(x):
    say = 1
    kişi_seç =int(input("kaç kişi Seçilsin"))
    rastgle_seç = random.sample(x,kişi_seç)
    
    for i in rastgle_seç:
        print(str(say)+"-Sanşlı kişi: ", i)
        say+=1
    print("-"*30)
    
def salla(x):
    say =1
    random.shuffle(x)
    for i in x:
        print(str(say)+"-Sallanan kişi: ", i)
        say+=1
    
while True:
    print("****ÇArk*****")
    seçim = input("1-Kullanıcı Ekle\n2-Kullanıcı Görüntüle\n3-Kullanıcı Seç\n4-Salla\n5-Çıkış")
        