# dosya = open("deneme.txt","r")
# a = dosya.read()
# print(a)

import codecs as cs

with cs.open("deneme.txt","r",encoding="utf-8") as dosya:
    a = dosya.readlines()
    print(a[3])
    # say = 1
    # for i in a:
    #     print(say, i)
    #     say += 1
    # a = dosya.read()
    # print(a)
    # # dosya.open("deneme.txt","r")
    # # print(a)