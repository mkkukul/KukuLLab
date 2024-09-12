# liste = ["ali", "veli", "bilim"]

# sozluk = {"Apple":"Elma"}
# print(sozluk["Apple"])

# sozluk = {"Apple":"Elma","İsim":"Tuncay","Telefon":"Apple"}
# print(sozluk["İsim"])

# sozluk = {"Apple":"Elma","İsim":"Tuncay","Telefon":"Apple"}
# print(len(sozluk))

# sozluk = {"Apple":"Elma","İsim":"Tuncay","Telefon":"Apple"}
# for i in sozluk:
#     print(i)

sozluk = {"Apple":"Elma","İsim":"Tuncay","Telefon":"Apple"}

for isim, deger in sozluk.items():
    print(isim, ":", deger)