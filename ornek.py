atesiniziyaziniz = float((input("lütfen ates derecenizi yaziniz ")))
oksuruk = input("oksurüğünüz var mı ? E/H").lower()
basAgrisi = input("baş ağrısı var mı ? E/H").lower()
gün = int(input("Şikayetiniz kaç günden beri devam ediyor ? "))
if atesiniziyaziniz >= 39:
    if gün >=3:
        print("UYARI HASTANEYE GİDİNİZ") 
    else:
        print("ACİL  OLARAK HASTANAYE GİDİNİZ")
    