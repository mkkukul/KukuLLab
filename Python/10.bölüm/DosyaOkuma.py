# dosya = open("deneme.txt","r")
# a = dosya.read()
# print(a)

import codecs as cs

with cs.open("deneme.txt","r",encoding="utf-8") as dosya:
    a = dosya.readlines()
    print(a)
    # a = dosya.read()
    # print(a)
    # # dosya.open("deneme.txt","r")
    # # print(a)