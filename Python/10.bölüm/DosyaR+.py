import codecs as cs

# with cs.open("deneme.txt","r+",encoding="utf-8") as dosya:
#     # dosya.write ("\n2.Mahmut")
#     dp = dosya.read()
#     dosya.seek(0)
#     dp = "2.mahmut\n" + dp
#     dosya.write(dp)


with cs.open("deneme.txt","r+",encoding="utf-8") as dosya:
    dp = dosya.readlines()
    dp.insert(2,"Makamı MAhmut\n")
    dosya.seek(0)
    dosya.writelines(dp)