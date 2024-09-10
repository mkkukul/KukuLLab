vizenetu = int(input("vize notunuzu giriniz:"))
finalnotu = int(input("final notunuzu giriniz:"))
ortalama = (vizenetu*0.4) + (finalnotu*0.6)
if ortalama >=85:
    print("AA", ortalama)
elif ortalama >=70:
    print("BB", ortalama)
elif ortalama >=60:
    print("CC", ortalama)
elif ortalama >=50:
    print("DD", ortalama) 
else:
    print("haci Gecmis olsun Kaldin")
