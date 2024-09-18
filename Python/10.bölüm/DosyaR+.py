import codecs as cs

with cs.open("deneme.txt","r+",encoding="utf-8") as dosya:
    # dosya.write ("\n2.Mahmut")
    dp = dosya.read()
    dosya.seek(0)