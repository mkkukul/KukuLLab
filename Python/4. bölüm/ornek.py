atesiniziyaziniz = float((input("lütfen ates derecenizi yaziniz ")))
oksuruk = input("oksurüğünüz var mı ? E/H").lower()
basAgrisi = input("baş ağrısı var mı ? E/H").lower()
gun = int(input("Şikayetiniz kaç günden beri devam ediyor ? "))
if atesiniziyaziniz >= 39:
    if gun >=3:
        print("UYARI HASTANEYE GİDİNİZ") 
    else:
        print("ACİL  OLARAK HASTANAYE GİDİNİZ")

if (atesiniziyaziniz >= 39) and (oksuruk=="e") and (basAgrisi=="e") and ( gun >=3):
    print("ACİL  OLARAK HASTANAYE GİDİNİZ")
    print("Yanıyorsun fuat abi")


elif (atesiniziyaziniz <= 39) or (oksuruk=="e") or (basAgrisi=="e") or ( gun >=3):
    print("UYARI HASTANEYE GİDİNİZ")
else:
    print("Eve gidin ve dinlenin")