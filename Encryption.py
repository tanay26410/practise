#Encryption
import math


def encrypt(s):
    c=math.ceil(math.sqrt(len(s)))
    f=math.floor(math.sqrt(len(s)))
    li=[]
    for i in range(c):
        li.append(s[i::c])
    return ' '.join(li)

s='haveaniceday'
print(encrypt(s))