import random

kullanıcılar = list()
def kullanıcı_ekle(x):
    print("-"*30)
    print("Kulllanıcı Ekleme Ekranı:")
    ekle = input("Lütfen Eklenecek Kullanıcıyı Yazınız:")
    kullanıcılar.append(ekle)


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
        print(str(say)+"-Kullanıcı Adı: ", i)
        say+=1
    print("-"*30)
    
def salla(x):
    say =1
    random.shuffle(x)
    for i in x:
        print(str(say)+"-Kullanıcı Adı:", i)
        say+=1
    
while True:
    print("****ÇArk*****")
    seçim = int(input("1-Kullanıcı Ekle\n2-Kullanıcı Görüntüle\n3-Kullanıcı Seç\n4-Salla\n"))
    
    if seçim == 1:
        kullanıcı_ekle(kullanıcılar)
    elif seçim == 2:
        kullanıcı_gör(kullanıcılar)
    elif seçim == 3:
        salla(kullanıcılar)
    elif seçim == 4:
        seç(kullanıcılar)
    else:
        print("Lütfen uygun bir tercih yapınız.")
             